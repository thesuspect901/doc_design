from datetime import datetime


class User:

    def __init__(self, username: str):
        self.username = username
        self.is_registered = True


class Chat:

    def __init__(self, name: str):
        self.name = name
        self.members = []


class Message:

    def __init__(self, text: str, user_id: int, chat_id: int):
        self.text = text
        self.user_id = user_id
        self.chat_id = chat_id
        self.timestamp = datetime.now()