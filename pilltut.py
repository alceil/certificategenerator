from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
image_1 = Image.open('UX Certificate.png')
# image_1.show()
draw = ImageDraw.Draw(image_1)
font = ImageFont.truetype("arial.ttf",60)
draw.text((361,356),'Ashish Thomas',(0,0,0),font=font)
image_1.save('ashish.png')