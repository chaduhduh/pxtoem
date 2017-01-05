"""  PxToEM Sublime Plugin Class  """

import sublime
import sublime_plugin
import sys

if sys.version_info[0] > 2:
    from PxToEm.pxtoem import pxtoem  # sublime 3
else:
    from pxtoem import pxtoem  # sublime 2


class PxToEmCommand(sublime_plugin.TextCommand):

    def init(self):
        self._basePixel = self.getBasePixel()
        self.PXEM = pxtoem.pxtoem({
            'useRem': self.getSettings().get('useRem'),
            'defaultBasePixel' : self.getSettings().get('basePixel')
        })

    def getBasePixel(self):
        return self.getSettings().get('basePixel')

    def getSettings(self):
        if not hasattr(self, '_settings'):
            self._settings = sublime.load_settings(
                                "settings.sublime-settings") or {}
        return self._settings

    def clearClipboard(self):
        sublime.set_clipboard(' ')

    def copyText(self, textToCopy):
        sublime.set_clipboard(textToCopy)

    def getSelection(self, region):
        return self.view.substr(region)

    def convertPx(self, value):
        return self.PXEM.convertPx(value, self.getBasePixel())

    def getView(self):
        return self.view

    def run(self, edit):
        self.init()
        view = self.getView()
        for region in view.sel():
            if region.empty():
                return
            s = self.getSelection(region)
            s = self.convertPx(s)
            if not s:
                return
            self.getView().replace(edit, region, s)
