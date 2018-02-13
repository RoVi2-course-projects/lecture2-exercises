#!/usr/bin/python3
import cv2
import matplotlib
import numpy as np
from scipy import misc

if __name__ == "__main__":
    # Read the reference image.
    image = misc.imread("./photos/DJI_0295.JPG")
    hsv = matplotlib.colors.rgb_to_hsv(image)
    v_filtered = (hsv[:, :, 2] > 220)
    filtered = v_filtered * s_filtered
    _, contours, hierarchy = cv2.findContours(v_filtered.astype(np.uint8),
                                              cv2.RETR_CCOMP,
                                              cv2.CHAIN_APPROX_SIMPLE)
    good_contours = []
    for index, contour in enumerate(contours):
        if (contour.size > 10 and contour.size < 100):
            good_contours.append(contour)
