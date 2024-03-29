import pandas as pd

class CalculationHistoryManager:
    def __init__(self, history_file):
        self.history_file = history_file
        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        self.load_history()

    def load_history(self):
        try:
            self.history = pd.read_csv(self.history_file)
        except FileNotFoundError:
            pass

    def save_history(self):
        self.history.to_csv(self.history_file, index=False)

    def add_to_history(self, expression, result):
        self.history = self.history.append({'Expression': expression, 'Result': result}, ignore_index=True)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        self.save_history()

    def delete_history_record(self, index):
        self.history.drop(index, inplace=True)
        self.save_history()

    def show_history(self):
        print(self.history)

if __name__ == "__main__":
    history_manager = CalculationHistoryManager('history.csv')
    history_manager.add_to_history('2 + 2', 4)
    history_manager.save_history()
    history_manager.show_history()
