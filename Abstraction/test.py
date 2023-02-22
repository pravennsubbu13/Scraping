import PyPDF2
import tabula
from pandas import *
import numpy as np

def check_nam():
    data=read_csv("output1.csv",encoding='cp1252')
    nam=data['Name'].tolist()
    for i in range(len(nam)):
        if '\r' in nam[i]:
            nam[i]=nam[i].replace('\r',' ')
    return nam
def check_uno():
    data=read_csv("output1.csv",encoding='cp1252')
    nam=data['Regn.No'].tolist()
    return nam

file='E:\scrape\Abstraction\pdfs\Loli.pdf'


'''with open('E:\scrape\Abstraction\pdfs\Loli.pdf','rb') as pdf_reader:
    pdf_reader=PyPDF2.PdfFileReader(pdf_reader)

    l=pdf_reader.numPages
    tabula.convert_into('E:\scrape\Abstraction\pdfs\Loli.pdf','output1.csv',output_format="csv",pages=1)'''
print(check_uno())