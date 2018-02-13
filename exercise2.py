#!/usr/bin/python3
import numpy as np
from scipy import misc
import cv2
import matplotlib.pyplot as plt

def plot_figure(original_image, image_name):
    exposed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    plt.figure(image_name)
    plot_original = plt.subplot(2, 2, 1)
    plot_original.imshow(original_image)
    for idx in range(0, 3):
        color_chan = original_image[:, :, idx]
        segmented_image = color_chan[:, :] > 0.7*255
        plot = plt.subplot(2, 2, idx+2)
        plt.imshow(segmented_image, 'gray')

if __name__ == "__main__":

    image_underexposed = misc.imread("../photos/DJI_0034.JPG")
    image_overexposed = misc.imread("../photos/DJI_0037.JPG")
    image_mediumexposed = misc.imread("../photos/DJI_0033.JPG")

    plot_figure(image_underexposed, "Underexposed")
    plot_figure(image_overexposed, "Overexposed")
    plot_figure(image_mediumexposed, "Neutralexposed")
    plt.show()
