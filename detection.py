import logging
import cv2 as cv
import numpy as np
from config import COLOR_RANGES

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")


def create_red_mask(frame: np.ndarray) -> np.ndarray:
    red_range = COLOR_RANGES["red"]
    red_mask_1 = cv.inRange(frame, red_range[0][0], red_range[0][1])
    red_mask_2 = cv.inRange(frame, red_range[1][0], red_range[1][1])
    red_mask = cv.bitwise_or(red_mask_1, red_mask_2)
    return red_mask


def create_other_mask(frame: np.ndarray, color: str ) -> np.ndarray:
    color_range = COLOR_RANGES[color]
    mask = cv.inRange(frame, color_range[0][0],color_range[0][1])
    return mask


def create_mask(frame: np.ndarray, color: set | str) -> np.ndarray | None:
    mask = None
    if isinstance(color, str):
        if str == "red":
            mask = create_red_mask(frame)
        else:
            mask = create_other_mask(frame, color)
    else:
        for col in color:
            if col == "red":
                temp_mask = create_red_mask(frame)
            else:
                temp_mask = create_other_mask(frame, col)
                mask = temp_mask if mask is None else cv.bitwise_or(
                    mask, temp_mask)
    return mask


def detect_object(cam_src: int | str, color: set | str) -> None:
    cap = cv.VideoCapture(cam_src)
    if not cap.isOpened():
        raise RuntimeError("Cannot open video source")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                logging.warning("Failed to open the camera source")
                continue
            hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            mask = create_mask(hsv_frame, color)
            # result = cv.bitwise_and(frame,frame,mask=mask)
            cv.imshow("Object Detection",mask)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv.destroyAllWindows()


