#
# Copyright (C) 2021-2022 by StormBeatz@Github, < https://github.com/StormBeatz >.
#
# This file is part of < https://github.com/StormBeatz/StormBeatz > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/StormBeatz/StormBeatz/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="📚 All Commands", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="Dev", url="https://t.me/ItsChinnoda"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="DKNF", url="https://t.me/Dark_night_logs"
            ),
            InlineKeyboardButton(
                text="TFTC Group", url="https://t.me/Telugu_family_Ties_chatting"
            ),                       
        ],        
        [
            InlineKeyboardButton(
                text="Chinna", url="https://t.me/ItsChinnoda"
            ),                                  
        ]
    ]
    return buttons


def private_panel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add me to your group ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Help", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="DKNF", url="https://t.me/Dark_night_logs"),
            InlineKeyboardButton(
                text="TFTC Group", url=f"https://t.me/Telugu_family_Ties_chatting"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🏳️‍🌈 Language", callback_data="LG"
                )
        ],
        [
            InlineKeyboardButton(
                text="Chinna", url="https://t.me/ItsChinnoda"
            )
        ]
     ]
    return buttons
