#
# Copyright (C) 2022-2023 by StormBeatz@Github, < https://github.com/StormBeatz >.
#
# This file is part of < https://github.com/StormBeatz/StormBeatz > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/StormBeatz/StormBeatz/blob/master/LICENSE >
#
# All rights reserved.
#

from StormBeatz import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""**Hᴇʏʏ, MENTION !!\n\nTʜɪs Is Lʏʀᴀ Mᴜꜱɪᴄ Bᴏᴛ.\n\nA Pᴏᴡᴇʀғᴜʟ Mᴜsɪᴄ Pʟᴀʏᴇʀ Bᴏᴛ Wɪᴛʜ Sᴏᴍᴇ Aᴡᴇsᴏᴍᴇ Aɴᴅ Usᴇғᴜʟ Fᴇᴀᴛᴜʀᴇs.\n\nAʟʟ Oғ Mʏ Cᴏᴍᴍᴀɴᴅs Aʀᴇ Lɪsᴛᴇᴅ Iɴ Hᴇʟᴩ Bᴜᴛᴛᴏɴ.\n\nIғ Yᴏᴜ Hᴀᴠᴇ Aɴʏ Oᴛʜᴇʀ Qᴜᴇsᴛɪᴏɴs Aʙᴏᴜᴛ Mᴇ Asᴋ Iᴛ Iɴ Sᴜᴩᴩᴏʀᴛ Cʜᴀᴛ.\n\n"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : [-𝘽𝙤𝙩 𝘿𝙚𝙢𝙤𝙣𝙨](https://t.me/Bot_Demons).**
"""

COMMANDS_TEXT = f"""
✨ **𝙃𝙚𝙮𝙮𝙖, MENTION !!**
**𝘾𝙡𝙞𝙘𝙠 𝙤𝙣 𝙩𝙝𝙚 𝙗𝙪𝙩𝙩𝙤𝙣𝙨 𝙗𝙚𝙡𝙤𝙬 𝙩𝙤 𝙠𝙣𝙤𝙬 𝙢𝙮 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="❰📚 𝘽𝙖𝙨𝙞𝙘 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", url="https://telegra.ph/StormBeatz-Music-Bot-Commands-11-07"
            ),
            InlineKeyboardButton(
                text="❰🔧 𝙎𝙚𝙩𝙩𝙞𝙣𝙜 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="settings_helper"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/Xd_Nitric"
            ),
            InlineKeyboardButton(
                text="❰𝗚𝗿𝗼𝘂𝗽❱", url="https://t.me/+S7iHX7RSFk5kYjA1"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(

                        "❰➕ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 ➕❱",

                        url=f"https://t.me/MissStormBeatzRobot?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("❰𝙃𝙚𝙡𝙥❱", callback_data="settings_back_helper")],

                







                [

                    InlineKeyboardButton(

                        "❰𝗚𝗿𝗼𝘂𝗽❱", url=f"https://t.me/+S7iHX7RSFk5kYjA1"

                    ),

                    InlineKeyboardButton(

                        "❰𝗢𝘄𝗻𝗲𝗿❱", url=f"https://t.me/Xd_Nitric"

                    ),

                ],
                [
                 InlineKeyboardButton("❰🏳️‍🌈 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚❱", callback_data="LG"
            ),
        ],
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="❰𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="❰𝘽𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="❰𝙋𝙡𝙖𝙮 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", url="https://telegra.ph/StormBeatz-Music-Bot-Commands-11-07"
            ),            
            InlineKeyboardButton(
                text="❰𝙀𝙭𝙩𝙧𝙖 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", url="https://telegra.ph/StormBeatz-Music-Bot-Extra-Commands-11-07"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="❰↪️ 𝘽𝙖𝙘𝙠❱", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="❰𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="❰𝘽𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="❰𝙋𝙡𝙖𝙮 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="❰𝙎𝙪𝙙𝙤 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", url="https://telegra.ph/StormBeatz-Music-Bot-Sudo-Commands-11-07"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="❰𝙀𝙭𝙩𝙧𝙖 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", url="https://telegra.ph/StormBeatz-Music-Bot-Extra-Commands-11-07"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="❰↪️ 𝘽𝙖𝙘𝙠❱", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="❰↪️ 𝘽𝙖𝙘𝙠❱", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="❰𝙎𝙪𝙙𝙤 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", url="https://telegra.ph/StormBeatz-Music-Bot-Sudo-Commands-11-07"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="❰↪️ 𝘽𝙖𝙘𝙠❱", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
✅𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨:

c stands for channel play.

/pause or /cpause - Pause the playing music.
/resume or /cresume- Resume the paused music.
/mute or /cmute- Mute the playing music.
/unmute or /cunmute- Unmute the muted music.
/skip or /cskip- Skip the current playing music.
/stop or /cstop- Stop the playing music.
/shuffle or /cshuffle- Randomly shuffles the queued playlist.
/seek or /cseek - Forward Seek the music to your duration
/seekback or /cseekback - Backward Seek the music to your duration
/restart - Restart bot for your chat .


✅𝙎𝙥𝙚𝙘𝙞𝙛𝙞𝙘 𝙎𝙠𝙞𝙥:
/skip or /cskip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

✅𝙇𝙤𝙤𝙥 𝙋𝙡𝙖𝙮:
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.

✅𝘼𝙪𝙩𝙝 𝙐𝙨𝙚𝙧𝙨:
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.
"""

AUTH_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="❰↪️ 𝘽𝙖𝙘𝙠❱", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close_btn"
            ),            
        ],                        
    ]
)

BOT_TEXT = """
✅--**𝘽𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨:**--
/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.
/sudolist - Check Sudo Users of StormBeatz Music Bot
/lyrics [Music Name] - Searches Lyrics for the particular Music on web.
/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.
c stands for channel play.
/queue or /cqueue- Check Queue List of Music.
"""

PLAY_TEXT = """
✅--**𝙋𝙡𝙖𝙮 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨:**--
Available Commands = play , vplay , cplay
ForcePlay Commands = playforce , vplayforce , cplayforce
c stands for channel play.
v stands for video play.
force stands for force play.
/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.
/playforce or /vplayforce or /cplayforce -  Force Play stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.
/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.
✅--**𝘽𝙤𝙩'𝙨 𝙎𝙚𝙧𝙫𝙚𝙧 𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩𝙨:**--
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers.
"""


BASIC_TEXT = """
💠 **𝘽𝙖𝙨𝙞𝙘 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨:**
/start - Start the bot
/help - Get help message
/play - Play songs or videos in vc
/vplay - Play video in VC
/settings - Check Settings of bot in your group
**Some Useful Commands :** 
/pause /resume /skip /end /loop /shuffle
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="❰↪️ 𝘽𝙖𝙘𝙠❱", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close_btn"
            ),            
        ],                        
    ]
)

ADMIN_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="❰𝘼𝙪𝙩𝙝 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="auth_cmds"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="❰↪️ 𝘽𝙖𝙘𝙠❱", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="❰🔍 𝘽𝙖𝙨𝙞𝙘 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="❰📚 𝘼𝙙𝙫𝙖𝙣𝙘𝙚𝙙 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❰↪️ 𝘽𝙖𝙘𝙠❱", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close_btn"
            ),            
        ],                        
    ]
)
