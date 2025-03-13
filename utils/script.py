class script(object):
    START = """**Hello {} 🤟**
   
I am **Find Post Bot**.I am best Channel Link Search Bot! 
I Will filter your channel posts automatically and send it in your group chat when Someone search it."""

    HELP = """💢 ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ɪɴ ᴀ ɢʀᴏᴜᴘ

❂ ᴀᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ.⚠️ ᴀʟʟ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘꜱ 👇

❂ ᴛʏᴘᴇ /verify ɪɴ ɢʀᴏᴜᴘ.

❂ sᴇɴᴅ /ᴠᴇʀɪғʏ ɪɴ ɢʀᴏᴜᴘ & ᴡᴀɪᴛ ғᴏʀ ɪᴛ ᴛᴏ ᴀᴄᴄᴇᴘᴛ ᴏʀ ᴅɪʀᴇᴄᴛʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴏᴡɴᴇʀ ᴀғᴛᴇʀ ʀᴇᴏ‌ᴜᴇsᴛ @ACX_OWNER_DM_ROBOT

❂ ᴀꜰᴛᴇʀ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ꜱᴇɴᴅ /connect ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪᴅ
⤨ ᴇxᴀᴍᴘʟᴇ -

/connect -100xxxxxxxxxxx

❂ ʀᴇᴍᴏᴠᴇ ᴀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ
/disconnect -100xxxxxxxxxxx
ᴛʜɪꜱ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀ ɪɴᴅᴇxᴇᴅ ᴄʜᴀɴɴᴇʟ ꜰʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

❂ ʀᴇꜱᴇᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴡɪᴛʜ /reset_grp.
ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴘʀᴇᴠɪᴏᴜꜱ ꜱᴇᴛᴛɪɴɢꜱ ꜰʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.

❂ ꜰᴏʀ ᴀᴅᴅɪɴɢ ꜰᴏʀᴄᴇ ꜱᴜʙ ɪɴ ɢʀᴏᴜᴘ ᴛʏᴘᴇ /fsub ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪᴅ
⤨ ᴇxᴀᴍᴘʟᴇ -

/fsub -100xxxxxxxxxx

❂ ꜰᴏʀ ʀᴇᴍᴏᴠɪɴɢ ꜰᴏʀᴄᴇ ꜱᴜʙ ɪɴ ɢʀᴏᴜᴘ ᴛʏᴘᴇ /nofsub

❂ ɢᴇᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ ʟɪꜱᴛ ᴡɪᴛʜ - /connections


⏣►📃 𝗜ғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴋɪɴᴅ ᴏғ ɪ𝘀𝘀ᴜᴇ, ᴘʀᴏʙʟᴇᴍ ᴏʀ ɴᴇᴇᴅ 𝘀ᴜᴘᴘᴏʀᴛ ᴡʜɪʟᴇ ᴜ𝘀ɪɴɢ ᴛʜɪ𝘀 ʙᴏᴛ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴍᴇ𝘀𝘀ᴀɢᴇ ᴏᴜʀ 𝘀ᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ʙᴇ 𝘀ᴏʟᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇʀᴇ.➠ @ACX_DISCUSSION"""

    ABOUT = """Developed By @CyniteBackup

✯ Mʏ Nᴀᴍᴇ:  {}
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/CyniteOfficial'>Harman</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://cloud.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: : <a href='https://heroku.com'>Heroku</a>"""

    STATS = """My Status 💫

👥 Users: {}
🧿 Groups: {}"""

    BROADCAST = """<u>{}</u>

Total: `{}`
Remaining: `{}`
Success: `{}`
Failed: `{}`"""

    
