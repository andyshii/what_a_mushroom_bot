from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from config import TOKEN
from function import predict_models

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.first_name

    await message.answer(f'Привет, {user_name}! Я помогу тебе собрать вкусные грибы и не принести домой поганок!')

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Чтобы я тебе помог\n ты должен прислать мне фотографию")

@dp.message_handler(content_types=['text'])
async def text_message(message: types.Message):
    await message.answer("Чтобы я помог, мне нужна фотография")

@dp.message_handler(content_types=['photo'])
async def photo_message(message: types.Message):
    list_name_photo = os.listdir('input_photo')
    if len(list_name_photo) == 0:
        name = '0'
        await message.photo[-1].download(f'input_photo/{name}.jpg', make_dirs=False)
        text = predict_models(f'input_photo/{name}.jpg')
        #await bot.send_photo(chat_id=message.chat.id, photo=types.InputFile(f'input_photo/{name}.jpg')) # присылает фото обратно
        await message.answer(text)
    else:
        next_name = int(list_name_photo[-1].split('.')[0]) + 1
        await message.photo[-1].download(f'input_photo/{next_name}.jpg', make_dirs=False)
        #await bot.send_photo(chat_id=message.chat.id, photo=types.InputFile(f'input_photo/{next_name}.jpg')) # присылает фото обратно
        text = predict_models(f'input_photo/{next_name}.jpg')
        await message.answer(f'Поздравляю! Это: \n {text}')

# команда запуска бота
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)