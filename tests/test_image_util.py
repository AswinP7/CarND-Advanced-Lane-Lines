import sys
import os
import unittest
import cv2

sys.path.append("..")
import image_util as uut

CAMERA_CAL="../camera_cal"
TEST_OUT_DIR="test_image_util_out"

class ImageUtilTest(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(TEST_OUT_DIR):
            os.makedirs(TEST_OUT_DIR)
    
    def tearDown(self):
        return

    def test_01_load(self):
        imgs = uut.loadImagesRGB(CAMERA_CAL)
        self.assertEqual(20,len(imgs))
        for img in imgs:
            print("1" + str(img.shape))

    def test_02_loadAndSave(self):
        imgs = uut.loadImagesRGB(CAMERA_CAL)
        for i,img in enumerate(imgs):
            print("2" + str(img.shape))
            uut.saveImage(img, TEST_OUT_DIR+"/out"+str(i)+".png")

    def test_03_createBeforeAfterImages(self):
        imgs = uut.loadImagesRGB(CAMERA_CAL)
        for i,img in enumerate(imgs):
            uut.saveBeforeAfterImages(img, "before", img, "after", TEST_OUT_DIR+"/before_after_"+str(i)+".png")

if __name__ == '__main__':
    unittest.main()
