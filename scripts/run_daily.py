from src.driver import init_driver
from src.vision import find_image
import time

driver = init_driver()

def tap_image(image_name):
    driver.save_screenshot("screen.png")
    pos = find_image("screen.png", f"images/{image_name}")
    if pos:
        x, y = pos
        driver.tap([(x, y)])
        print(f"Tapped {image_name} at ({x}, {y})")
    else:
        print(f"{image_name} not found")

DAILY_TASKS = ["claim_button.png", "tower_button.png"]

for task in DAILY_TASKS:
    tap_image(task)
    time.sleep(5)
