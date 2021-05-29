import numpy as np
import cv2 as cv
import sys

class Sketcher:
    def __init__(self,windowname,dests,colors_func):
        self.prev__pt=None
        self.windowname=windowname
        self.dests=dests
        self.colors_func=colors_func
        self.dirty= False
        self.show()
        cv.setMouseCallback(self.windowname,self.on_Mouse)




    def show(self):
        cv.imshow(self.windowname,self.dests[0])
        cv.imshow(self.windowname+"Masks",self.dests[1])


    def on_Mouse(self, event, x, y, flags, param):
        pt=( x, y)

        if event == cv.EVENT_LBUTTONDOWN:
            self.prev__pt=pt

        elif event == cv.EVENT_LBUTTONUP:
            self.prev__pt=None


        if self.prev__pt and flags & cv.EVENT_FLAG_LBUTTON:
            for dst,color in zip(self.dests,self.colors_func()):
                cv.line(dst,self.prev__pt,pt,color,4)
                self.dirty=True
                self.prev__pt=pt
                self.show()





def main():
    print ("Inpainting Python ")
    print ("Keys: ")
    print("t- inpainting using Fast Marching method")
    print ("n- Inpainting using modified Convolution technique")
    print ("r-reset the mask")
    print ("ESC-exit ")

    img=cv.imread("image123.jfif",cv.IMREAD_COLOR)
    if img is None:
        print ("Failed to import the Image".format(img))
        return

    img_mask=img.copy()

    inpaintMask=np.zeros(img.shape[:2],np.uint8)

    sketch =Sketcher('image',[img_mask,inpaintMask],lambda : ((255,255,255,),255))

    while True:
        ch=cv.waitKey(0)

        if ch==27:
            break
        if ch==ord('t'):
            res=cv.inpaint(src=img_mask,inpaintMask=inpaintMask,inpaintRadius=4,flags=cv.INPAINT_TELEA)
            cv.imshow("Inpaint using Fast March Methodology", res)

        if ch==ord('n'):
            res=cv.inpaint(src=img_mask,inpaintMask=inpaintMask,inpaintRadius=4,flags=cv.INPAINT_NS)
            cv.imshow("Inpaint using NS segmentation", res)

        if ch==ord('r'):
            img_mask[ : ]=img
            inpaintMask[ : ]=0
            sketch.show()

    print("Process Complete")





if __name__ == '__main__':
    main()
    cv.destroyAllWindows()






