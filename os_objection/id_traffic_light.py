import cv2 as cv
import numpy as np


IMG_SZIE = (40, 40)
img_size_flter = 60

red_hsv_lower_bound = np.array([156, 127, 128])  # 红色阈值下界
red_hsv_upper_bound = np.array([180, 255, 255])  # 红色阈值上界

green_hsv_lower_bound = np.array([35, 43, 46])
green_hsv_upper_bound = np.array([77, 255, 245])

black_hsv_lower_bound = np.array([0, 0, 0])
black_hsv_upper_bound = np.array([180, 255, 46])


path = "E://file//projection//OS_objection//"

cmd = ["stop", "letf", "right", "None"]

def load_img(path):
    img = cv.imread(path)
    return img


def show_img(img, name="img"):
    cv.imshow(name, img)
    cv.waitKey(0)

"""去除图片中的其他颜色"""
def pretreatment(img):
    # 高斯模糊
    src_gauss = cv.GaussianBlur(img, (5, 5), 0)
    #将rgb转化为hsv
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    #过滤绿色和红色以外的颜色
    mask_red = cv.inRange(hsv, red_hsv_lower_bound, red_hsv_upper_bound)
    mask_green = cv.inRange(hsv, green_hsv_lower_bound, green_hsv_upper_bound)

    #比较红色区域和绿色区域面积,确认当前颜色
    length = int(mask_red.shape[0])
    width = int(mask_red.shape[1])
    erea_red = mask_red.sum() / (length*width*255)
    erea_green = mask_green.sum() / (length*width*255)
    if erea_red >= erea_green:
        color = "red"
    else:
        color = "green"

    # #当出现误识别时,红色面积过小,视作没看见红色
    # if erea_red < 0.02:
    #     color = "green"

    #合并红色和绿色图片
    mask = cv.bitwise_xor(mask_red, mask_green)

    #膨胀腐蚀
    kernel = np.ones((15, 15), np.uint8)
    filter_img = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

    cv.imshow("mask_red", mask_red)
    cv.imshow("mask_green", mask_green)

    return filter_img, color


"""使用canny函数进行边缘检测"""
def identify_logo_canny(src, pret):
    # 边缘检测
    edges = cv.Canny(pret, 50, 150)

    contours, hierarchy = cv.findContours(edges.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv.contourArea, reverse=True)[:1]

    data = np.array(contours)
    data.resize((len(contours[0]), 2))

    #对应边框的四个顶点
    x1 = np.min(data[:, 0])
    x2 = np.max(data[:, 0])
    y1 = np.min(data[:, 1])
    y2 = np.max(data[:, 1])

    #面积过小,视作噪点
    if x2-x1 < 40 or y2-y1 < 40:
        return

    cv.rectangle(src, (x1, y1), (x2, y2), (255, 255, 0), 1)
    cv.drawContours(src, contours, -1, (255, 0, 0), 1)


"""使用findContours进行边缘检测"""
def identify_logo_findContours(src, pret):
    font = cv.FONT_HERSHEY_SIMPLEX

    cnts1, hierarchy1 = cv.findContours(pret, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cnts1 = sorted(cnts1, key=cv.contourArea, reverse=True)[:1]

    print(type(cnts1))

    (x, y, w, h) = cv.boundingRect(cnts1[0])  #该函数返回矩阵四个点

    # 面积过小,视作噪点
    if w < img_size_flter or h < img_size_flter:
        return 0, 0, 0, 0

    cv.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 1)  # 将检测到的颜色框起来
    cv.putText(src, color, (x, y - 5), font, 0.7, (0, 0, 255), )


    return x, y, x+w, y+h




def compare(destin, frame):
    #图片为空,返回
    if(destin.shape == (0, 0)):
        return 3

    if color == "red":
        cmd_num = 0
        cv.putText(frame, cmd[cmd_num], (x2, y1 - 5), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
        return cmd_num

    destin = cv.resize(destin, IMG_SZIE)
    y_sum = 0
    y_num = 0

    for i in range(destin.shape[0]):
        for j in range(destin.shape[1]):
            if destin[i][j] == 255:
                y_sum = y_sum + j
                y_num = y_num + 1

    y_mean = y_sum / y_num

    if y_mean < destin.shape[1] / 2:
        cmd_num = 1
    elif y_mean > destin.shape[1] / 2:
        cmd_num = 2
    else:
        cmd_num = 3

    cv.putText(frame, cmd[cmd_num], (x2, y1 - 5), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    return cmd_num

if __name__ == '__main__':
    """"""
    # round_standard = cv.cvtColor(cv.imread(path + "round_standard.png"), cv.COLOR_BGR2GRAY)
    # left_arrow_standard = cv.cvtColor(cv.imread(path + "left_arrow_standard.png"), cv.COLOR_BGR2GRAY)
    # right_arrow_standard = cv.cvtColor(cv.imread(path + "right_arrow_standard.png"), cv.COLOR_BGR2GRAY)
    # standard_list = [round_standard, left_arrow_standard, right_arrow_standard]


    # """"""
    # #src = load_img(path + "red_round1.png")
    # src = load_img(path + "arrow3.png")
    # show_img(src, "src")
    #
    # pret, color = pretreatment(src)
    # print(color)
    #
    # show_img(pret, "pret")
    # x1, y1, x2, y2 = identify_logo_findContours(src, pret)
    # destin = pret[y1:y2, x1:x2]
    # cmd = compare(destin, standard_list)
    #
    # print(cmd)


    cap = cv.VideoCapture(path+"小车行车记录仪.avi")
    while((cap.isOpened())):
        ret, frame = cap.read()

        pret, color = pretreatment(frame)
        #将图片的轮廓剪切下来
        x1, y1, x2, y2 = identify_logo_findContours(frame, pret)

        destin = pret[y1:y2, x1:x2]
        #和标准图片进行比较
        cmd_num = compare(destin, frame)

        cv.imshow('frame', frame)
        print(cmd[cmd_num])

        if cv.waitKey(25) & 0xFF == ord('q'):
            break


    cap.release()
    cv.destroyWindow()



