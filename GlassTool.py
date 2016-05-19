# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Magnifying Glass
                                 A QGIS plugin
 Magnifying Glass Tool for Qgis
                             -------------------
        begin                : 2016-05-19
        copyright            : (C) 2016 All4Gis.
        email                : franka1986@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 #   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""
#Original code: https://github.com/emka/python-lightmaps/blob/master/lightmaps.py

from PyQt4 import QtCore, QtGui, QtNetwork
import math
try:
    import sys
    from pydevd import *
except:
    None
 
HOLD_TIME = 701
MAX_MAGNIFIER = 229
tdim = 256
MIN_ZOOM = 2
MAX_ZOOM = 18

 
def SetMap(zoom,latitude,longitude):
    s = QtCore.QSettings()
    s.setValue("MagnifyingGlass/zoom", zoom)
    s.setValue("MagnifyingGlass/latitude", latitude)
    s.setValue("MagnifyingGlass/longitude", longitude)
    return 

def qHash(point):
    return (point.x(),point.y())

def tileForCoordinate(lat, lng, zoom):
    zn = 1 << zoom    # 2**zoom
    tx = (lng+180.0)/360.0
    ty = (1.0 - math.log(math.tan(lat*math.pi/180.0) + 1.0/math.cos(lat*math.pi/180.0)) / math.pi) / 2.0
    return QtCore.QPointF(tx*zn, ty*zn)

def longitudeFromTile(tx, zoom):
    zn = 1 << zoom
    lat = tx / zn * 360.0 - 180.0
    return lat

def latitudeFromTile(ty, zoom):
    zn = 1 << zoom
    n = math.pi - 2 * math.pi * ty / zn
    lng = 180.0 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n)))
    return lng

