from usecase import UseCase
from databases import MySqlRepository

class MySqlFactory:

    @staticmethod
    def create() -> UseCase:
        return UseCase(MySqlRepository())