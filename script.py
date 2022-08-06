from aiogram import Bot, types, Dispatcher, executor
from py3pin.Pinterest import Pinterest
from auth_data import *
import random
import asyncio
import pprint

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

    # urls = random.sample(pictures,3)
    return pictures

print(len(to_send()))

def getBoardIds(username):
    
    pinterest = Pinterest(email='mafek@mail.ru',
                    password='Qwerty123++',
                    username='mafek0001',
                    cred_root='cred_root')

    dictBoards = {}
    boards = pinterest.boards(username=username)
    for board in boards:
        dictBoards[board['name']] = board['id']
    return dictBoards

print(getBoardIds(username = 'mafek0001'))

if __name__ == '__main__':
    pass
