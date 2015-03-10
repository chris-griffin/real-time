from PIL import Image, ImageFont, ImageDraw

staticimg = Image.open('staticimages/23N.ppm')
draw = ImageDraw.Draw(staticimg)
font = ImageFont.truetype('/usr/share/fonts/truetype/droid/DroidSans.ttf', 12)
draw.text((14, 1),'3,5,18,24',(50,50,50),font=font)
staticimg.save('dynamicimages/23N.ppm')

