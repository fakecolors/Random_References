from aiogram import Bot, types, Dispatcher, executor
from py3pin.Pinterest import Pinterest
from auth_data import *
import random

bot = Bot(token=token)
dp = Dispatcher(bot)

def to_send():

    pinterest = Pinterest(email='mafek@mail.ru',
                        password='Qwerty123++',
                        username='mafek0001',
                        cred_root='cred_root')


    def get_board_pins_batched(board_id='644296359130839700'):
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

async def on_startup(dispatcher):
    media = types.MediaGroup()
    for item in to_send():
        media.attach_photo(item)
    await bot.send_media_group(chat_id, media)

if __name__ == '__main__':
    # print(type(to_send()))
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
