from PIL import Image
mac = Image.open('example.jpg')
print(type(mac))
print(mac.size)
print(mac.format_description)
#mac = mac.crop((0,0,100,100))
mac = mac.rotate(90)
mac.save("rotated_example.jpg")