class SlippyMap(QtCore.QObject):
    updated = QtCore.pyqtSignal(QtCore.QRect)

    def __init__(self, parent=None,Url=None, width=None, height=None, zoom=None, latitude=None, longitude=None):
        QtCore.QObject.__init__(self)
        self.width = width
        self.height = height
        self.zoom = zoom
        self.latitude = latitude
        self.longitude = longitude
        SetMap(self.zoom,self.latitude,self.longitude)
 
        self.path=Url
        self.m_emptyTile = QtGui.QPixmap(tdim, tdim)
        self.m_emptyTile.fill(QtCore.Qt.lightGray)

        self.m_manager = QtNetwork.QNetworkAccessManager()
      
        cache = QtNetwork.QNetworkDiskCache()
        cache.setCacheDirectory(QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.CacheLocation))
        self.m_manager.setCache(cache)
        self.m_manager.finished.connect(self.handleNetworkData)

        self.m_url = QtCore.QUrl()
        self.m_offset = QtCore.QPoint()
        self.m_tilesRect = QtCore.QRect()
        self.m_tilePixmaps = {}

    def invalidate(self, emitSignal=True):
        if self.width <= 0 or self.height <= 0:
            return

        ct = tileForCoordinate(self.latitude, self.longitude, self.zoom)
        tx = ct.x()
        ty = ct.y()

        # top left corner of the center tile
        xp = int(self.width / 2 - (tx - math.floor(tx)) * tdim)
        yp = int(self.height / 2 - (ty - math.floor(ty)) * tdim)

        # first tile vertical and horizontal
        xa = (xp + tdim -1) / tdim
        ya = (yp + tdim -1) / tdim
        xs = tx - xa
        ys = ty - ya

        # offset for top-left tile
        self.m_offset = QtCore.QPoint(xp - xa * tdim, yp - ya * tdim)

        # last tile vertical and horizontal
        xe = tx + (self.width - xp -1) / tdim
        ye = ty + (self.height - yp -1) / tdim

        # build a rect
        self.m_tilesRect = QtCore.QRect(xs, ys, xe - xs + 1, ye - ys + 1)

        if self.m_url.isEmpty():
            self.download()

        if emitSignal:
            self.updated.emit(QtCore.QRect(0, 0, self.width, self.height))

    def render(self, painter, rect):
        for x in xrange(self.m_tilesRect.width()+1):
            for y in xrange(self.m_tilesRect.height()+1):
                tp = QtCore.QPoint(x + self.m_tilesRect.left(), y + self.m_tilesRect.top())
                box = self.tileRect(tp)
                if rect.intersects(box):
                    if qHash(tp) in self.m_tilePixmaps:
                        painter.drawPixmap(box, self.m_tilePixmaps[qHash(tp)])
                    else:
                        painter.drawPixmap(box, self.m_emptyTile)

    def pan(self, delta):
        dx = QtCore.QPointF(delta) / tdim
        center = tileForCoordinate(self.latitude, self.longitude, self.zoom) - dx
        self.latitude = latitudeFromTile(center.y(), self.zoom)
        self.longitude = longitudeFromTile(center.x(), self.zoom)
        self.invalidate()
        SetMap(self.zoom,self.latitude,self.longitude)
 
    def zoomTo(self, zoomlevel):
        self.zoom = zoomlevel
        self.invalidate(False)
        SetMap(self.zoom,self.latitude,self.longitude)
 
    def zoomIn(self):
        if self.zoom < MAX_ZOOM:
            self.zoomTo(self.zoom+1)
        SetMap(self.zoom,self.latitude,self.longitude)

        
    def zoomOut(self):
        if self.zoom > MIN_ZOOM:
            self.zoomTo(self.zoom-1)
        SetMap(self.zoom,self.latitude,self.longitude)

        
    def handleNetworkData(self, reply):
        img = QtGui.QImage()
        tp = reply.request().attribute(QtNetwork.QNetworkRequest.User)
        url = reply.url()
 
        if not reply.error():
            if not img.load(reply, ""):
                img = QtGui.QImage()
        reply.deleteLater()
        if img.isNull():
            self.m_tilePixmaps[qHash(tp)] = self.m_emptyTile
        else:
            self.m_tilePixmaps[qHash(tp)] = QtGui.QPixmap.fromImage(img)
        self.updated.emit(self.tileRect(tp))

        self.download()

    def download(self):
        try:
            for x in xrange(self.m_tilesRect.width()+1):
                for y in xrange(self.m_tilesRect.height()+1):
                    tp = self.m_tilesRect.topLeft() + QtCore.QPoint(x, y)
                    if not qHash(tp) in self.m_tilePixmaps:
                        raise StopIteration()

            self.m_url = QtCore.QUrl()
            bound = self.m_tilesRect.adjusted(-2, -2, 2, 2)
            for hash in self.m_tilePixmaps.keys():
                if not bound.contains(QtCore.QPoint(hash[0],hash[1])):
                    del self.m_tilePixmaps[hash]

        except StopIteration:
            self.m_url = QtCore.QUrl(self.path.format(self.zoom, tp.x(),tp.y()))
            request = QtNetwork.QNetworkRequest()
            request.setUrl(self.m_url)
            request.setAttribute(QtNetwork.QNetworkRequest.User,tp)
            self.m_manager.get(request)

    def tileRect(self, tp):
        t = tp - self.m_tilesRect.topLeft()
        x = t.x() * tdim + self.m_offset.x()
        y = t.y() * tdim + self.m_offset.y()
        return QtCore.QRect(x, y, tdim, tdim)


