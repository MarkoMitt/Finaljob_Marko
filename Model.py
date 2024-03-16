import csv


class Model:
    def __init__(self):
        self.data = None
        self.header = None

    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            self.header = next(reader)
            self.data = list(reader)

    def search(self, result):
        found_results = []
        for row in self.data:
            for item in row:
                if result.lower() in item.lower():
                    found_results.append(row)
                    break
        return found_results
