import cv2
import numpy as np
import matplotlib.pyplot as plt

b = np.zeros((5, 5))
plt.imshow(b, cmap='gray')
plt.savefig('output_image.png')
plt.close()
print(b)
