from PIL import Image


image = Image.open("monro.jpg")

red, green, blue = image.split()

cropped_left_red = red.crop((100, 0, red.width, red.height))
cropped_middle_red = red.crop((50, 0, red.width-50, red.height))
image_red = Image.blend(cropped_left_red, cropped_middle_red, 0.5)

cropped_right_blue = blue.crop((0, 0, blue.width-100, blue.height))
cropped_middle_blue = blue.crop((50, 0, blue.width-50, blue.height))
image_blue = Image.blend(cropped_right_blue, cropped_middle_blue, 0.5)

image_green = green.crop((50, 0, green.width-50, green.height))

new_image_monro = Image.merge("RGB", (image_red, image_green, image_blue))
new_image_monro.save("new_image_monro.jpg")
new_image_monro.thumbnail((80, 80))
new_image_monro.save("new_image_monro_avatar.jpg")