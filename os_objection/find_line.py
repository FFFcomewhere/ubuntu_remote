import cv2 as cv
import numpy as np

path = "E://file//projection//OS_objection//"


black_bgr_lower_bound = np.array([40, 40, 40])
black_bgr_upper_bound = np.array([70, 60, 60])

black_hsv_lower_bound = np.array([0, 0, 0])
black_hsv_upper_bound = np.array([180, 255, 46])

def pretreatment(img):
    """对图片进行预处理 包括高斯滤波 过滤黑色外的颜色"""
    #高斯模糊
    gauss_img = cv.GaussianBlur(img, (5, 5), 0, 0)
    #过滤黑色外的颜色
    mask_black = cv.inRange(gauss_img, black_bgr_lower_bound, black_bgr_upper_bound)

    return mask_black

def find_line(img):
    #canny 边缘检测
    lthrehlod = 50
    hthrehlod = 150
    edges_img = cv.Canny(img, lthrehlod, hthrehlod)
    edges_img = np.resize(edges_img, img.shape)
    print(edges_img.shape)

    #ROI划定区间,并将非此区间变成黑色

    regin = np.zeros_like(edges_img)
    regin[0:edges_img.shape[0], 0:edges_img.shape[1]] = edges_img[0:edges_img.shape[0], 0:edges_img.shape[1]]

    line_img = regin

    # 利用霍夫变换原理找出上图中的像素点组成的直线，然后画出来
    rho = 1
    theta = np.pi / 180
    threhold = 15
    minlength = 40
    maxlengthgap = 20
    lines = cv.HoughLinesP(line_img, rho, theta, threhold, np.array([]), minlength, maxlengthgap)
    # 画线
    linecolor = [0, 255, 255]
    linewidth = 4
    src5 = cv.cvtColor(line_img, cv.COLOR_GRAY2BGR)  # 转化为三通道的图像
    lefts = []
    rights = []
    cv.imshow("scr5", src5)

    for line in lines:
        for x1, y1, x2, y2 in line:
            # cv.line(src5,(x1,y1),(x2,y2),linecolor,linewidth)
            # 分左右车道
            k = (y2 - y1) / (x2 - x1)
            if k < 0:
                lefts.append(line)
            else:
                rights.append(line)


    return line_img

if __name__ == '__main__':

    #cap = cv.VideoCapture(path+"小车行车记录仪.avi")
    cap = cv.VideoCapture(path+"真实环境行车记录仪.avi")


    while((cap.isOpened())):
        ret, frame = cap.read()
        #对于道路线检测 只需截取图像的下部分1/3画面
        frame = frame[int(frame.shape[0]*2/3):frame.shape[0], :, :]

        pret = pretreatment(frame)
        line_img = find_line(pret)

        cv.imshow('frame', frame)
        cv.imshow('pret', pret)
        cv.imshow('edges_img', line_img)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break


    cap.release()
    cv.destroyWindow()
