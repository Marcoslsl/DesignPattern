from abc import ABC, abstractmethod

class DataBaseInterface(ABC):

    @abstractmethod
    def select_one(self):
        pass