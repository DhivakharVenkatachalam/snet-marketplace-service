class Wallet:
    def __init__(self, address, type, private_key=None, status=None):
        self.__address = address
        self.__private_key = private_key
        self.__status = status
        self.__type = type

    def get_wallet(self):
        return {"address": self.__address, "private_key": self.__private_key, "status": self.__status,
                "type": self.__type}