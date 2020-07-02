import PyPDF2

book = 'oshengBook.pdf'
readBook = PyPDF2.PdfFileReader(book)
page = readBook.getPage(1)
pageContent = page.extractText()

print(pageContent)
# for word in pageContent.split('.'):
#   print(word)
