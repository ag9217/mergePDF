#! python3
#mergePDF.py - combines all PDFs from the directories given in arguments
import PyPDF2, sys, os, time

# Get all the PDF filenames
pdfFiles = []
if len(sys.argv) < 2: #If no arguments/directories are given
    print('Usage: python mergePDF.py pdfdir1 pdfdir2 ..')
    time.sleep(3)
    sys.exit()

for directory in sys.argv[1:]: #Looking at each directory specified in arguments
    for files in os.listdir(directory): #Looking at each file in directory
        if files.endswith('.pdf'):
            pdfFiles.append(files) #Add pdf to list of pdfs to combine
pdfFiles.sort(key = str.lower) #list sorted in alphabetical order

#Object created to hold the combined PDF pages
pdfWriter = PyPDF2.PdfFileWriter()

#Loop through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) #reading PDF into variable

    #Loop through all the pages (except the first) and add them.
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#Save the resulting PDF to a file
pdfOutput = open('merged.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
