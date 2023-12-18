from PIL import Image, ImageDraw, ImageFont, ImageShow
from datetime import datetime
from datetime import timedelta
import numpy as np


background = Image.open("/home/hamze/personal/s.jpg").convert("RGBA")
tbackground = Image.new("RGBA", background.size, (255, 255, 255, 0))
print(background.getbbox())
# font labels
fontL = ImageFont.truetype(
    "usr/share/fonts/truetype/nunitosans/NunitoSans-ExtraBold.ttf",
    14, encoding="unic")
fontN = ImageFont.truetype(
    "usr/share/fonts/truetype/nunitosans/NunitoSans-ExtraBold.ttf",
    44, encoding="unic")
drawb = ImageDraw.Draw(tbackground)
# label DAYS

# dates in string format
str_d1 = '2023/08/31'
str_d2 = '2023/08/27'

# convert string to date object
d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")
# difference between dates in timedelta
delta = d1 - d2
dt_store = np.char.array(np.zeros((4, 1)), unicode=True)
i = 0
pics = []
while delta.days > 0:
    delta -= timedelta(days=1, seconds=0, microseconds=0,
                       milliseconds=0, minutes=0, hours=0, weeks=0)
    dt_store[i, 0] = str(delta.days)
    i += 1
print(i)
dt_store = np.char.zfill(dt_store, 2)
for i in range(len(dt_store)):
    drawb = ImageDraw.Draw(tbackground)
    drawb.rounded_rectangle((207.5, 145, 242.5, 195),
                            fill="white", width=0, radius=7)
    drawb.rounded_rectangle((395, 145, 430, 195),
                            fill="white", width=0, radius=7)
    # label DAYS
    drawb.text((225, 170), dt_store[i, 0][0], anchor="mm",
               fill=(255, 255, 255, 0), font=fontN)
    drawb.text((412.5, 170), dt_store[i, 0][1], anchor="mm",
               fill=(255, 255, 255, 0), font=fontN)
    out = Image.alpha_composite(background, tbackground)
    #out = out.resize((320, 180), Image.LANCZOS)
    backgroundp = Image.new("RGB", out.size, (255, 255, 255))
    backgroundp.paste(out, mask=out.split()[3])
    #path = locals()["/home/hamze/personal/timer/"+str(i)+'.jpg']
    path = "/home/hamze/personal/timer/pic3/"+str(i)+'.jpg'
    backgroundp.save(path, 'jpeg')
    pics.append(out)
# ImageShow.register(ImageShow.EogViewer(), 0)

# ImageShow.show(out)
    print(round(i/(3600*6), 4)*100)
# pics[0].save("/home/hamze/personal/out2.gif", save_all=True,
#              optimize=True,
#              append_images=pics[1:], duration=1000, loop=0)
# draw the text onto the text canvas, and use blue as the text color

# save the blank canvas to a file
