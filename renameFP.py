import pdfplumber
import pandas as pd
import os
import csv

pathToPdfs = os.getcwd()+"/dropPdfHere/"


def printText(list_of_texts):
    counter = 0
    for text in list_of_texts:
        print(counter)
        print(text)
        counter += 1

def reformatMonth(month):
    if month == "Januari" or month == "January":
        month = '01'
    elif month == "Februari" or month == "February":
        month = '02'
    elif month == "Maret" or month == "March":
        month = '03'
    elif month == "April":
        month = '04'
    elif month == "Mei" or month == "May":
        month = '05'
    elif month == "Juni" or month == "June":
        month = '06'
    elif month == "Juli" or month == "July":
        month = '07'
    elif month == "Agustus" or month == "August":
        month = '08'
    elif month == "September":
        month = '09'
    elif month == "Oktober" or month == "October":
        month = '10'
    elif month == "Nopember" or month == "November":
        month = '11'
    elif month == "Desember" or month == "December":
        month = '12'
    return month

for _, _, files in os.walk(pathToPdfs):
    for filename in files:
        if '.pdf' in filename:
            print ("Renaming " + filename)
            
            pdf = pdfplumber.open(pathToPdfs + filename)
            page = pdf.pages[0] # get the page
            texts = page.extract_text()
            list_of_texts = texts.split('\n')
            
            month = reformatMonth(list_of_texts[26].split(', ')[-1].split(' ')[1])
            invoice_number = list_of_texts[28].replace('/','-')
            entity = list_of_texts[8].split(': ')[-1]
            tax_invoice_number = list_of_texts[1].split(': ')[-1]

            # printText(list_of_texts)
            old_file_directory = pathToPdfs + filename
            new_name = month + '_' + invoice_number + '_' + entity + '_' + tax_invoice_number+'.pdf'
            new_file_directory = pathToPdfs + new_name

            pdf.close()
            
            os.rename(old_file_directory, new_file_directory)
            print ("Success! " + filename + " has been renamed to " + new_name)