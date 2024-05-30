import logging
import os
from Config import Messages as tr
from Config import Config as C
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
UPDATES_CHANNEL = C.UPDATES_CHANNEL
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.incoming & filters.command(['start']) & filters.private)
async def _start(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               await client.send_message(
                   chat_id=message.chat.id,
                   text="ʏᴏᴜ  ᴀʀᴇ  ʙᴀɴɴᴇᴅ  ᴛᴏ  ᴜsᴇ  ᴛʜɪs  ʙᴏᴛ.",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.chat.id,
                text=f"ᴅᴜᴇ  ᴛᴏ  ᴏᴠᴇʀʟᴏᴀᴅ,  ᴏɴʟʏ  ᴄʜᴀɴɴᴇʟ  ᴍᴇᴍʙᴇʀꜱ  ᴄᴀɴ  ᴜꜱᴇ  ᴍᴇ.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔥  𝙹𝙾𝙸𝙽  𝚄𝙿𝙳𝙰𝚃𝙴  𝙲𝙷𝙰𝙽𝙽𝙴𝙻  🔥", url=f"https://telegram.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(message.chat.id,
                text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚚     ɱᴀɪɴ   𝙲ʜᴀɴɴᴇʟ     ⚚', url='https://youtube.com/@RahulReviews')],[InlineKeyboardButton('😊  𝙰ʙᴏᴜᴛ', url='https://telegram.me/RahulReviews'),InlineKeyboardButton('👨‍💻  𝙾ᴡɴᴇʀ', url='https://telegram.me/CodeXBro')]]),                
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
            return
    await client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚚     ɱᴀɪɴ   𝙲ʜᴀɴɴᴇʟ     ⚚', url='https://youtube.com/@RahulReviews')],[InlineKeyboardButton('😊  𝙰ʙᴏᴜᴛ', url='https://telegram.me/RahulReviews'),InlineKeyboardButton('👨‍💻  𝙾ᴡɴᴇʀ', url='https://telegram.me/CodeXBro')]]), 
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )


@Client.on_message(filters.incoming & filters.command(['source_code']) & filters.private)
async def _source_code(client, message):
    await client.send_message(message.chat.id,
        text=tr.SC_MSG.format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Souce Code", url="https://github.com/CodeXBots/Force-Sub-Bot")
                ],
                [
                    InlineKeyboardButton("Join Updates Channel", url="https://telegram.me/RahulReviewsYT"),
                    InlineKeyboardButton("Support Group", url="https://telegram.me/CodeXSupport")
                ],
                [
                    InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url="https://telegram.me/CodeXBro")
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.incoming & filters.command(['help']) & filters.private)
async def _help(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               await client.send_message(
                   chat_id=message.chat.id,
                   text="ʏᴏᴜ  ᴀʀᴇ  ʙᴀɴɴᴇᴅ  ᴛᴏ  ᴜsᴇ  ᴛʜɪs  ʙᴏᴛ.",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.chat.id,
                text=f"ᴅᴜᴇ  ᴛᴏ  ᴏᴠᴇʀʟᴏᴀᴅ,  ᴏɴʟʏ  ᴄʜᴀɴɴᴇʟ  ᴍᴇᴍʙᴇʀꜱ  ᴄᴀɴ  ᴜꜱᴇ  ᴍᴇ.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔥  𝙹𝙾𝙸𝙽  𝚄𝙿𝙳𝙰𝚃𝙴  𝙲𝙷𝙰𝙽𝙽𝙴𝙻  🔥", url=f"https://telegram.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.chat.id,
                text="Hey use this command in my pm. \nFor more help ask in my [Support Group](https://telegram.me/CodeXSupport).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
async def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    await client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '-->', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        button = [
            [InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '-->', callback_data = f"help+{pos+1}")
            ],
        ]
    return button