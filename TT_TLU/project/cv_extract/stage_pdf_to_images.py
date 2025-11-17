import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_path):
    doc = fitz.open(pdf_path)

    out_folder = os.path.join(os.path.dirname(pdf_path), "pdf_images")
    os.makedirs(out_folder, exist_ok=True)

    output_paths = []

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        pix = page.get_pixmap(dpi=200)

        out_path = os.path.join(out_folder, f"page_{page_index + 1}.png")
        pix.save(out_path)
        output_paths.append(out_path)

    return output_paths
