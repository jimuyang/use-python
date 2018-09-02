from PIL import Image, ImageFilter
import os

path = os.path.abspath('.')
print(path)

im = Image.open(path + '/resource/cat.jpg', mode="r")
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save(path + '/resource/thumbnail.jpg', 'jpeg')

im2 = im.filter(ImageFilter.BLUR)
im2.save(path + '/resource/blur.jpg', 'jpeg')
