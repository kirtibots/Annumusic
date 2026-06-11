# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------
from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app

# ── Premium emoji IDs (Emoji_fan37_by_TgEmodziBot pack) ──
_E_SHIELD  = 4958900559139570572   # 🛡  Admin
_E_BELL    = 4956290155326473271   # 🔔  Auth
_E_MEGA    = 4958686613933655185   # 📣  G-Cast
_E_BAN     = 4956337889593000947   # 🚫  Bl-Chat
_E_SKULL   = 4958642964181025908   # 💀  Bl-Users
_E_PLAY    = 4956250031741993892   # ▶️  C-Play
_E_XSKULL  = 4956461073550017373   # ☠️  G-Ban
_E_LOOP    = 4956371914323920049   # 🔄  Loop
_E_CHART   = 4958506272551863292   # 📊  Log
_E_BOLT    = 4958479549265347295   # ⚡️  Ping
_E_MUSIC   = 4958562566688211974   # 🎶  Play
_E_HAT     = 4956564307383944011   # 🎩  Shuffle
_E_SEARCH  = 4958587679361991667   # 🔍  Seek
_E_MIC     = 4956441587283395517   # 🎤  Song
_E_CAR     = 4958801766301828295   # 🚗  Speed
_E_CLOSE   = 4958526153955476488   # ❌  Close
_E_BACK    = 4956282853882069908   # ➡️  Back
_E_BULB    = 4958665796227171144   # 💡  Help DM


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(
        text=_["CLOSE_BUTTON"],
        callback_data="close",
        icon_custom_emoji_id=_E_CLOSE
    )]
    second = [
        InlineKeyboardButton(
            text=_["BACK_PAGE"],
            callback_data="mbot_cb",
        ),
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
            icon_custom_emoji_id=_E_BACK
        ),
        InlineKeyboardButton(
            text=_["NEXT_PAGE"],
            callback_data="mbot_cb",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                    icon_custom_emoji_id=_E_SHIELD,
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                    icon_custom_emoji_id=_E_BELL,
                ),
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                    icon_custom_emoji_id=_E_MEGA,
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                    icon_custom_emoji_id=_E_BAN,
                ),
                InlineKeyboardButton(
                    text=_["H_B_5"],
                    callback_data="help_callback hb5",
                    icon_custom_emoji_id=_E_SKULL,
                ),
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="help_callback hb6",
                    icon_custom_emoji_id=_E_PLAY,
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="help_callback hb7",
                    icon_custom_emoji_id=_E_XSKULL,
                ),
                InlineKeyboardButton(
                    text=_["H_B_8"],
                    callback_data="help_callback hb8",
                    icon_custom_emoji_id=_E_LOOP,
                ),
                InlineKeyboardButton(
                    text=_["H_B_9"],
                    callback_data="help_callback hb9",
                    icon_custom_emoji_id=_E_CHART,
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_10"],
                    callback_data="help_callback hb10",
                    icon_custom_emoji_id=_E_BOLT,
                ),
                InlineKeyboardButton(
                    text=_["H_B_11"],
                    callback_data="help_callback hb11",
                    icon_custom_emoji_id=_E_MUSIC,
                ),
                InlineKeyboardButton(
                    text=_["H_B_12"],
                    callback_data="help_callback hb12",
                    icon_custom_emoji_id=_E_HAT,
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_13"],
                    callback_data="help_callback hb13",
                    icon_custom_emoji_id=_E_SEARCH,
                ),
                InlineKeyboardButton(
                    text=_["H_B_14"],
                    callback_data="help_callback hb14",
                    icon_custom_emoji_id=_E_MIC,
                ),
                InlineKeyboardButton(
                    text=_["H_B_15"],
                    callback_data="help_callback hb15",
                    icon_custom_emoji_id=_E_CAR,
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="settings_back_helper",
                    icon_custom_emoji_id=_E_BACK,
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
                icon_custom_emoji_id=_E_BULB,
            ),
        ],
    ]
    return buttons
