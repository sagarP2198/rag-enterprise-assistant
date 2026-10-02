import pymupdf  # pymupdf
import docx
from pathlib import Path


def extract_text_from_pdf(file_path: str) -> str:
    """Extract all text from a PDF file, page by page."""
    text = ""
    doc = pymupdf.open(file_path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


def extract_text_from_docx(file_path: str) -> str:
    """Extract all text from a Word document, paragraph by paragraph."""
    doc = docx.Document(file_path)
    return "\n".join(para.text for para in doc.paragraphs)


def extract_text_from_txt(file_path: str) -> str:
    """Read a plain text file directly."""
    return Path(file_path).read_text(encoding="utf-8")


def extract_text(file_path: str) -> str:
    """Route a file to the correct extractor based on its extension."""
    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".txt":
        return extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


if __name__ == "__main__":
    # Quick manual test — run this file directly to try it
    import sys
    if len(sys.argv) < 2:
        print("Usage: python ingestion/extract.py <path_to_file>")
    else:
        result = extract_text(sys.argv[1])
        print(result[:500])  # print first 500 chars as a preview