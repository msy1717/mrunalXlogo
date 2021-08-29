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

client.run_until_disconnected()