from PIL import Image
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import tensorflow as tf
img1= Image.open(r'C:\Users\devak\Downloads\download.jpg')
plt.subplot(1,2,1)
plt.title('Original Image')
img = np.array(img1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.title('Augmented[Height Shift]')
plt.imshow(img)
datagen = ImageDataGenerator(height_shift_range=0.6,fill_mode="wrap")
plt.show()


