import json
import os
import asyncio
import time
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.markdown import hbold, hlink
from main import collect_data


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    # start_buttons = ['🔪Ножи', '🧤Перчатки', '🔫Снайперские винтовки']
    kb = [
        [types.KeyboardButton(text='🔪Ножи')],
        [types.KeyboardButton(text='🧤Перчатки')],
        [types.KeyboardButton(text='🔫Снайперские винтовки')]
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)

    await message.answer('Выберите категорию', reply_markup=keyboard)


@dp.message(F.text == '🔪Ножи')
async def get_discount_knives(message: types.Message):
    await message.answer('Подождите, Ваш запрос обрабатывается...')
    collect_data(cat_type=2)

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("item_price")} 🔥'

        if index % 20 == 0:
            time.sleep(7)

        await message.answer(card)


@dp.message(F.text == '🔫Снайперские винтовки')
async def get_discount_guns(message: types.Message):
    await message.answer('Подождите, Ваш запрос обрабатывается...')
    collect_data(cat_type=4)

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("item_price")} 🔥'

        if index % 20 == 0:
            time.sleep(7)

        await message.answer(card)


@dp.message(F.text == '🧤Перчатки')
async def get_discount_gloves(message: types.Message):
    await message.answer('Подождите, Ваш запрос обрабатывается...')
    collect_data(cat_type=13)

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("item_price")} 🔥'

        if index % 20 == 0:
            time.sleep(7)

        await message.answer(card)


async def main():
    bot = Bot(token=os.getenv('TOKEN'),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
