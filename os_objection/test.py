import numpy as np
import cv2 as cv
src = np.array([[0, 255, 255, 0],
                [255, 0, 0, 255],
                [255, 255, 0, 255],
                [255, 0, 0, 255]])
mask_1 = np.zeros_like(src)
mask_1[1:4, 1:3] = src[1:4, 1:3]



#ans = cv.bitwise_xor(mask_1, src)

print(src)
print(mask_1)
#print(ans)



