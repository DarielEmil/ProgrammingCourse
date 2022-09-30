import PyPDF2

pdfObject = open('ejemploPDF.pdf', 'rb') #WARNING: This is to open the PDF

pdfReader = PyPDF2.PdfFileReader(pdfObject) #NOTE: Assigning to another variable the pdfObject

# pagePDF = pdfReader.getPage(0) #NOTE: This get an specific page
# print(pagePDF.extractText()) #NOTE: To extractText

#WARNING: This is descrypting PDFs

pdfEncryptedReader = PyPDF2.PdfFileReader(open('ejemploPDF.pdf','rb'))

# print(pdfEncryptedReader.isEncrypted) #NOTE: To check if this is encrypted

#TODO: To descrypting the pdf is needed decrypt and its needed to pass a password, if the password is not correct will return an error

#WARNING: Creating PDFs



