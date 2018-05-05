import cv2
import numpy as np
import glob


class PerspectiveTrafo:
    M = []
    
    DEFAULT_SRC = np.float32(
        [[120, 720],
            [550, 470],
            [730, 470],
            [1160, 720]])

    DEFAULT_DST = np.float32(
        [[200,720],
            [200,0],
            [1080,0],
            [1080,720]])
            
    def __init__(self, src=DEFAULT_SRC, dst=DEFAULT_DST, img_size=(1300,1300)):
        self.M = cv2.getPerspectiveTransform(src,dst)
        self.Minv = cv2.getPerspectiveTransform(dst,src)
        self.img_size = img_size

    def warp(self,img) :
        return cv2.warpPerspective(img, self.M, self.img_size, flags=cv2.INTER_LINEAR)

    def warpInv(self,img, img_size) :
        return cv2.warpPerspective(img, self.Minv, img_size, flags=cv2.INTER_LINEAR)
