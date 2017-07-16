import textract
import os


input_dir = input("Enter a directory: ")
for root, dirs, filenames in os.walk(input_dir):
    for f in filenames:
        if f.endswith(".pdf"):
            filename = os.path.join(root, f)
            text = textract.process(filename, method='pdftotext', layout=True)
            with open(filename.replace(".pdf", ".txt"), "w") as text_file:
                print(text.decode("utf-8"), file=text_file)