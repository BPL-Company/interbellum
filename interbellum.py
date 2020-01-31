import config
from modules.botutil import BotUtil

bot = BotUtil(config.token, config.creator)

from pymongo import MongoClient

db = MongoClient(config.db).interbellum
games = db.games
countries = db.countries

from modules.mongohelper import MongoHelper

db_helper = MongoHelper(MongoClient(config.db))


@bot.message_handler(commands=['start'])
def start_handler(m):
    if not m.text.count(' ') and m.chat.type == 'private':
        bot.send_message(m.from_user.id, 'Бот для игры в Интербеллум. Выступите в роли лидера целой державы.')
        return


@bot.message_handler(commands=['newgame'])
def newgame_handler(m):
    db_helper.create_game(m.chat.id, m.from_user.id)
    bot.send_message(m.chat.id, 'Игра создана!')


@bot.message_handler(commands=['game_info'])
def game_info_handler(m):
    bot.send_message(m.chat.id, db_helper.game_info(m.chat.id), parse_mode='HTML')


@bot.message_handler(commands=['delgame'])
def delgame_handler(m):
    game = db_helper.find_game(m.chat.id)
    if not m.from_user.id == game['admin']:
        bot.reply_to(m, 'Может только админ.')
        return
    db_helper.delete_game(game)
    bot.reply_to(m, 'Игра удалена.')
