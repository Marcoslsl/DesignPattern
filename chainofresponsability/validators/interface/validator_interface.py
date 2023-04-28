from abc import ABC, abstractmethod

class ValidatorInterface(ABC):

    @abstractmethod
    def validate(self):
        pass
    
    @abstractmethod
    def action(self):
        pass

