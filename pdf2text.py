import fitz  # this is pymupdf

filepath='path'
# Generate text from article PDF
with fitz.open(filepath) as doc:
    text = ""
    for page in doc:
        text += page.get_text()
