import csv
import os
import pandas as pd

from utils import colors
from log import Logging


log_instance = Logging()
log = log_instance.get_logger()


class FileStorage:
    def save_in_csv(self, data, filename='data/startup100.csv'): # hardcoded, have to change later
        try:
            current_file = os.path.isfile(filename)
            #append mode
            with open(filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
            
                if not current_file:
                    # Write the header (optional, depending on your data)
                    writer.writerow(["Company", "Data"])
                
                # Iterate over the dictionary and write each company's data
                for company_name, row_data in data.items():
                    filtered_row = row_data[1:]
                    writer.writerow([company_name] + filtered_row)
                
                self.clean_csv(filename)
                self.count_rows(filename)  
                
        except Exception as e:
            log.error(f"File error: {e}")
            print("Error: File storage\n")  
            
            
    def clean_csv(self, filename='../data/startup100.csv'): #hardcoded, needs change
        unique_data = []  # To store unique rows
        seen = set()  # To track company names (or entire rows) we have already seen

        # Read the file
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Assume first row is header

            unique_data.append(header)  # Keep the header

            # Iterate through each row
            for row in reader:
                company_name = row[0]  # Assuming first column is the company name

                if company_name not in seen:  # Check if we've already seen this company
                    seen.add(company_name)  # Mark this company as seen
                    unique_data.append(row)  # Add the row to unique data

        # Overwrite the file with only unique rows
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(unique_data)

        print(f"\n{colors.bcolors.OKBLUE}Duplicate rows removed.")
     
                
    def count_rows(self, filename):
        # needs expectation handling
         number_rows = pd.read_csv(filename)
         
         print(f'{colors.bcolors.OKBLUE}-' * 30)
         print(f"{colors.bcolors.OKBLUE}current number of rows: {len(number_rows) - 1}\n")