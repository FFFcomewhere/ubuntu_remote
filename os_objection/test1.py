import cv2

path = "E://file//projection//OS_objection//"


def cv_show(img,  name):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()




img = cv2.imread(path+'green_arrow.png', cv2.IMREAD_GRAYSCALE)
cv_show(img, 'img')

# 分别计算x和y
img = cv2.imread(path+'green_arrow.png', cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv_show(sobelxy, 'sobelxy')


