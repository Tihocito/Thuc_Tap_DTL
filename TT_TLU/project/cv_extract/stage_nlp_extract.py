def extract_structured_data(parsed: dict) -> dict:
    """
    NLP đơn giản – bạn có thể nâng cấp sau
    """
    return {
        "full_text": parsed.get("raw_text", ""),
        "lines": parsed.get("lines", [])
    }
