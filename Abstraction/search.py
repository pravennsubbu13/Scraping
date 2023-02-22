import PyPDF2


with open('E:\scrape\Abstraction\pdfs\icici.pdf','rb') as pdf_file:
    
    f=open("write.txt","a")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
  
    for page_num in range(pdf_reader.numPages):
        
      
        page = pdf_reader.getPage(page_num)
        
     
        page_text = page.extractText()

        a=['Name of the Product','Tag Line','Policy Term','Payment Term','premium payment','Rs.','Period']
        #p='This benefit illustration is intended to show year-wise premiums payable and benefits under the policy'
        for i in range(len(a)):
            if a[i] in page_text:
                lines=page_text.split('\n')
                for line in lines:
                    if a[i] in line:
                        f.write(line+"\n")
                    else:
                        continue
            print("hello")

