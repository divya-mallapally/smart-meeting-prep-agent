"""Extracts text from user-uploaded PDF and TXT files.

How it works:
- TXT files are decoded directly as UTF-8 text.
- PDF files are opened with pypdf, which reads each page's text layer
  (the invisible text stored inside the PDF) page by page.
- Extracted text is returned as one combined string, truncated to a safe
  maximum length so the prompt never exceeds the model's context window.

The extracted text is NOT saved to disk. It lives only in Streamlit's
session memory and is passed straight into the AI prompt.
"""

import io

from pypdf import PdfReader

# Roughly 100,000 characters of document text is plenty for meeting prep
# and keeps us safely inside Gemini's context window.
MAX_TOTAL_CHARS = 100_000
MAX_PER_FILE_CHARS = 40_000


def extract_text_from_txt(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="replace")


def extract_text_from_pdf(file_bytes: bytes) -> str:
    reader = PdfReader(io.BytesIO(file_bytes))
    pages = []
    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        pages.append(f"[Page {page_number}]\n{page_text.strip()}")
    return "\n\n".join(pages)


def extract_text(uploaded_file) -> str:
    """Extract text from one Streamlit UploadedFile (PDF or TXT)."""
    name = uploaded_file.name.lower()
    file_bytes = uploaded_file.getvalue()

    if name.endswith(".pdf"):
        try:
            text = extract_text_from_pdf(file_bytes)
        except Exception as exc:
            return f"[ERROR: Could not read '{uploaded_file.name}'. It may be a scanned/image PDF or corrupted file. Details: {exc}]"
    elif name.endswith(".txt"):
        text = extract_text_from_txt(file_bytes)
    else:
        return f"[ERROR: Unsupported file type '{uploaded_file.name}'. Only PDF and TXT are supported.]"

    if not text.strip():
        return f"[NOTE: '{uploaded_file.name}' contained no extractable text. It may be a scanned PDF — try a text-based PDF instead.]"

    return text[:MAX_PER_FILE_CHARS]


def process_uploaded_files(uploaded_files) -> str:
    """Combine text from all uploaded files into one labelled block."""
    if not uploaded_files:
        return ""

    blocks = []
    total = 0
    for uploaded_file in uploaded_files:
        text = extract_text(uploaded_file)
        header = f"--- DOCUMENT: {uploaded_file.name} ---"
        allowed = min(len(text), MAX_TOTAL_CHARS - total)
        if allowed <= 0:
            blocks.append(f"{header}\n[Skipped: total document limit reached.]")
            continue
        blocks.append(f"{header}\n{text[:allowed]}")
        total += allowed

    return "\n\n".join(blocks)
