#!/usr/bin/python3
import numpy as np
from scipy import misc
import cv2
import matplotlib.pyplot as plt

def plot_figure(original_image, image_name):
    hsv_image = cv2.cvtColor(original_image,cv2.COLOR_BGR2HSV)
    plt.figure(image_name)
    plot_original = plt.subplot(2, 2, 1)
    plot_original.imshow(original_image)
    for idx in range(0, 3):
        if(idx == 0): # range for blue value
            lower_blue = np.array([110, 50, 50])
            upper_blue = np.array([130, 255, 255])
            mask0 = cv2.inRange(hsv_image, lower_blue, upper_blue)
        elif(idx == 1): # ranges for red value
            lower_red = np.array([0, 50, 50])
            upper_red = np.array([10, 255, 255])
            mask0 = cv2.inRange(hsv_image, lower_red, upper_red)
            lower_red = np.array([170, 50, 50])
            upper_red = np.array([180, 255, 255])
            mask1 = cv2.inRange(hsv_image, lower_red, upper_red)
            mask0 = mask0 + mask1
        elif(idx == 2): # range for green value
            lower_green = np.array([65, 60, 60])
            upper_green = np.array([80, 255, 255])
            mask0 = cv2.inRange(hsv_image, lower_green, upper_green)

        hsv_out = hsv_image.copy()
        hsv_out[np.where(mask0==0)] =0
        #hsv_image[np.where(mask0==0)] = 0
        plot = plt.subplot(2, 2, idx+2)
        plt.imshow(hsv_out, 'gray')

if __name__ == "__main__":

    image_underexposed = misc.imread("../photos/DJI_0034.JPG")
    image_overexposed = misc.imread("../photos/DJI_0037.JPG")
    image_mediumexposed = misc.imread("../photos/DJI_0033.JPG")

    plot_figure(image_underexposed, "Underexposed")
    plot_figure(image_overexposed, "Overexposed")
    plot_figure(image_mediumexposed, "Neutralexposed")
    plt.show()
