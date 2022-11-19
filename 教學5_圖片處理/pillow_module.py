from PIL import Image, ImageFilter

#開啟、顯示圖片
image = Image.open('./miyuki.jpg')
image.show() #要一段時間才會開啟圖片
image.close()

#剪裁圖片
image = Image.open('./miyuki.jpg')
rect = 80, 20, 310, 360
image.crop(rect).show()

#生成縮略圖
image = Image.open('./miyuki.jpg')
size = 128, 128
image.thumbnail(size)
image.show()

#縮放和黏貼圖片
image1 = Image.open('./miyuki.jpg')
image2 = Image.open('./miyuki.jpg')
rect = 80, 20, 310, 360
guido_head = image2.crop(rect) #剪下一塊
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40)) #貼到i1上
image1.show()

#旋轉、翻轉
image = Image.open('./miyuki.jpg')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()

#操作像素
image = Image.open('./miyuki.jpg')
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128)) #該像素區塊改成灰色RGB
image.show()

#濾鏡效果
image = Image.open('./miyuki.jpg')
image.filter(ImageFilter.CONTOUR).show() #輪廓濾鏡



