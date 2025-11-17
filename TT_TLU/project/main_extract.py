import os
from cv_extract.stage_preprocess_cv import preprocess_image
from cv_extract.stage_ocr_runner import run_ocr
from cv_extract.stage_parse_cv import parse_cv
from cv_extract.stage_nlp_extract import extract_structured_data
from cv_extract.stage_export_cv import export_results
from cv_extract.stage_pdf_to_images import pdf_to_images


def process_image_file(image_path):
    print(f"\nProcessing file: {image_path}")

    # 1. Preprocess
    clean_img = preprocess_image(image_path)

    # 2. OCR
    text = run_ocr(clean_img)

    # 3. Parse
    parsed = parse_cv(image_path)

    # 4. NLP
    data = extract_structured_data(parsed)

    data["file_name"] = os.path.basename(image_path)
    data["ocr_text"] = text

    return data


def collect_image_files(path):
    if os.path.isfile(path):
        ext = os.path.splitext(path)[1].lower()

        if ext in [".png", ".jpg", ".jpeg", ".bmp"]:
            return [path]

        if ext == ".pdf":
            print("📄 PDF detected → converting to images...")
            return pdf_to_images(path)

        print(f"❌ Unsupported file: {ext}")
        return []

    if os.path.isdir(path):
        all_files = []
        for file in os.listdir(path):
            fpath = os.path.join(path, file)
            ext = os.path.splitext(file)[1].lower()

            if ext in [".png", ".jpg", ".jpeg", ".bmp"]:
                all_files.append(fpath)
            elif ext == ".pdf":
                imgs = pdf_to_images(fpath)
                all_files.extend(imgs)

        return all_files

    return []


def main():
    print("=== CV Extraction Tool ===")
    path = input("Enter path to image or folder: ").strip().strip('"')

    image_files = collect_image_files(path)

    if not image_files:
        print("❌ No valid image or PDF files found.")
        return

    print(f"\nFound {len(image_files)} files to process.")

    results = []

    for img in image_files:
        try:
            data = process_image_file(img)
            results.append(data)
        except Exception as e:
            print(f"⚠️ Error processing {img}: {e}")

    export_results(results)

    print("\n✅ DONE! Saved to:")
    print(" → output/cv_extracted.json")
    print(" → output/cv_extracted.csv")


if __name__ == "__main__":
    main()
