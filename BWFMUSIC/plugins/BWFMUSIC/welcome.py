import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from BWFMUSIC import app  

photo = [ ### ❖ ➥ 𝗕𝐖𝗙 𝗠𝗨𝗦𝗜𝗖™🇮🇳
    "https://telegra.ph/file/72f6ad49d321c88135727.jpg",
    
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷𝐇ᴇʏ🧸 {message.from_user.mention} 🌲𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ💐**\n\n"
                
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"⛩️ 𝐖ᴇʟᴄᴏᴍᴇ 𝐁σт 𝐀ᴅᴅ ⛩️", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
