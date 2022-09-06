# Image Alignment

This project uses OpenCV to align similar images taken from different perspectives.
The implementation is based on [this tutorial](https://pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/).

Take these two images as inputs

<div>
  <img src="photos/1.jpg" alt="Image 1 of building site" width="500" />
  <img src="photos/2.jpg" alt="Image 2 of building site" width="500" /> 
</div>

Use an ORB algorithm to identify keypoints, which can be matched between the images.

![Matched features](output/1-2-matches.jpg)

Compute the homography matrix between the two sets of matched points and tranform the second image to align it with the first

![Aligned image 2](output/2-aligned.jpg)

By overlaying it onto the original image, we can judge the effectiveness of the operation

![Overlayed images](output/overlay-1-2.jpg)
