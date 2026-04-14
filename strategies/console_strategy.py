from .base_strategy import OutputStrategy

class ConsoleStrategy(OutputStrategy):

    def output(self, data):
        for item in data:
            print(item)