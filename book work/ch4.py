import argparse
import cv2

ap = argparse.ArgumentParser()
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
(b,g,r) = image[0, 0]
print r,b,g

cv2.imshow("f", image[0:-1, 0:100])
image[0:100, 0:100] = (0, 0, 0)
cv2.imshow("mod", image)

cv2.waitKey(0)