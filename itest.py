from PIL import Image, ImageDraw, ImageFont, ImageShow
background = Image.open("/home/hamze/personal/s.jpg").convert("RGBA")
tbackground = Image.new("RGBA", background.size, (255, 255, 255, 0))
print(background.getbbox())
# font labels
fontL = ImageFont.truetype(
    "usr/share/fonts/truetype/nunitosans/NunitoSans-ExtraBold.ttf",
    16, encoding="unic")
fontN = ImageFont.truetype(
    "usr/share/fonts/truetype/nunitosans/NunitoSans-ExtraBold.ttf",
    40, encoding="unic")
drawb = ImageDraw.Draw(tbackground)
print(fontL.getbbox("SECONDS"))
# label DAYS
drawb.rounded_rectangle((80-22, 150, 80+22, 200),
                        fill="white", width=0, radius=7)
drawb.rounded_rectangle((320-80-29, 150, 320-80+29, 200),
                        fill="white", width=0, radius=7)
drawb.rounded_rectangle((320+80-35.5, 150, 320+80+35.5, 200),
                        fill="white", width=0, radius=7)
drawb.rounded_rectangle((640-80-38.5, 150, 640-80+38.5, 200),
                        fill="white", width=0, radius=7)
drawb.text((80, 140), '05', anchor="ms", fill=(255, 255, 255, 0), font=fontN)
# label DAYS
drawb.text((80, 215), 'DAYS', anchor="ms", fill='red', font=fontL)
drawb.text((320-80, 215), 'HOURS', anchor="ms", fill='red', font=fontL)
drawb.text((320+80, 215), 'MINUTES', anchor="ms", fill='red', font=fontL)
drawb.text((640-80, 215), 'SECONDS', anchor="ms", fill='red', font=fontL)
# draw the text onto the text canvas, and use blue as the text color

# save the blank canvas to a file
out = Image.alpha_composite(background, tbackground)
out.save("/home/hamze/personal/unicode-text.png", "PNG")
ImageShow.register(ImageShow.EogViewer(), 0)
ImageShow.show(out)
