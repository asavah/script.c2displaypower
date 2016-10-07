import os, sys, subprocess
import xbmc, xbmcgui, xbmcaddon

__addon__    = sys.modules[ '__main__' ].__addon__
__addonid__  = sys.modules[ '__main__' ].__addonid__
__cwd__      = sys.modules[ '__main__' ].__cwd__
__skindir__  = xbmc.getSkinDir().decode('utf-8')
__skinhome__ = xbmc.translatePath( os.path.join( 'special://home/addons/', __skindir__, 'addon.xml' ).encode('utf-8') ).decode('utf-8')
__skinxbmc__ = xbmc.translatePath( os.path.join( 'special://xbmc/addons/', __skindir__, 'addon.xml' ).encode('utf-8') ).decode('utf-8')

class Screensaver(xbmcgui.WindowXMLDialog):
    def __init__( self, *args, **kwargs ):
        pass

    def onInit(self):
        self._is_powered = True
        self.mode = "fb0"
        if self.mode == "fb0":
            self.knob = "/sys/class/graphics/fb0/blank"
            self.on = "0"
            self.off = "4"
        else:
            self.knob = "/sys/class/amhdmitx/amhdmitx0/phy"
            self.on = "1"
            self.off = "0"

        self.Monitor = MyMonitor(action = self._power_on)
        self._power_toggle()

    def _power_on(self):
        self._power_toggle()
        self.close()

    def _power_toggle(self):
        if self._is_powered:
            knob_val = self.off
        else:
            knob_val = self.on
        try:
            with open(self.knob,"w") as fd:
                fd.write(knob_val)
        except Exception, e:
            xbmc.log(msg="%s: Exception while writing to %s %s" % ( __addonid__ , self.knob, str(e)), level=xbmc.LOGERROR)
        else:
            self._is_powered = not self._is_powered

class MyMonitor(xbmc.Monitor):
    def __init__( self, *args, **kwargs ):
        self.action = kwargs['action']

    def onScreensaverDeactivated(self):
        self.action()
