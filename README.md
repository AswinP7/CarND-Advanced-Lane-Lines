[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

# The Project
---
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
* [camera_calibration.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/camera_calibration.py) code for calibration of the camera
* [threshold.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/threshold.py)
* [pipeline.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/pipeline.py)


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
The pipeline is implemented in [pipeline.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/pipeline.py)

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

The code for my perspective transform includes a function called `warper()`, which appears in lines 1 through 8 in the file `example.py` (output_images/examples/example.py) (or, for example, in the 3rd code cell of the IPython notebook).  The `warper()` function takes as inputs an image (`img`), as well as source (`src`) and destination (`dst`) points.  I chose the hardcode the source and destination points in the following manner:

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

Then I did some other stuff and fit my lane lines with a 2nd order polynomial kinda like this:

![alt text][image5]

## Calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did this in functions curvature and lanepos in [curvature.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/curvature.py)

## Example image of result plotted back down onto the road such that the lane area is identified clearly.

I implemented this step in lines 40 to 48 in my code in [pipeline.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/pipeline.py) and in [lanefinder.py](https://github.com/MarkBroerkens/CarND-Advanced-Lane-Lines/blob/master/lanefinder.py)  in the function `draw()`.  Here is an example of my result on a test image:

![alt text][image6]

---

# Pipeline (video)

## Final video output

* Here's a [link to my project video result](./output_images/L_project_video.mp4)
* Here's a [link to my challenge video result](./output_images/L_challenge_video.mp4)
* Here's a [link to my harder challenge video result](./output_images/L_harder_challenge_video.mp4)

---

# Discussion

## 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  



