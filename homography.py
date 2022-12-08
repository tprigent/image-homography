import os
import cv2
import numpy as np


# handle click on image for point definition
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # memorize coordinates
        x1.append(x)
        y1.append(y)

        # overlay clicked images
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img_shown, str(x) + ',' +
                    str(y), (x, y), font,
                    1, (0, 255, 0), 2)
        cv2.imshow('Select 4 points and press ENTER', img_shown)


if __name__ == "__main__":
    # reading the image
    img_src_name = 'rgb0001.jpg'
    img_src = cv2.imread(img_src_name, 1)
    img_shown = np.copy(img_src)
    width = img_src.shape[1]
    height = img_src.shape[0]

    # display image
    cv2.imshow('Select 4 points and press ENTER', img_shown)

    x1 = []
    y1 = []
    pts_final = np.array([[0, 0], [width, 0], [width, height], [0, height]])
    cv2.setMouseCallback('Select 4 points and press ENTER', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # homography computation
    n = 4
    A = np.zeros((n * 3, 9))
    x2 = pts_final[:, 0]
    y2 = pts_final[:, 1]

    for i in range(n):
        tmp = np.array([[x1[i], y1[i], 1, 0, 0, 0, -x2[i] * x1[i], -x2[i] * y1[i], -x2[i]],
                        [0, 0, 0, x1[i], y1[i], 1, -y2[i] * x1[i], -y2[i] * y1[i], -y2[i]]])
        A = np.concatenate((A, tmp), axis=0)

    u, s, v = np.linalg.svd(A, full_matrices=False)
    H = v[-1].reshape(3, 3)

    # apply homography
    img_dst = cv2.warpPerspective(img_src, H, (width, height))

    # write and open destination image
    img_dst_name = 'res-' + img_src_name
    cv2.imwrite('res-' + img_src_name, img_dst)
    os.system('open /System/Applications/Preview.app ' + img_dst_name)
