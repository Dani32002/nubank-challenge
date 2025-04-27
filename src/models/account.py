from .transaction import Transaction

class Account():

    def __init__(self, active: bool, available_limit: int, history: list[Transaction]) -> None:
        self.__active: bool = active
        self.__available_limit: int = available_limit
        self.__history: list[Transaction] = history

    @property
    def active(self) -> bool:
        return self.__active
    
    @property
    def available_limit(self) -> int:
        return self.__available_limit
    
    @property
    def history(self) -> list[Transaction]:
        return self.__history
    
    @active.setter
    def active(self, active: bool) -> None:
        self.__active = active

    @available_limit.setter
    def available_limit(self, available_limit: int) -> None:
        self.__available_limit = available_limit

    @history.setter
    def history(self, history: list[Transaction]) -> None:
        self.__history = history

    def __str__(self) -> str:
        return f'Account(active = {self.__active}, available_limit = {self.__available_limit}, history = {[str(t) for t in self.__history]})'