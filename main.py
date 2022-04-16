import cv2
import numpy as np
from pyzbar.pyzbar import decode


def readCode():
    img = cv2.imread("test.png")

    for barcode in decode(img):
        print(barcode.data)
        print(barcode.rect)
        myData = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        cv2.putText(img, myData, (barcode.rect[0], barcode.rect[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        print(myData)
    cv2.imshow("Image", img)
    cv2.waitKey(0)


def readCodeFromCamera():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        for barcode in decode(img):
            print(barcode.data)
            print(barcode.rect)
            myData = barcode.data.decode('utf-8')
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
            # cv2.rectangle(img, (barcode.rect[0], barcode.rect[1]), (barcode.rect[2], barcode.rect[3]), (255, 0, 0), 2)
            cv2.putText(img, myData, (barcode.rect[0], barcode.rect[1]), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2, cv2.LINE_AA)
            print(myData)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    readCode()
