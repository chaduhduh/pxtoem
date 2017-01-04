"""  PxToEM Python Class  """


class pxtoem(object):

    def convertPx(self, value, basePixel):
        type = self.getType(value)
        return self.getConversion(type, value, basePixel);

    def getConversion(self, type, value, basePixel):
        if type is "px":
            return str(self.pxEm(basePixel, value))
        if type is "em":
            return str(self.emPx(basePixel, value))

    def pxEm(self, base, value):
        # Formula: size in pixels / parent size in pixels
        value = value[0:(len(value)-2)]   # assuming px at end
        return str(float(value)/float(base)) + "rem"

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
