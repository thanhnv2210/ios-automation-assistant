import cv2
import numpy as np

def find_image(screen_path, template_path, threshold=0.8):
    screen = cv2.imread(screen_path)
    template = cv2.imread(template_path)
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    if len(loc[0]) > 0:
        y, x = loc[0][0], loc[1][0]
        h, w, _ = template.shape
        return x + w // 2, y + h // 2
    return None