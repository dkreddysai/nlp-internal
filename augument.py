from PIL import Image
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
img1 = Image.open(r'C:\Python310\dog.webp')
plt.subplot(1,2,1)
plt.title('Original Image')
img = np.array(img1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.title('Augmented[Rotation]')
plt.imshow(img)
img2=img1.rotate(180)
flipped_img=np.fliplr(img2)
plt.imshow(flipped_img)
plt.show()


 
