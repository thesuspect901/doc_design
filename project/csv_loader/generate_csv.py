import csv
import random
import os


OUTPUT_FILE = "data/messages.csv"


def generate_csv(rows=1000):

    os.makedirs("data", exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # заголовки
        writer.writerow(["user_id", "chat_id", "text"])

        for i in range(rows):

            user_id = random.randint(1, 20)
            chat_id = random.randint(1, 5)

            text = f"Message number {i}"

            writer.writerow([user_id, chat_id, text])


if __name__ == "__main__":

    generate_csv(1000)

    print("CSV файл створено: data/messages.csv")