class LightMaps(QtGui.QWidget):
    def __init__(self, parent=None, NormalUrl=None,GlassUrl=None,pressed=False, snapped=False, zoomed=False, invert=False,width=None, height=None, zoom=None, latitude=None, longitude=None):
        QtGui.QWidget.__init__(self)

        self.pressed = pressed
        self.snapped = snapped
        self.zoomed = zoomed
        self.invert = invert

        self.pressPos = QtCore.QPoint()
        self.dragPos = QtCore.QPoint()

        self.zoomPixmap = QtGui.QPixmap()
        self.maskPixmap = QtGui.QPixmap()

        self.tapTimer = QtCore.QBasicTimer()
 
        self.m_normalMap = SlippyMap(self,Url=NormalUrl,width=width, height=height, zoom=zoom, latitude=latitude, longitude=longitude)
        self.m_largeMap = SlippyMap(self,Url=GlassUrl,width=width, height=height, zoom=zoom, latitude=latitude, longitude=longitude)
        self.m_normalMap.updated.connect(self.updateMap)
        self.m_largeMap.updated.connect(self.update)

    def setCenter(self, lat, lng):
        self.m_normalMap.latitude = lat
        self.m_normalMap.longitude = lng
        self.m_normalMap.invalidate()
        self.m_largeMap.invalidate()
 
    def updateMap(self, rect):
        self.update(rect)
 
    def activateZoom(self):
        if self.m_normalMap.zoom < MAX_ZOOM:
            self.zoomed = True
            self.tapTimer.stop()
            self.m_largeMap.zoom = self.m_normalMap.zoom + 1
            self.m_largeMap.width = self.m_normalMap.width * 2
            self.m_largeMap.height = self.m_normalMap.height * 2
            self.m_largeMap.latitude = self.m_normalMap.latitude
            self.m_largeMap.longitude = self.m_normalMap.longitude
            self.m_largeMap.invalidate()
            self.update()

    def resizeEvent(self, event):
        self.m_normalMap.width = self.width()
        self.m_normalMap.height = self.height()
        self.m_normalMap.invalidate()
        self.m_largeMap.width = self.m_normalMap.width * 2
        self.m_largeMap.height = self.m_normalMap.height * 2
        self.m_largeMap.invalidate()

    def paintEvent(self, event):
        p = QtGui.QPainter()
        p.begin(self)
        self.m_normalMap.render(p, event.rect())
        p.setPen(QtCore.Qt.black)
        p.end()

        if self.zoomed:
            dim = min((self.width(), self.height()))
            magnifierSize = min((MAX_MAGNIFIER, dim * 2 / 3))
            radius = magnifierSize / 2
            ring = radius - 15
            box = QtCore.QSize(magnifierSize, magnifierSize)

            # reupdate our mask
            if self.maskPixmap.size() != box:
                self.maskPixmap = QtGui.QPixmap(box)
                self.maskPixmap.fill(QtCore.Qt.transparent)

                g = QtGui.QRadialGradient()
                g.setCenter(radius, radius)
                g.setFocalPoint(radius, radius)
                g.setRadius(radius)
                g.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
                g.setColorAt(0.5, QtGui.QColor(128, 128, 128, 255))

                mask = QtGui.QPainter(self.maskPixmap)
                mask.setRenderHint(QtGui.QPainter.Antialiasing)
                mask.setCompositionMode(QtGui.QPainter.CompositionMode_Source)
                mask.setBrush(g)
                mask.setPen(QtCore.Qt.NoPen)
                mask.drawRect(self.maskPixmap.rect())
                mask.setBrush(QtGui.QColor(QtCore.Qt.transparent))
                mask.drawEllipse(g.center(), ring, ring)
                mask.end()

            center = self.dragPos - QtCore.QPoint(0, radius)
            center = center + QtCore.QPoint(0, radius / 2)
            corner = center - QtCore.QPoint(radius, radius)

            xy = center * 2 - QtCore.QPoint(radius, radius)

            # set the dimension to the magnified portion only
            if self.zoomPixmap.size() != box:
                self.zoomPixmap = QtGui.QPixmap(box)
                self.zoomPixmap.fill(QtCore.Qt.lightGray)
            p = QtGui.QPainter(self.zoomPixmap)
            p.translate(-xy)
            self.m_largeMap.render(p, QtCore.QRect(xy, box))
            p.end()

            clipPath = QtGui.QPainterPath()
            clipPath.addEllipse(QtCore.QPointF(center), ring, ring)

            p = QtGui.QPainter(self)
            p.setRenderHint(QtGui.QPainter.Antialiasing)
            p.setClipPath(clipPath)
            p.drawPixmap(corner, self.zoomPixmap)
            p.setClipping(False)
            p.drawPixmap(corner, self.maskPixmap)
            p.setPen(QtCore.Qt.gray)
            p.drawPath(clipPath)

        if self.invert:
            p = QtGui.QPainter(self)
            p.setCompositionMode(QtGui.QPainter.CompositionMode_Difference)
            p.fillRect(event.rect(), QtCore.Qt.white)
            p.end()

    def timerEvent(self, event):
        if not self.zoomed:
            self.activateZoom()
        self.update()

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.pressed = self.snapped = True;
            self.pressPos = self.dragPos = event.pos()
            self.tapTimer.stop()
            self.tapTimer.start(HOLD_TIME, self)

    def mouseMoveEvent(self, event):
        if event.buttons():
            if not self.zoomed:
                if not self.pressed or not self.snapped:
                    delta = event.pos() - self.pressPos
                    self.pressPos = event.pos()
                    self.m_normalMap.pan(delta)
                else:
                    threshold = 10
                    delta = event.pos() - self.pressPos
                    if self.snapped:
                        self.snapped &= delta.x() < threshold
                        self.snapped &= delta.y() < threshold
                        self.snapped &= delta.x() > -threshold
                        self.snapped &= delta.y() > -threshold
                    if not self.snapped:
                        self.tapTimer.stop()
            else:
                self.dragPos = event.pos()
                self.update()

    def mouseReleaseEvent(self, event):
        self.zoomed = False
        self.update()

    def keyPressEvent(self, event):
        if not self.zoomed:
            if event.key() == QtCore.Qt.Key_Left:
                self.m_normalMap.pan(QtCore.QPoint(20, 0))
            elif event.key() == QtCore.Qt.Key_Right:
                self.m_normalMap.pan(QtCore.QPoint(-20, 0))
            elif event.key() == QtCore.Qt.Key_Up:
                self.m_normalMap.pan(QtCore.QPoint(0, 20))
            elif event.key() == QtCore.Qt.Key_Down:
                self.m_normalMap.pan(QtCore.QPoint(0, -20))
            elif event.key() == QtCore.Qt.Key_Z or event.key() == QtCore.Qt.Key_Select:
                self.dragPos = QtCore.QPoint(self.width() / 2, self.height() / 2)
                self.activateZoom()
            elif event.key() == QtCore.Qt.Key_Plus:
                self.m_normalMap.zoomIn()
            elif event.key() == QtCore.Qt.Key_Minus:
                self.m_normalMap.zoomOut()
        else:
            if event.key() == QtCore.Qt.Key_Z or event.key() == QtCore.Qt.Key_Select:
                self.zoomed = False
                self.update()
            else:
                delta = QtCore.QPoint(0, 0)
                if event.key() == QtCore.Qt.Key_Left:
                    delta = QtCore.QPoint(-15, 0)
                elif event.key() == QtCore.Qt.Key_Right:
                    delta = QtCore.QPoint(15, 0)
                elif event.key() == QtCore.Qt.Key_Up:
                    delta = QtCore.QPoint(0, -15)
                elif event.key() == QtCore.Qt.Key_Down:
                    delta = QtCore.QPoint(0, 15)
                if delta != QtCore.QPoint(0, 0):
                    self.dragPos += delta
                    self.update()

    def wheelEvent(self, event):
        if self.zoomed:
            self.zoomed = False
        if event.delta() > 0:
            self.m_normalMap.zoomIn()
        else:
            self.m_normalMap.zoomOut() 