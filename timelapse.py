import cv2
import numpy as np
import imutils

OUTPUT_IMAGE_WIDTH = 500
# max number of features of interest to consider
MAX_FEATURES = 1000
# percentage of features of interest to keep
# lower percentage reduces noise
KEEP_PERCENT = 0.2
# use ORB algorithm to detect keypoints
ORB = cv2.ORB_create(MAX_FEATURES)
MATCHER = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

def resize(img):
    return imutils.resize(img, width=OUTPUT_IMAGE_WIDTH)

def get_matches(img1, img2):
    # detect keypoints in each image
    # extract local invariant features
    (kp1, desc1) = ORB.detectAndCompute(img1, None)
    (kp2, desc2) = ORB.detectAndCompute(img2, None)

    # match features in both images
    matches = MATCHER.match(desc1, desc2, None)
    # sort to get the best matches
    matches = sorted(matches, key=lambda x:x.distance)
    # only keep the top _% of matches
    keep = int(len(matches) * KEEP_PERCENT)
    matches = matches[:keep]

    # draw matches
    matched_img = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)
    cv2.imshow('Matches', matched_img)

    # allocate memory to store keypoints for top matches
    pts1 = np.zeros((len(matches), 2), dtype="float")
    pts2 = np.zeros((len(matches), 2), dtype="float")

    for (i, m) in enumerate(matches):
        # keypoint in img1
        pts1[i] = kp1[m.queryIdx].pt
        # keypoint in img2
        pts2[i] = kp2[m.trainIdx].pt

	# compute the homography matrix between the two sets of matched points
    (H, mask) = cv2.findHomography(pts2, pts1, method=cv2.RANSAC)
	# use the homography matrix to align the images
    (h, w) = img1.shape[:2]
    aligned_img = cv2.warpPerspective(img2, H, (w, h))
    return aligned_img


if __name__=='__main__':
    img1 = resize(cv2.imread('photos/1.jpg', 0))
    img2 = resize(cv2.imread('photos/2.jpg', 0))

    aligned = get_matches(img1, img2)

    cv2.imshow('img 1', img1)
    cv2.imshow('img 2', img2)
    cv2.imshow('aligned img 2', aligned)

    cv2.waitKey(0)
    cv2.destroyAllWindows()