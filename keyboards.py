from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from button_state import get_button_status

# Главное меню с разделом "Жидкости"
main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        # Болше варинатов
        [InlineKeyboardButton(text="Актуальное наличие", callback_data="liquids")]
    ]
)


def generate_assortiment_kb():
    buttons = [
        ("Российкая жидкость 🇷🇺", "russia_liquids"),
        ("Китайская жидкость 🇨🇳", "china_liquids"),
        ("Украинская жидкость 🇺🇦", "uk_liquids"),
        ("Одноразки", "hqd"),
        ("Pod-Системы", "pod_system"),
        ("Снюс", "snus"),
    ]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=cb)]
            for text, cb in buttons
            if get_button_status(cb)
        ]
    )
    return kb


def generate_russia_kb():
    buttons = [
        ("Анархия", "anarchia"),
    ]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=cb)]
            for text, cb in buttons
            if get_button_status(cb)
        ]
        + [[InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]]
    )
    return kb


def generate_china_kb():
    buttons = [
        ("Elf Liq 30 ml", "elfliq_30"),
        ("Elf Liq 10 ml", "elfliq_10"),
        ("HQD 30 ml", "hqd_30"),
        ("HQD 10 ml", "hqd_10"),
        ("Solana 30 ml", "solana_30"),
        ("Flonq Liquid 30 ml", "flonq_30"),
    ]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=cb)]
            for text, cb in buttons
            if get_button_status(cb)
        ]
        + [[InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]]
    )
    return kb


def generate_uk_kb():
    buttons = [
        ("Chaser Lux 30 ml - 6,5%", "chaser_lux_6_5"),
        ("Chaser Black 30 ml - 6,5%", "chaser_black_6_5"),
        ("Chaser Lux 30 ml - 5%", "chaser_lux_5"),
        ("Chaser Black 30 ml - 5%", "chaser_black_5"),
        ("Elix 30 ml", "elix_30"),
        ("Elix 10 ml", "elix_10"),
    ]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=cb)]
            for text, cb in buttons
            if get_button_status(cb)
        ]
        + [[InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]]
    )
    return kb


def generate_hqd_kb():
    buttons = [
        ("Lost Mary OS 12000", "lost_mary"),
    ]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=cb)]
            for text, cb in buttons
            if get_button_status(cb)
        ]
        + [[InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]]
    )
    return kb


def generate_pod_kb():
    buttons = [
        ("Xros Pro", "xros_pro"),
        ("Xros 4 mini", "xros_4_mini"),
        ("Xros 3 mini", "xros_3_mini"),
        ("Xros mini", "xros_mini"),
        ("Minican 4+", "minican_4"),
        ("Elf X", "elf_x"),
    ]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=cb)]
            for text, cb in buttons
            if get_button_status(cb)
        ]
        + [[InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]]
    )
    return kb


def generate_snus_kb():
    buttons = [
        ("Cuba 150 mg", "cuba_150"),
        ("Cuba 40 mg", "cuba_40"),
    ]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=cb)]
            for text, cb in buttons
            if get_button_status(cb)
        ]
        + [[InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]]
    )
    return kb


# Клавиатура финальная
final_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        # Надо больше жидкостей
        [
            InlineKeyboardButton(
                text="🛒 Оформить заказ", url="https://t.me/time_for_money1"
            )
        ],
        [InlineKeyboardButton(text="🏬 Шоп", url="https://t.me/Breeze_Store_MDV")],
        [
            InlineKeyboardButton(
                text="💫 Напиши отзывы", url="https://t.me/Breeze_feedback"
            )
        ],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")],
    ]
)
