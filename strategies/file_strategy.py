from .base_strategy import OutputStrategy

class FileStrategy(OutputStrategy):

    def output(self, data):
        with open("output/result.txt", "w", encoding="utf-8") as f:
            for item in data:
                f.write(str(item) + "\n")