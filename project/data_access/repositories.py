from .interfaces import IUserRepository, IChatRepository, IMessageRepository
from .database import SessionLocal
from .orm_models import UserORM, ChatORM, MessageORM


class UserRepository(IUserRepository):

    def add_user(self, username: str):
        session = SessionLocal()

        user = UserORM(
            username=username,
            is_registered=1
        )

        session.add(user)
        session.commit()
        session.close()

        return user

    def get_user(self, user_id: int):
        session = SessionLocal()

        user = session.query(UserORM).filter(UserORM.id == user_id).first()

        session.close()

        return user


class ChatRepository(IChatRepository):

    def create_chat(self, name: str):
        session = SessionLocal()

        chat = ChatORM(name=name)

        session.add(chat)
        session.commit()
        session.close()

        return chat

    def get_chat(self, chat_id: int):
        session = SessionLocal()

        chat = session.query(ChatORM).filter(ChatORM.id == chat_id).first()

        session.close()

        return chat


class MessageRepository(IMessageRepository):

    def save_message(self, text: str, user_id: int, chat_id: int):

        session = SessionLocal()

        message = MessageORM(
            text=text,
            user_id=user_id,
            chat_id=chat_id
        )

        session.add(message)
        session.commit()
        session.close()

        return message

    def get_chat_messages(self, chat_id: int):

        session = SessionLocal()

        messages = session.query(MessageORM)\
            .filter(MessageORM.chat_id == chat_id)\
            .all()

        session.close()

        return messages