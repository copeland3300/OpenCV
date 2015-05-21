import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'path to image')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print image.shape
cv2.imshow("image", image)
cv2.waitKey(0)