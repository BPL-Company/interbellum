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
