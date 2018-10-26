# importing required modules 
import PyPDF2 
  
path ='/Users/martinodonnell/Documents/Software/Scouts/files/test1.pdf'
# creating a pdf file object 
pdfFileObj = open(path, 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 

for x in range(pdfReader.numPages):
# creating a page object 
    pageObj = pdfReader.getPage(x)
    # extracting text from page 
    print(pageObj.extractText()) 
    print('-----New Page-----')
# closing the pdf file object 
pdfFileObj.close() 