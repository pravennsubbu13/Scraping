import PyPDF2
import test
class scrape:
    def __init__(self,path):
        self.path=path
    
    def name_search(self):
        m=test.check_nam()
    
    def Reg_no_search(self):
        r=test.check_uno()

    def stirpe(self):
        with open(path,'rb') as pdf_reader:
            pdf_reader=PyPDF2.PdfFileReader(pdf_reader)
            
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)

                page_text = page.extract_text()

                if a in page_text:
                    lines=page_text.split('\n')

                    for line in lines:
                        if a in line:
                            print(line)


