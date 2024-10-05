import csv

class FileStorage:
    def save_in_csv(self, data, filename='../data/startup100.csv'): # hardcoded, have to change later
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write the header (optional, depending on your data)
            writer.writerow(["Company", "Data"])
            
            # Iterate over the dictionary and write each company's data
            for company_name, row_data in data.items():
                filtered_row = row_data[1:]
                writer.writerow([company_name] + filtered_row) 