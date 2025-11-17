import cv2
from cv_extract.stage_preprocess_cv import preprocess_image_for_ocr
from cv_extract.stage_ocr_runner import get_text_from_image_data


def parse_cv_text(ocr_text: str) -> dict:
    """
    Tách thông tin text đơn giản (placeholder)
    """
    lines = ocr_text.split("\n")
    return {
        "raw_text": ocr_text,
        "lines": lines
    }


def parse_cv(file_path: str) -> dict:
    """
    Pipeline parse file: preprocess → OCR → text → parse
    """
    temp_path = preprocess_image_for_ocr(file_path)
    img = cv2.imread(temp_path)

    raw = get_text_from_image_data(img)
    parsed = parse_cv_text(raw)

    return parsed
