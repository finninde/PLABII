#TODO: Import only functions needed
from PIL import *

Class Imager():
    def __init__(self, fid = False, image = False, width = 100, height = 100, background = 'black', mode = 'RGB'):
        self.fid = fid
        self.image = image
        self.xmax = width
        self.ymax = height
        self.mode = mode
        #self.init_image(background = background)


