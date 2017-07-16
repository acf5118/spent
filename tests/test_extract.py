import textract

filename = input("Enter a filename: ")
outfile = input ("Enter an output filename: ")
text = textract.process(filename, method='pdftotext', layout=True)
with open(outfile, "w") as text_file:
    print(text.decode("utf-8"), file=text_file)