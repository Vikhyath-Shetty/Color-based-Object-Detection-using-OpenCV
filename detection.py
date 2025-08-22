import logging
import cv2 as cv
import cv2.typing as cvt
import numpy as np
from config import COLOR_RANGES
from type import green, red, blue

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")

# Create a mask for the red color


def create_red_mask(frame: cvt.MatLike) -> cvt.MatLike:
    red_range = COLOR_RANGES["red"]
    red_mask_1 = cv.inRange(frame, red_range[0][0], red_range[0][1])
    red_mask_2 = cv.inRange(frame, red_range[1][0], red_range[1][1])
    red_mask = cv.bitwise_or(red_mask_1, red_mask_2)
    return red_mask

# Create a mask for other colors


def create_other_mask(frame: cvt.MatLike, color: str) -> cvt.MatLike:
    color_range = COLOR_RANGES[color]
    mask = cv.inRange(frame, color_range[0][0], color_range[0][1])
    return mask

# Function to create a mask


def create_mask(frame: cvt.MatLike, color: set | str) -> cvt.MatLike | None:
    mask = None
    for col in color:
        if col == "red":
            temp_mask = create_red_mask(frame)
        else:
            temp_mask = create_other_mask(frame, col)
        mask = temp_mask if mask is None else cv.bitwise_or(
            mask, temp_mask)
    return mask

# Function to perform morphological operations and get contours


def get_contours(mask: cvt.MatLike):
    kernal = np.ones((5, 5), np.uint8)
    morphed_mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
    contours, _ = cv.findContours(
        morphed_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    return contours


# Function to detect objects
def detect_object(cam_src: int | str, color: set | str, n: int) -> None:
    cap = cv.VideoCapture(cam_src)
    if not cap.isOpened():
        raise RuntimeError("Cannot open video source")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                logging.warning("Failed to read frame")
                continue
            hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            mask = create_mask(hsv_frame, color)
            if mask is None:
                logging.warning("Failed to create mask")
                continue
            contours = get_contours(mask)
            if contours:
                selected_contours = sorted(
                    contours, key=cv.contourArea, reverse=True)[:min(n, len(contours))]
                for con in selected_contours:
                    x, y, w, h = cv.boundingRect(con)
                    cv.rectangle(frame, (x, y), (x + w, y + h), green, 2)
            cv.imshow('Contours', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv.destroyAllWindows()
