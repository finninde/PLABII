from imager import Imager
from imager import ptest2
from os import path

if __name__ == "__main__":
    #testImage = ptest2()    #Nothing's like a trippy Einstein-pic to get things going.

    #Testing contrast method
    testImage = Imager(fid=path.normpath("images/einstein.gif"))
    edgeImage = testImage.FIND_EDGES()
    testImage.morph(im2 = edgeImage).display()
