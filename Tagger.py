import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from random import choice

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

emoji_calisan = []

anlik_calisan = []

tekli_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**๐Perintah Kang Tag**\n Saya Dapat Menandai Hampir Semua Anggota Di Grup Anda Dengan \nUntuk perintah, ketikkan =======> /help**",
                    buttons=(
                   
		       [Button.url('โ Tambahkan ke Grup โ', 'https://t.me/kangtagbot?startgroup=a')],
                      [Button.url('Support', 'https://t.me/DutabotId')],
                   
		      [Button.url('Developer', 'https://t.me/Mazekubot')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**๐ Perintah Kang Tag**\n\n**/tag <pesan> - Tag 5 anggota**\n\n**/etag <pesan> - Emoji dan tag**\n\n**/tektag pesan - Anggota Tag Individual**\n\n**/admins pesan - Tag Admin Satu per Satu**\n\n**/start - memulai bot**"
  await event.reply(helptext,
                    buttons=(
                       [Button.url('โ Tambahkan ke Grup โ', 'https://t.me/kangtagbot?startgroup=a')],
                      [Button.url('Support', 'https://t.me/DutabotId')],
                   
		      [Button.url('Developer', 'https://t.me/Mazekubot')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**Banyak fitur @kangtagbot pemilik Grub yang mencoba menemukan bot tag cocok untuk Anda:\n\n๐ tag 5 anggota \n๐ Stiker emoji\n๐ Label tunggal\n๐ Tag Satu Admin\n๐\n\n Anda dapat menambahkan @kangtagbot multi-fitur seperti admin ke grup Anda dan dengan mudah menjadi anggota, Anda dapat menetapkan tag **"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('โ Tambahkan ke Grup โ', 'https://t.me/kangtagbot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


emoji = " โค๏ธ ๐งก ๐ ๐ ๐ ๐ ๐ค ๐ค ๐ค ๐ ๐ ๐ ๐ ๐ ๐ฅฐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐คช ๐คจ ๐ง ๐ค ๐ ๐คฉ ๐ฅณ ๐ ๐ " \
        "๐ ๐ ๐ ๐ ๐ ๐ฃ ๐ ๐ซ ๐ฉ ๐ฅบ ๐ข ๐ญ ๐ค ๐? ๐ก  ๐คฏ ๐ณ ๐ฅต ๐ฅถ ๐ฑ ๐จ ๐ฐ ๐ฅ ๐ ๐ค ๐ค ๐คญ ๐คซ ๐คฅ ๐ถ ๐ ๐ ๐ฌ ๐ " \
        "๐ฏ ๐ฆ ๐ง ๐ฎ ๐ฒ ๐ฅฑ ๐ด ๐คค ๐ช ๐ต ๐ค ๐ฅด ๐คข ๐คฎ ๐คง ๐ท ๐ค ๐ค ๐ค ๐ค? ๐ ๐ฟ ๐น ๐บ ๐คก  ๐ป ๐ ๐ฝ ๐พ ๐ค ๐ ๐บ ๐ธ ๐น " \
        "๐ป ๐ผ ๐ฝ ๐ ๐ฟ ๐พ".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global emoji_calisan
  if event.is_private:
    return await event.respond("**Perintah ini hanya untuk grup**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Hanya administrator yang dapat menggunakan perintah ini**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Tag untuk pesan sebelumnya**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tidak ada..! alasan untuk membuat label๏ธ")
  else:
    return await event.respond("**Pada label, ketikkan alasan untuk memulai...!**")
  
  if mode == "text_on_cmd":
    emoji_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("** Tag berhasil dihentikan**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    emoji_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("Operasi berhenti dengan sukses\n\n**Buddha bisa menjadi @kangtagbot Anda**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Perintah ini berlaku untuk grup dan saluran๏ธ**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Hanya administrator yang dapat menggunakan perintah ini๏ธ**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Jangan Membalas Pesan Sebelumnya")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tidak ada alasan untuk memulai ๏ธ")
  else:
    return await event.respond("Tidak ada alasan untuk memulai")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"๐ฅ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Operasi Berhasil Dihentikan\n\n**Ini bisa jadi iklan Anda @kangtagbot**โ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"๐ฅ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Operasi Berhasil Dihentikanโ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar iรงin geรงerliโ๏ธ**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Hanya administrator yang dapat menggunakan perintah ini.**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**รถnceki mesajฤฑ etiketleye bilmerim*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tulis Alasan untuk Memulai !๏ธ")
  else:
    return await event.respond("**Tulis alasan saya untuk memulai proses..**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**๐ค - [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Operasi Berhasil Dihentikan\n\n**Ini bisa jadi iklan Anda @kangtagbot**โ****")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"๐ค - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("Operasi Berhasil Dihentikan\n\n**Ini bisa jadi iklan Anda @kangtagbot**โ**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def mentionall(tagadmin):

	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> Bot sedang bermain jangan khawatir ๐ @mazekubot Anda bisa mendapatkan informasi <<")
client.run_until_disconnected()
