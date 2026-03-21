from abc import ABC, abstractmethod


class IUserRepository(ABC):

    @abstractmethod
    def add_user(self, username: str):
        pass

    @abstractmethod
    def get_user(self, user_id: int):
        pass


class IChatRepository(ABC):

    @abstractmethod
    def create_chat(self, name: str):
        pass

    @abstractmethod
    def get_chat(self, chat_id: int):
        pass


class IMessageRepository(ABC):

    @abstractmethod
    def save_message(self, text: str, user_id: int, chat_id: int):
        pass

    @abstractmethod
    def get_chat_messages(self, chat_id: int):
        pass