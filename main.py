import re
import shutil
import os
import json
from extract_data import extract_data
from extract_line_item import extract_line_items_from_pages
from header_data import extract_invoice_details
from excelCreate import createExcel
import time
import pandas as pd
from finalTest1 import create_sap_connection,sap_one_creation  
    



inputPath = r"C:\Users\hp\Downloads\SAP po 1\SAP po 1\input"


# for file in os.listdir(inputPath):
#     filePath = os.path.join(inputPath, file)
#     outPutFile = os.path.join(os.path.dirname(__file__), "result.json")
    
#     print("Extraction Boat Started....................... ")
#     if not os.path.exists(outPutFile):
#         fileName = os.path.basename(filePath) 
#         data = extract_data(filePath)
#         print(data)
#         #print("Extraction Bot Started....................... ")
        
#         print(os.path.exists(outPutFile))
#         print("file exists")
#         with open(outPutFile,'w+') as fl:
#             json.dump(data, fl, indent=4)
#     # /===================================
    
#     data = []
#     import csv

#     with open(r'C:\Users\hp\Downloads\SAP po 1\SAP po 1\aws\output\Contract_Agreement-pdf-page-15-tables.csv', mode='r', encoding='utf-8') as infile:
        
#         reader = csv.reader(infile)

#         for row in reader:
#             if len(row) == 0:
#                 pass
#             else:
#                 print(row)
#                 data.append({"SAP Managerial Positions":[]})
                
                
#             # if all(cell.strip() for cell in row):  # Keep only rows without empty cells
                

# ---------------------------------------------

result,session = create_sap_connection('ECQ [10.22.22.23]') # you can also run only finaltest1.py file for sap
sap_one_creation(result,session)   # you can also run only finaltest1.py file for sap

    

     

    
