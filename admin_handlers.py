import json

from aiogram import Dispatcher, F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from button_state import set_button_status
from data import save_product_data
from handlers import product_data

# 👉 сюда впиши ID человека, которому доступна команда /update
ADMIN_IDS = [1365015496, 5768435511, 7281613540]  # замени на свой Telegram ID

router = Router()


@router.message(Command("update"))
async def update_product_text(message: types.Message, state: FSMContext):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ У тебя нет доступа.")
        return

    data = await state.get_data()
    product_key = data.get("current_product")

    if not product_key:
        await message.answer("⚠️ Сначала выбери товар через кнопки.")
        return

    text = message.text or ""  # если None, заменим на пустую строку
    parts = text.split(maxsplit=1)
    new_text = parts[1] if len(parts) > 1 else None
    photo = message.photo[-1].file_id if message.photo else None

    if product_key not in product_data:
        product_data[product_key] = {}

    if new_text:
        product_data[product_key]["text"] = new_text
    if photo:
        product_data[product_key]["photo"] = photo

    save_product_data(product_data)
    await message.answer(f"✅ Обновлено для {product_key}!")


@router.message(F.text.startswith("/off "))
async def off_button(message: Message):
    button = message.text.split("/off ")[1].strip()
    set_button_status(button, False)
    await message.answer(f"🔕 Кнопка {button} скрыта.")


@router.message(F.text.startswith("/on "))
async def on_button(message: Message):
    button = message.text.split("/on ")[1].strip()
    set_button_status(button, True)
    await message.answer(f"🔔 Кнопка {button} включена.")


# список ID админов


# Функция, которая загружает JSON файл с состоянием кнопок
def load_button_status():
    with open("buttons_status.json", "r", encoding="utf-8") as file:
        return json.load(file)


@router.message(Command("show"))
async def show_button_status(message: Message):
    # Проверяем, является ли пользователь админом
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ У вас нет прав для использования этой команды.")
    else:
        button_status = load_button_status()
        status_text = "Текущий статус кнопок:\n\n"

        # Формируем текст для вывода
        for key, value in button_status.items():
            status_text += f"{key}: {'✅' if value else '❌'}\n"

        await message.answer(status_text)


def register_admin_handlers(dp: Dispatcher):
    dp.include_router(router)
