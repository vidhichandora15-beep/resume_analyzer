# PDF files ko read karne ke liye PyMuPDF import karna
import fitz

# Resume PDF se text extract karne ka function
def extract_resume_text(pdf_file):

    # Uploaded PDF ka data read karna
    pdf_data = pdf_file.read()

    # PDF ko memory se open karna
    document = fitz.open(
        stream=pdf_data,
        filetype="pdf"
    )

    # Resume ka text store karne ke liye empty string
    resume_text = ""

    # PDF ke har page ko read karna
    for page in document:

        # Har page ka text collect karna
        resume_text = resume_text + page.get_text()

    # PDF document close karna
    document.close()

    # Extracted text return karna
    return resume_text
