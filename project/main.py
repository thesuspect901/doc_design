from data_access.database import init_db
from data_access.repositories import UserRepository, ChatRepository, MessageRepository
from business.services import ChatService


def main():

    # створення таблиць
    init_db()

    # створення репозиторіїв
    user_repo = UserRepository()
    chat_repo = ChatRepository()
    message_repo = MessageRepository()

    # Dependency Injection
    service = ChatService(
        user_repo,
        chat_repo,
        message_repo
    )

    # тестові користувачі
    service.register_user("Ruslan")
    service.register_user("Ivan")

    # тестовий чат
    service.create_chat("General")

    # завантаження CSV
    service.load_messages_from_csv("data/messages.csv")

    print("Дані успішно завантажені в SQLite")


if __name__ == "__main__":
    main()