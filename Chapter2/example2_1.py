import keras
from keras.datasets import mnist

# Sets of images and labels that the model will learn from
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images.shape
