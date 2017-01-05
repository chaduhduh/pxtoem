"""  PxToEM Python Class  """


class pxtoem(object):
    def __init__(self, args):
        # settings
        self._useRem = args['useRem'] or False
        self.setDefaultBasePixel(args['defaultBasePixel'])

    def setDefaultBasePixel(self, value):
        self._defaultBasePixel = value or 16

    def getDefaultBasePixel(self):
        return self._defaultBasePixel;

    def convertPx(self, value, basePixel):
        type = self.getType(value)
        if basePixel is None:
            basePixel = self.getDefaultBasePixel()
        return self.getConversion(type, value, basePixel)

    def getConversion(self, type, value, basePixel):
        if type is "px":
            return str(self.pxEm(basePixel, value))
        if type is "em":
            return str(self.emPx(basePixel, value))

    def pxEm(self, base, value):
        # Formula: size in pixels / parent size in pixels
        appendStr = "em"
        if self._useRem:
            appendStr = "rem"
        value = value[0:(len(value)-2)]   # assuming px at end
        return str(float(value)/float(base)) + appendStr

    def emPx(self, base, value):
        # Formula: size in EMs * parent size in pixels
        if 'rem' in value:
            rtnValue = value[0:(len(value)-3)]  # assuming rem at end
        else:
            rtnValue = value[0:(len(value)-2)]  # assuming em at end
        return str(float(rtnValue) * float(base)) + "px"

    def getType(self, value):
        if 'px' in value:
            return 'px'
        if 'em' in value:
            return 'em'
