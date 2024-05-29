
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
img = Image.open(r'C:\Users\devak\Figure_1.png')
plt.subplot(1,2,1)
plt.title('Original Image')
img= np.array(img)
plt.imshow(img)
plt.subplot(1,2,2)
plt.title('Augmented Image]')
plt.imshow(img)


rotated_image1 = img.rotate(180)
 
# This is Alternative Syntax To Rotate
# The Image
rotated_imag2=img.transpose(Image.ROTATE_90)
 
# This Will Rotate Image By 60 Degree
rotated_image3 = img.rotate(60)
rotated_image1.show()
rotated_image2.show()
rotated_image3.show()
#data=np.img(
   # rotation_range = 40,
    #shear_range = 0.2,
#zoom_range = 0.2,
#horizontal_flip = True,
#brightness_range = (0.5, 1.5))
#plt.show(data)
