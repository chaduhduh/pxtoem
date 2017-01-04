"""  PxToEM Sublime Plugin Class  """

import sublime_plugin
import sys

if sys.version_info[0] > 2:    
    from PxToEm.pxtoem import pxtoem  # sublime 3
else:
    from pxtoem import pxtoem  # sublime 2

    
class PxToEmCommand(sublime_plugin.TextCommand):
    PXEM = pxtoem.pxtoem()
    _basePixel = 16

    def clearClipboard(self):
        sublime.set_clipboard(' ')
    
    def copyText(self, textToCopy):
        sublime.set_clipboard(textToCopy)
        
    def getSelection(self, region):
        return self.view.substr(region)

    def convertPx(self, value):
        return self.PXEM.convertPx(value, self._basePixel)

    def getView(self):
        return self.view

    def run(self, edit):
        view = self.getView()
        for region in view.sel():
            if region.empty():
                return
            s = self.getSelection(region)
            s = self.convertPx(s)
            if not s:
                return
            self.getView().replace(edit, region, s)
