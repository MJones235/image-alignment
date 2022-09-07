import cv2
import numpy as np

# max number of features of interest to consider
MAX_FEATURES = 5000
# percentage of features of interest to keep
# lower percentage reduces noise
KEEP_PERCENT = 0.03
# use ORB algorithm to detect keypoints
ORB = cv2.ORB_create(MAX_FEATURES)
MATCHER = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

def get_aligned_image(img1, img2):
    img1_grey = get_greyscale_img(img1)
    img2_grey = get_greyscale_img(img2)
    img2_aligned = get_aligned_img(img1_grey, img2_grey, img2)
    return img2_aligned

def get_greyscale_img(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def get_aligned_img(template, img, img_colour):
    pts1, pts2 = get_keypoints(template, img)
	# compute the homography matrix between the two sets of matched points
    (H, mask) = cv2.findHomography(pts2, pts1, method=cv2.RANSAC)
	# use the homography matrix to align the images
    (h, w) = template.shape[:2]
    aligned_img = cv2.warpPerspective(img_colour, H, (w, h))
    return aligned_img

def get_keypoints(template, img):
    # detect keypoints in each image
    # extract local invariant features
    (kp1, desc1) = ORB.detectAndCompute(template, None)
    (kp2, desc2) = ORB.detectAndCompute(img, None)

    # match features in both images
    matches = MATCHER.match(desc1, desc2, None)
    # sort to get the best matches
    matches = sorted(matches, key=lambda x:x.distance)
    # only keep the top KEEP_PERCENT% of matches
    keep = int(len(matches) * KEEP_PERCENT)
    matches = matches[:keep]
    # allocate memory to store keypoints for top matches
    pts1 = np.zeros((len(matches), 2), dtype="float")
    pts2 = np.zeros((len(matches), 2), dtype="float")

    for (i, m) in enumerate(matches):
        # keypoint in template
        pts1[i] = kp1[m.queryIdx].pt
        # keypoint in img
        pts2[i] = kp2[m.trainIdx].pt

    return pts1, pts2