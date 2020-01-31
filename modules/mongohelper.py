from modules.botutil import BotUtil


class MongoHelper:

    def __init__(self, client):
        self.__client = client
        self.__games = client.interbellum.games

    def create_game(self, chat_id, game_admin):
        commit = {
            'id': chat_id,
            'admin': game_admin,
            'players': {}
        }
        self.__games.insert_one(commit)

    def delete_game(self, chat_id):
        self.__games.delete_one({'id': chat_id})

    def find_game(self, chat_id):
        return self.__games.find_one({'id': chat_id})

    def game_info(self, chat_id):
        game = self.find_game(chat_id)
        return 'Айди игры: {}\n' \
               'Админ игры: {}'.format(game['id'], BotUtil.get_link('Админ', game['admin']))
