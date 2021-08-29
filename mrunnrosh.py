from PIL import Image, ImageFont, ImageDraw
import random

from telethon import TelegramClient, events
api_id = 7292613
api_hash = 'b9ba8cddfa0ca77ed102960554fe4cda'
token = '1965005670:AAF04TnUpmGhU-ToRZV4q1w2w4jvC6ylJnw'
OWNER_ID = '1042657912'
client = TelegramClient("mrunal", api_id, api_hash).start(bot_token=token)
mm = '''
you can make logo of your name
Type /logo
'''
@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    await event.reply("please use me in pm🥺")
  else:
    await event.reply(mm)

from telethon import events
@client.on(events.NewMessage(pattern="/logo ?(.*)",outgoing=True ))
async def logo(event):
  quew = event.pattern_match.group(1)
  if not quew:
    await event.reply('**Provide Some Text To Draw! Noob...**')
    return
  await event.reply('Creating your logo...wait!')
  await event.reply(f"Your logo : {quew}")
try :
  text = "{quew}"

photo = "Mrunal/mrunal.jpg"

color= "white"

X = "Mrunal/Chophsic.otf"

pp = "photo"

fnt = random.choice(os.listdir(X))

image = Image.open(photo)

draw = ImageDraw.Draw(image)

font = ImageFont.truetype(f"{X}/{fnt}", 120)

draw.text((150, 150), text, fill =color, font =font, align ="center")

image.save('output.jpg')

await e.reply(file="output.jpg")

