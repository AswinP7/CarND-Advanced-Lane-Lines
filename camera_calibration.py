# thanks to https://github.com/udacity/CarND-Camera-Calibration.git

import numpy as np
import cv2
import glob
import image_util

CHESS_BOARD_SHAPE = (9,6)

objp = np.zeros((CHESS_BOARD_SHAPE[0]*CHESS_BOARD_SHAPE[1],3), np.float32)
objp[:,:2] = np.mgrid[0:CHESS_BOARD_SHAPE[0], 0:CHESS_BOARD_SHAPE[1]].T.reshape(-1,2)


def calibrateCameraFromDir(path):
    objpoints = [] # 3d points in real world space
    imgpoints = [] # 2d points in image plane.

    imgs = image_util.loadImagesRGB(path)
    for img in imgs:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Find the chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, CHESS_BOARD_SHAPE, None)

        # If found, add object points, image points
        if ret == True:
            objpoints.append(objp)
            imgpoints.append(corners)

    # Do camera calibration given object points and image points
    img_size = (img.shape[1], img.shape[0])
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size,None,None)
    return ret, mtx, dist, rvecs, tvecs



