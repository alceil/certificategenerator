from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd


def creatcert(name:str):
    image_1 = Image.open('UX Certificate.png')
    draw = ImageDraw.Draw(image_1)
    font = ImageFont.truetype("arial.ttf",60)
    draw.text((361,356),name,(0,0,0),font=font)
    image_1.save(f'cert/{name}.png')

dataframe = pd.read_excel('data.xlsx')
for i in dataframe.index:
    entry = dataframe.iloc[i]
    name = entry['Full Name']
    creatcert(name)





