
from PyPDF2 import PdfReader



# Open PDF file
with open('CAT_EXAM.pdf', 'rb') as file:
    # Create reader object
    reader = PdfReader(file)

    # Get number of pages
    print(len(reader.pages))

    # Read first page
    page = reader.pages[-1]

    # Extract text
    text = page.extract_text()

    # print(text)