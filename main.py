from aiogram import Bot, types, Dispatcher, executor
from py3pin.Pinterest import Pinterest
from auth_data import *
import random
import asyncio
import aioschedule

bot = Bot(token=token)
dp = Dispatcher(bot)

def to_send(pin_id):

    pinterest = Pinterest(email='mafek@mail.ru',
                        password='Qwerty123++',
                        username='mafek0001',
                        cred_root='cred_root')

    def get_board_pins_batched(board_id=pin_id):
        board_feed = []
        feed_batch = pinterest.board_feed(board_id=board_id)
        while len(feed_batch) > 0:
            board_feed += feed_batch
            feed_batch = pinterest.board_feed(board_id=board_id)

        return board_feed

    pictures = []

    for item in get_board_pins_batched()[:-1]:
        url = item['images']['orig']['url']
        # print(data)
        pictures.append(url)

    urls = random.sample(pictures,3)
    return urls

async def send_message():
    media = types.MediaGroup()
    anatomy = to_send(pin_id = '644296359130839700')
    media.attach_photo(anatomy[0], '>>> Anatomy references')

    for item in anatomy[1:]:
        media.attach_photo(item)
    await bot.send_media_group(chat_id = References_ch, media = media)

    media = types.MediaGroup()
    anatomy = to_send(pin_id = '644296359130840117')
    media.attach_photo(anatomy[0], '>>> Style references')

    for item in anatomy[1:]:
        media.attach_photo(item)
    await bot.send_media_group(chat_id = References_ch, media = media)

async def scheduler():
    aioschedule.every(15).seconds.do(send_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(dispatcher):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)