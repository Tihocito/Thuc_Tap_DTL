from paddleocr import PaddleOCR

ocr_instance = PaddleOCR(lang="en", use_textline_orientation=True)


def get_text_from_image_data(image_data):
    try:
        result = ocr_instance.ocr(image_data, cls=True)
        if not result or not result[0]:
            return ""
        lines = []
        for line in result[0]:
            txt, score = line[1]
            if score is None or score >= 0.3:
                lines.append(txt)
        return "\n".join(lines)
    except Exception as e:
        print(f"[ocr_runner] OCR error: {e}")
        return ""


def run_ocr(image_path: str) -> str:
    """
    Nhận đường dẫn ảnh → trả về text OCR
    """
    from PIL import Image
    import numpy as np

    try:
        img = Image.open(image_path)
        img_np = np.array(img)
        return get_text_from_image_data(img_np)

    except Exception as e:
        print(f"[run_ocr] Cannot read {image_path}: {e}")
        return ""
