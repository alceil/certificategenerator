from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd
import random


def creatcert(name:str):
    image_1 = Image.open('UX Certificate.png')
    draw = ImageDraw.Draw(image_1)
    n = random.randint(100,999)
    certno=f'C2U0I{n}U1X1K'
    certid = "Completion ID: " + certno 
    if len(name) >= 14:
        font = ImageFont.truetype("arial.ttf",50)
        draw.text((357,314),name,(0,0,0),font=font)
        font2 = ImageFont.truetype("arial.ttf",12)
        draw.text((74,686),certid,(0,0,0),font=font2)  
       
    else:
        font = ImageFont.truetype("arial.ttf",50)
        draw.text((420,314),name,(0,0,0),font=font)
        font2 = ImageFont.truetype("arial.ttf",12)
        draw.text((74,686),certid,(0,0,0),font=font2)    
        # 361,356
    image_1.save(f'cert/{name}.png')

dataframe = pd.read_excel('Participants.xlsx')
for i in dataframe.index:
    entry = dataframe.iloc[i]
    name = entry['Full Name']
    creatcert(name)





