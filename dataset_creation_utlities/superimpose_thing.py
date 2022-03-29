import numpy as np
import cv2
from math import floor

def superimpose_thing(image_size, annotations):
    height, width = image_size

    # create a single channel black image
    superimposed_image = np.zeros((height, width))

    polygons_list = []
    # Add the polygon segmentation
    for segmentation_points in annotation['segmentation']:
        segmentation_points = np.multiply(segmentation_points, 1).astype(int)
        polygons_list.append(segmentation_points)

    # convert segmentation points to contour
    for x in polygons_list:
        end = []
        if len(x) % 2 != 0:
            print(x)
        for l in range(0, len(x), 2):
            coords = [floor(x[l]), floor(x[l + 1])]
            end.append(coords)
        contours = np.array(end)
        if end == []:
            continue

        # plot and fill the contour
        cv2.fillPoly(superimposed_image, pts=[contours], color=(1, 1, 1))
  
    return superimposed_image
