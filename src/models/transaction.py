from datetime import datetime

class Transaction():

    def __init__(self, amount: int, merchant: str, time: datetime) -> None:
        self.__amount: int = amount
        self.__merchant: str = merchant
        self.__time: datetime = time

    @property
    def amount(self) -> int:
        return self.__amount
    
    @property
    def merchant(self) -> str:
        return self.__merchant
    
    @property
    def time(self) -> datetime:
        return self.__time
    
    @amount.setter
    def amount(self, amount: int) -> None:
        self.__amount = amount

    @merchant.setter
    def merchant(self, merchant: str) -> None:
        self.__merchant = merchant

    @time.setter
    def time(self, time: datetime) -> None:
        self.__time = time

    def __str__(self) -> str:
        return f'Transaction(amount = {self.__amount}, merchant = {self.__merchant}, time = {self.__time})'