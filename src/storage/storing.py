import csv

class FileStorage:
    def save_in_csv(self, data, filename='../data/startup100.csv'): # hardcoded, have to change later
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)