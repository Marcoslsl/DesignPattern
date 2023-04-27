from interface import DataBaseInterface
from typing import Type, Dict, Union

class UseCase:

    def __init__(self, repository: Type[DataBaseInterface]) -> None:
        self.__repository = repository
        
    def do_something(self, data: bool) -> Union[Dict, None]:
        if data is True:
            repository_response = self.__repository.select_one()
            return repository_response
        
        return None