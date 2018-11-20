
import keras

# import keras_retinanet
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color

# import miscellaneous modules
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time
import tensorflow as tf
def get_session():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    return tf.Session(config=config)
keras.backend.tensorflow_backend.set_session(get_session())
model_path = os.path.join('.', 'resnet50_anklebone.h5')
model = models.load_model(model_path, backbone_name='resnet50')
labels_to_names = {0: 'horse', 1: 'camel', 2: 'sheep', 3: 'goat'}
cap = cv2.VideoCapture(0)
while(True):
    ret, image = cap.read()
    #cv2.imshow('frame',frame)
    draw = image.copy()
    draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)
    image = preprocess_image(image)
    image, scale = resize_image(image)
    start = time.time()
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
    print("processing time: ", time.time() - start)
    boxes /= scale
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
    	if score < 0.5:
    		break
    	color = label_color(label)
    	b = box.astype(int)
    	draw_box(draw, b, color=color)
    	caption = "{} {:.3f}".format(labels_to_names[label], score)
    	draw_caption(draw, b, caption)
    #plt.figure(figsize=(15, 15))
    #plt.axis('off')
    #plt.imshow(draw)
    #plt.show()
    cv2.imshow('draw',draw)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()