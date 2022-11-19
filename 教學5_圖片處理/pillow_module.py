from PIL import Image

#開啟、顯示圖片
image = Image.open('./miyuki.jpg')
image.show()

#剪裁圖片
rect = 80, 20, 310, 360
image.crop(rect).show()

#生成縮略圖
size = 128, 128
image.thumbnail(size)
image.show()

