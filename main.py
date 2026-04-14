from data.loader import load_data

from strategies.console_strategy import ConsoleStrategy
from strategies.file_strategy import FileStrategy
from strategies.kafka_strategy import KafkaStrategy
from strategies.redis_strategy import RedisStrategy


def get_strategy():
    print("\nОберіть тип виводу:")
    print("1 - Console")
    print("2 - File")
    print("3 - Kafka")
    print("4 - Redis")

    choice = input("Ваш вибір: ")

    if choice == "1":
        return ConsoleStrategy()
    elif choice == "2":
        return FileStrategy()
    elif choice == "3":
        return KafkaStrategy()
    elif choice == "4":
        return RedisStrategy()
    else:
        print("❌ Невірний вибір")
        return get_strategy()


def main():
    data = load_data()
    strategy = get_strategy()

    print("\n🔄 Виконується...\n")

    strategy.output(data)

    print("\n✅ Готово!")


if __name__ == "__main__":
    main()