import sys
import os
import unittest
import cv2

sys.path.append("..")
import image_util
import camera_calibration as uut

CAMERA_CAL_DIR="../camera_cal"
TEST_IMAGES_DIR="../test_images"
TEST_OUT_DIR="camera_calibration_out"

class CameraClibrationTest(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(TEST_OUT_DIR):
            os.makedirs(TEST_OUT_DIR)
    
    def tearDown(self):
        return

    def test_01_calibrateCameraFromDir(self):
        ret, mtx, dist, rvecs, tvecs = uut.cachedCalibrateCameraFromDir(CAMERA_CAL_DIR)
        print(ret)
        print(mtx)
        print(dist)

    def test_02_undistortCalibrationImages(self):
        imgs = image_util.loadImagesRGB(CAMERA_CAL_DIR)
        ret, mtx, dist, rvecs, tvecs = uut.cachedCalibrateCameraFromDir(CAMERA_CAL_DIR)
        for i,img in enumerate(imgs):
            dimg = cv2.undistort(img,mtx,dist)
            image_util.saveBeforeAfterImages(img, "Original", dimg, "Undistorted", TEST_OUT_DIR+"/calibration_"+str(i)+"_undistorted.png")

    def test_03_undistortTestImages(self):
        imgs = image_util.loadImagesRGB(TEST_IMAGES_DIR)
        ret, mtx, dist, rvecs, tvecs = uut.cachedCalibrateCameraFromDir(CAMERA_CAL_DIR)
        for i,img in enumerate(imgs):
            dimg = cv2.undistort(img,mtx,dist)
            image_util.saveBeforeAfterImages(img, "Original", dimg, "Undistorted", TEST_OUT_DIR+"/test_"+str(i)+"_undistorted.png")



if __name__ == '__main__':
    unittest.main()
