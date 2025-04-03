import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF resume."""
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"
    return text
