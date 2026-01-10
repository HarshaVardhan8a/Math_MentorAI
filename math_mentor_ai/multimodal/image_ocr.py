import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image):
    """
    Performs OCR on uploaded image
    Returns extracted text + confidence score
    """

    img = Image.open(image).convert("RGB")
    img_np = np.array(img)

    results = reader.readtext(img_np)

    extracted_text = []
    confidences = []

    for bbox, text, conf in results:
        extracted_text.append(text)
        confidences.append(conf)

    if not extracted_text:
        return {
            "text": None,
            "confidence": 0.0
        }

    avg_confidence = sum(confidences) / len(confidences)

    return {
        "text": " ".join(extracted_text),
        "confidence": round(avg_confidence, 2)
    }
