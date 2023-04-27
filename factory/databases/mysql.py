from typing import Dict
from interface import DataBaseInterface

class MySqlRepository(DataBaseInterface):

    def select_one(self) -> Dict:
        return {
            "success": True,
            "data": "ola mundo"
        }