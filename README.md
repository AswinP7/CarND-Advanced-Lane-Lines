[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

# The Project
The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

# Overview of Files

My project includes the following files:
* [README.md](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/README.md) (writeup report) documentation of the results 
* [pipeline.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/pipeline.py) contains the pipeline for lane line detection
* [camera_calibration.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/camera_calibration.py) code for calibration of the camera
* [undistorter.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/undistorter.py) code for correction of distortion
* [threshold.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/threshold.py) code for calculation of thresholds
* [perspective_trafo.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/threshold.py) code for perspective transformation
* [lanefinder.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/lanefinder.py) code for finding and drawing lane lines
* [curvatuere.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/curvature.py) code for calculation of curvature and the position of the car within the lane lines
* [image_util.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/image_util.py) code for loading and saving images and for calculation of the visalization of original and processed images.
* [project video result](./output_images/L_project_video.mp4)
* [challenge video result](./output_images/L_challenge_video.mp4)
* [lharder challenge video result](./output_images/L_harder_challenge_video.mp4)





[//]: # (Image References)

[image1]: ./output_images/1_undistorted.png "Undistorted"
[image2]: ./output_images/2_undistorted.png "Road Undistorted"
[image3a]: ./output_images/thresholded1.jpg "Thresholded Road Straigt Difficult"
[image3b]: ./output_images/thresholded2.jpg "Thresholded Road Straigt Difficult "
[image3c]: ./output_images/thresholded3.jpg "ThresholdedRoad Curve Right"
[image3d]: ./output_images/thresholded5.jpg "ThresholdedRoad Curve Left"
[image3e]: ./output_images/thresholded7.jpg "ThresholdedRoad Straigt"

[image4a]: ./output_images/warped1.jpg "Warped Road Straigt Difficult"
[image4b]: ./output_images/warped2.jpg "Warped Road Straigt Difficult "
[image4c]: ./output_images/warped3.jpg "Warped Road Curve Right"
[image4d]: ./output_images/warped5.jpg "Warped Road Curve Left"
[image4e]: ./output_images/warped7.jpg "Warped Road Straigt"


[image4]: ./examples/warped_straight_lines.jpg "Warp Example"
[image5]: ./examples/color_fit_lines.jpg "Fit Visual"
[image6]: ./output_images/pipeline5.jpg "Output"
[video1]: ./output_images//L_project_video.mp4 "Video"
[video2]: ./output_images//L_challenge_video.mp4 "Challenge Video"
[video3]: ./output_images//L_harder_challenge_video.mp4 "Harder Challenge Video"


# Camera Calibration
The code for this step is contained in the method `calibrateCameraFromDir` the file called [camera_calibration.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/camera_calibration.py).  

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function.  I applied this distortion correction to the test image using the `cv2.undistort()` function and obtained this result: 

![alt text][image1]

# Pipeline (single images)
The pipeline for single images is implemented in [pipeline.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/pipeline.py)

## Example of a distortion-corrected image.
The following image demonstrates the distortion corextion to a road image:

![alt text][image2]

## Used color transforms, gradients or other methods to create a thresholded binary image. 

I used a combination of color and gradient thresholds to generate a binary image ( [threshold.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/threshold.py) ).  Here's an example of my output for this step. 

![alt text][image3a]
![alt text][image3b]
![alt text][image3c]
![alt text][image3d]
![alt text][image3e]

## Perspective transform

The code for my perspective transform includes a function called `warp()`, which appears in file [perspective_trafo.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/perspective_trafo.py).  The `warp()` function takes as inputs an image (`img`), and runs `cv2.warpPerspective()` using the follwing source (`src`) and destination (`dst`) points.  I chose the hardcode the source and destination points in the following manner:

```python
src = np.float32(
[[(img_size[0] / 2) - 62, img_size[1] / 2 + 100],
[((img_size[0] / 6) - 10), img_size[1]],
[(img_size[0] * 5 / 6) + 60, img_size[1]],
[(img_size[0] / 2 + 62), img_size[1] / 2 + 100]])

dst = np.float32(
[[(img_size[0] / 4), 0],
[(img_size[0] / 4), img_size[1]],
[(img_size[0] * 3 / 4), img_size[1]],
[(img_size[0] * 3 / 4), 0]])
```

This resulted in the following source and destination points:

| Source        | Destination   | 
|:-------------:|:-------------:| 
| 578, 460      | 320, 0        | 
| 203, 720      | 320, 720      |
| 1127, 720    | 960, 720      |
| 702, 460      | 960, 0        |

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image4a]
![alt text][image4b]
![alt text][image4c]
![alt text][image4d]
![alt text][image4e]

## Identifying lane-line pixels and fitting their positions with a polynomial

The detection of lane-lines starts with searching for peaks in the histogramm in the bottom part of the thresholded and warped images. The identified peaks are used as the starting point for following the line using the sliding window approach. ([lanefinder.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/lanefinder.py), function `findLanes1st()`.
After the initial line is detected, we can continue searching for the new location of the lane line starting in the area where the current line was detected.  ([lanefinder.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/lanefinder.py), function `findLanesNext()`

![alt text][image5]

## Calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did this in functions `curvature()` and `lanepos()` in [curvature.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/curvature.py)

## Example image of result plotted back down onto the road such that the lane area is identified clearly.

I implemented this step in lines 40 to 48 in my code in [pipeline.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/pipeline.py) and in [lanefinder.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/lanefinder.py)  in the function `draw()`.  Here is an example of my result on a test image:

![alt text][image6]


# Pipeline (video)
The creation of the final video is implemented in [videoprocess.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/videoprocess.py)

## Final video output

* Here's a [link to my project video result](./output_images/L_project_video.mp4)
* Here's a [link to my challenge video result](./output_images/L_challenge_video.mp4)
* Here's a [link to my harder challenge video result](./output_images/L_harder_challenge_video.mp4)


# Discussion
During the implementation of this project I found it very useful to make use of python unittests in order to test the code and in order to calculate and evaluate differnt parameters, e.g. in the context of thresholding. 
The chosen approach worked pretty well for all three test videos. However, it had some problems in case the surface of the street changes, there is much shadow on the road, lane lines are missing, etc. 

Improvements could be:
* consider provious polynoms that were fitted onto the lane lines in order to smoothen lane line detection
* add sanity checks that kick out values that do nor make sense. In that case the previous polynoms could be reused.
* the values of the curvature and the position of the car are hardly readable since they change so often. Less frequent update of the values and calculation of the average over several frames of the video could help.
* In order to reduce effort for calculation of the thresholds, etc. the images reduced to the area of interest (the street only)
* There might be a better values for min and max thresholds of the threshold calculation. More finetuning might produce even better results. 



