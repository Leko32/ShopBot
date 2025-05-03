from aiogram import Dispatcher, F, Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from data import load_product_data
from keyboards import (
    final_kb,
    generate_assortiment_kb,
    generate_china_kb,
    generate_hqd_kb,
    generate_pod_kb,
    generate_russia_kb,
    generate_snus_kb,
    generate_uk_kb,
    main_menu_kb,
)

router = Router()


product_data = load_product_data()


class ProductState:
    current_product = "current_product"


product_sections = {
    "hqd": {"text": "HQD ассорт 😎", "kb": generate_hqd_kb},
    "pod_system": {"text": "Вот POD-системы 💨", "kb": generate_pod_kb},
    "snus": {"text": "Тут снюс 👊", "kb": generate_snus_kb},
    "uk_liquids": {"text": "UK жидкости 🇺🇦", "kb": generate_uk_kb},
    "china_liquids": {"text": "China вкусы 🇨🇳", "kb": generate_china_kb},
    "russia_liquids": {"text": "Russia жидкости 🇷🇺", "kb": generate_russia_kb},
}


text_start = (
    "⚜️Breeze — <b>лучшее что попадёт в твои лёгкие!</b>\n"
    'Бери топовые вкусы и забудь про "опять херня вкус".\n\n'
    "<b>🔰Что у нас крутого:</b>\n"
    "✅Только бомбовые миксы\n"
    "✅100% оригинал\n"
    "✅ Быстрый заказ без головняка\n"
    "✅ Молниеносная доставка\n"
    "✅ Плюшки и акции для своих\n\n"
    "💨Выбирай всё что по душе из ассортимента ниже🔥"
)

# Команда /start


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(text_start, reply_markup=main_menu_kb)


# ЖИДКОСТИ


@router.callback_query(F.data == "liquids")
async def show_liquids(callback: types.CallbackQuery):
    kb = generate_assortiment_kb()
    await callback.message.edit_text("Главное меню", reply_markup=kb)
    await callback.answer()


# ТУТ МЕНЯТЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬ
@router.callback_query(F.data.in_(product_sections.keys()))
async def show_product_section(callback: types.CallbackQuery, state: FSMContext):
    key = callback.data
    await state.update_data(current_product=key)

    section = product_sections.get(key)
    if section:
        # ВАЖНО: вызываем функцию, а не просто берём объект
        await callback.message.edit_text(section["text"], reply_markup=section["kb"]())
    else:
        await callback.message.edit_text("❌ Раздел не найден.")

    await callback.answer()


@router.callback_query(
    F.data.in_(
        [
            "flonq_30",
            "solana_30",
            "hqd_10",
            "hqd_30",
            "elfliq_10",
            "elfliq_30",
            "anarchia",
            "elix_10",
            "elix_30",
            "chaser_black_5",
            "chaser_lux_5",
            "chaser_black_6_5",
            "chaser_lux_6_5",
            "lost_mary",
            "elf_x",
            "minican_4",
            "xros_mini",
            "xros_3_mini",
            "xros_4_mini",
            "xros_pro",
            "cuba_40",
            "cuba_150",
        ]
    )
)
async def show_product(callback: types.CallbackQuery, state: FSMContext):
    key = callback.data
    await state.update_data(current_product=key)
    product = product_data.get(key, {})
    text = product.get("text", "❌ Товар не найден")
    photo = product.get("photo")

    if photo:
        media = types.InputMediaPhoto(media=photo, caption=text)
        await callback.message.edit_media(media=media, reply_markup=final_kb)
    else:
        await callback.message.edit_text(text, reply_markup=final_kb)

    await callback.answer()


# БЭКИ НАЗАД


@router.callback_query(F.data == "back_to_main")
async def show_main(callback: types.CallbackQuery):
    try:
        await callback.message.delete()
    except Exception as e:
        print("❌ Ошибка при удалении:", e)
    kb = generate_assortiment_kb()
    await callback.message.answer("Главное меню", reply_markup=kb)


def register_user_handlers(dp: Dispatcher):
    dp.include_router(router)
