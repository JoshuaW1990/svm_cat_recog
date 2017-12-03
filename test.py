import cv2 as cv

img = cv.imread('./cat/images (1).jpg')

cv.namedWindow("Image")

cv.imshow("Image", img)

cv.waitKey(0)

cv.destroyAllWindows()
