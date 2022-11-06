import numpy as np
from PIL import Image

l = np.array([[0, 128, 255], [0, 128, 255], [0, 128, 255]])
im = Image.fromarray(np.uint8(l), "L")
im.show()
