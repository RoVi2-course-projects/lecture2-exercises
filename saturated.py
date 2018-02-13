#!/usr/bin/python3
import numpy as np
from scipy import misc

if __name__ == "__main__":
    # Begin a loop going over all of the images in the photos folder.
    for idx in range(32, 52):
        image = misc.imread("../photos/DJI_00{img_idx}.JPG".format(img_idx=idx))
        # Count number of saturated pixels for every RGB component.
        red_sat = np.count_nonzero(image[:, :, 0] == 255)
        green_sat = np.count_nonzero(image[:, :, 1] == 255)
        blue_sat = np.count_nonzero(image[:, :, 2] == 255)
        all_sat = np.count_nonzero((image[:, :, 0] == 255)
                * (image[:, :, 1] == 255) * (image[:, :, 2] == 255))
        any_sat = np.count_nonzero((image[:, :, 0] == 255)
                + (image[:, :, 1] == 255) + (image[:, :, 2] == 255))
        # Initialize array if it is the first iteration
        if (idx == 32):
            saturated = np.array([red_sat, green_sat, blue_sat, all_sat,
                                  any_sat])
        # Append the saturated values to the result matrix.
        else:
            saturated = np.vstack((saturated,
                    np.array([red_sat, green_sat, blue_sat, all_sat, any_sat])))
    # Save results to text file.
    out_file = "results.txt"
    header = "RED\tGREEN\tBLUE\tALL\tANY"
    np.savetxt(out_file, saturated, fmt="%i", delimiter='\t', header=header)
