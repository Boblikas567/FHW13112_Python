import cv2
from PIL import Image

img_path = "man.jpg"
man_face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread(img_path)
man_face = man_face_cascade.detectMultiScale(image)
print(man_face)

man = Image.open(img_path)
glasses = Image.open("24910-6-glasses (1).png")
man = man.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x,y,w,h) in man_face:
    glasses = glasses.resize((w, int(h/3)))
    man.paste(glasses, (x, int(y+h/4)), glasses)
    man.save("man_glasses.png")
    man_glass = cv2.imread("man_glasses.png")
    cv2.imshow("Man", man_glass)
    cv2.waitKey()