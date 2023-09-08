import matplotlib.pyplot as plt
from ultralytics import YOLO
import glob
import os
import cv2
import numpy as np


"""
    main(): detect single image, save the result as a RESULT class
    RESULT:
        __attribute__:
            boxes:  numpy array, detected bounding box's xyxy
            cls:    numpy array, detected bounding box's cls
            conf:   numpy array, detected bounding box's conf  
"""

class RESULT:
    def __init__(self, boxes, cls, conf, names):
        self.boxes = boxes
        self.cls = cls
        self.conf = conf
        self.names = names

    def __len__(self):
        return len(self.boxes)

    def __getitem__(self, idx):
        return {'cls': self.cls[idx], 'conf': self.conf[idx], 'box': self.boxes[idx]}


def read_images(path):
    return glob.glob(os.path.join(path, '*.JPG'))

def preprocess(image):
    image = cv2.resize(image, (640, 640))
    return image

def scale_box(boxes, sf):
    for box in boxes:
        box[0] = box[0] * sf[0]
        box[1] = box[1] * sf[1]
        box[2] = box[2] * sf[0]
        box[3] = box[3] * sf[1]
    return boxes

def main(model, img):
    # model: path to the model
    # data: path to the data directory
    
    model = YOLO(model)
    source = cv2.imread(img)
    sf = np.array([source.shape[0] / 640, source.shape[1] / 640])
    source = preprocess(source)
    result = model.predict(source, conf=0.25)
    print(result.plot())

    boxes = result[0].boxes.xyxy.numpy()
    boxes = scale_box(boxes, sf)
    cls = result[0].boxes.cls.numpy()
    conf = result[0].boxes.conf.numpy()
    names = result[0].names

    result = RESULT(boxes, cls, conf, names)
    return result
                
if __name__ == '__main__':
    # test
    model = os.path.join('model', 'best.pt')
    image = os.path.join('0504', '103FTASK', 'MAX_0435.JPG')
    result = main(model, image)
    print(result[0])
