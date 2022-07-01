import cv2
import numpy as np

# import os
# print(os.getcwd())

def mix(num):

    net = cv2.dnn.readNetFromTorch(num)

    img = cv2.imread('gallery1/input/input_img.jpg')
    print(img)
    h, w, c = img.shape
    img = cv2.resize(img, dsize=(500, int(h / w * 500)))

    print(img.shape) # (325, 500, 3)

    MEAN_VALUE = [103.939, 116.779, 123.680]
    blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

    print(blob.shape) # (1, 3, 325, 500)

    net.setInput(blob)
    output = net.forward()

    output = output.squeeze().transpose((1, 2, 0))
    output += MEAN_VALUE

    output = np.clip(output, 0, 255)
    output = output.astype('uint8')


    # cv2.imshow('img', img)
    # cv2.imshow('output', output)
    cv2.imwrite('gallery1/output/output.jpg', output)
    # cv2.waitKey(0)

