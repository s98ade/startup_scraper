import csv
import json
import os
import pandas as pd

from utils.colors import bcolors
from log import Logging


log_instance = Logging()
log = log_instance.get_logger()


class FileStorage:
    def __init__(self):
        self.csv_filename = 'data/startup100.csv'# hardcoded, have to change later
        self.json_filename = 'data/startup100.json'# hardcoded, have to change later
         
    
    def save_in_csv(self, data):
        try:
            current_file = os.path.isfile(self.csv_filename)
            
            with open(self.csv_filename, mode='a', newline='', encoding='utf-8') as file: #append mode
                writer = csv.writer(file)
            
                if not current_file:
                    writer.writerow([
                        "Company", "S100 Index", "Category", "Founding Year", 
                        "Location", "Funding", "Revenue", "Business ID"
                    ])# Write the header (optional, depending on your data)

                for company_data in data.values():# Iterate over the dictionary and write each company's data
                    writer.writerow(company_data.values())
                
                print(f'{bcolors.OKGREEN}\nData retrieved successfully.\nData stored in ../data/startup100.csv\n')         
        except Exception as e:
            log.error(f"{bcolors.FAIL}File error: {e}")
            print(f"{bcolors.FAIL}Error: File storage\n") 
            
        
    def save_in_json(self, data):
        try:
            if os.path.exists(self.json_filename):
                with open(self.json_filename, 'r', encoding='utf-8') as file:
                    try:
                        existing_data = json.load(file)
                    except json.JSONDecodeError:
                        existing_data = []  # Handle case where file is empty or invalid
            else:
                existing_data = []

            existing_data.append(data)

            with open(self.json_filename, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)        
        except Exception as e:
            log.error(f"{bcolors.FAIL}File error: {e}")
            print(f"{bcolors.FAIL}Error: JSON storage\n") 
            
            
    def clean_csv(self):
        unique_data = [] 
        seen = set()  # To track company names (or entire rows) we have already seen

        with open(self.csv_filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Assume first row is header

            unique_data.append(header)  # Keep the header

            for row in reader:
                company_name = row[0]  # Assuming first column is the company name

                if company_name not in seen:  # Check if we've already seen this company
                    seen.add(company_name)  # Mark this company as seen
                    unique_data.append(row)  # Add the row to unique data

        with open(self.csv_filename, mode='w', newline='', encoding='utf-8') as file:# Overwrite the file with only unique rows
            writer = csv.writer(file)
            writer.writerows(unique_data)

        print(f"\n{bcolors.OKBLUE}Duplicate rows removed.")
        
    
    """ def clean_json(self, unique_key='Business ID'):
        try:
            with open(self.json_filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

            seen = {}# Dictionary to track unique entries
            unique_data = []

            for entry in data:
                unique_id = entry.get(unique_key)

                if unique_id and unique_id not in seen:
                    seen[unique_id] = entry
                    unique_data.append(entry)

            with open(self.json_filename, 'w', encoding='utf-8') as file:
                json.dump(unique_data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            log.error(f"{bcolors.FAIL}Error cleaning JSON file: {e}")
            print(f"{bcolors.FAIL}Error cleaning JSON file.\n")  """
     
                
    def count_rows(self):
        # needs expectation handling
         number_rows = pd.read_csv(self.csv_filename)
         
         print(f'{bcolors.OKBLUE}-' * 30)
         print(f"{bcolors.OKBLUE}current number of rows: {len(number_rows) - 1}\n")