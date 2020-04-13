import camelot
tables = camelot.read_pdf('data.pdf',flavor='stream',pages="2")
print(tables)
data = tables[0].df