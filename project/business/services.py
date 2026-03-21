import csv
from .models import User, Chat, Message


class ChatService:

    def __init__(self, user_repo, chat_repo, message_repo):
        """
        Dependency Injection:
        сюди передаються репозиторії
        """
        self.user_repo = user_repo
        self.chat_repo = chat_repo
        self.message_repo = message_repo

    def register_user(self, username: str):

        user = User(username)

        return self.user_repo.add_user(user.username)

    def create_chat(self, name: str):

        chat = Chat(name)

        return self.chat_repo.create_chat(chat.name)

    def send_message(self, text: str, user_id: int, chat_id: int):

        message = Message(text, user_id, chat_id)

        return self.message_repo.save_message(
            message.text,
            message.user_id,
            message.chat_id
        )

    def get_chat_history(self, chat_id: int):

        return self.message_repo.get_chat_messages(chat_id)

    def load_messages_from_csv(self, file_path):

        """
        Зчитує CSV файл і записує дані у БД
        """

        with open(file_path, newline='', encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                text = row["text"]
                user_id = int(row["user_id"])
                chat_id = int(row["chat_id"])

                self.send_message(text, user_id, chat_id)