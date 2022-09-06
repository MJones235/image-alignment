import cv2
import numpy as np
import imutils

NUM_INPUT_IMAGES = 12
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

def get_matches(img1, img2, img2_colour):
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
    # matched_img = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)
    # cv2.imshow('Matches', matched_img)
    # cv2.imwrite('output/1-2-matches.jpg', matched_img)

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
    aligned_img = cv2.warpPerspective(img2_colour, H, (w, h))
    return aligned_img

def overlay_images(img1, img2, i):
    overlay = img1.copy()
    output = img2.copy()
    cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)
    cv2.imshow(f'Overlayed {i}', output)

if __name__=='__main__':
    processed_images = [resize(cv2.imread('photos/1.jpg'))]

    for i in range(1, NUM_INPUT_IMAGES):
        img1 = resize(cv2.imread(f'photos/{i}.jpg'))
        img2 = resize(cv2.imread(f'photos/{i + 1}.jpg'))

        img1_grey = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2_grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        aligned = get_matches(img1_grey, img2_grey, img2)

        # overlay_images(img1, aligned, i)

        processed_images.append(aligned)

    # display processed images in sequence
    for image in processed_images:
        cv2.imshow('display', image)
        cv2.waitKey(1000)

    cv2.destroyAllWindows()