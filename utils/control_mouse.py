from typing import Tuple, Dict

import logging
import numpy as np
import cv2
import requests

from pyautogui import (
    click,
    mouseUp,
    scroll,
    moveTo,
    locateCenterOnScreen,
    screenshot,
)

w: int = 1335
h: int = 750

position_cache: Dict[str, Tuple[int, int]] = {}
base_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/"

def get_image(image: str) -> bool:
    response = requests.get(base_url + image)
    if response.status_code == 200:
        with open(image, 'wb') as file:
            file.write(response.content)
        return True
    return False

def get_position(image: str) -> Tuple[int, int] | None:
    if image in position_cache:
        return position_cache[image]
    if get_image(image):
        logging.debug(f"Image {image} downloaded")
    try:
        if position := locateCenterOnScreen(image, confidence=.8):
            logging.debug(f"Position of {image}: {position}")
            position_cache[image] = position
            return position
        else:
            logging.warning(f"Position of {image} not found")
            return None
        return position
    except Exception as error:
        logging.error(f"Error while getting position of {image}: {error}")
        return None

def is_searching_for_oppenent() -> bool:
    screenshot_np: np.ndarray = np.array(screenshot(region=(0, 0, w, h)))
    gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    mean_intensity = np.mean(gray)
    threshold = 100
    return mean_intensity >= threshold
    
def mouse_attack(image: str) -> None:
    click(get_position(image) or (75, 710))
    mouseUp()
    
def mouse_find_now(image: str) -> None:
    click(get_position(image) or (995, 525))
    mouseUp()
    
def mouse_select_troop(image: str) -> None:
    click(get_position(image) or (325, 720))
    mouseUp()

def mouse_place_troop(image: str) -> None:
    if position := get_position(image):
        position += (0, -150)
    click(position or (325, 570))
    mouseUp()
    
def mouse_surrender(image: str) -> None:
    click(get_position(image) or (75, 580))
    mouseUp()

def mouse_okay(image: str) -> None:
    click(get_position(image) or (790, 495))
    mouseUp()
    
def mouse_return_home(image: str) -> None:
    click(get_position(image) or (670, 665))
    mouseUp()

def mouse_zoom_in_out(image_in: str, image_out: str) -> None:
    moveTo(get_position(image_out) or (70, 700))
    for i in range(15): scroll(-1000)
    moveTo(get_position(image_in) or (1300, 70))
    for i in range(15): scroll(1000)
    moveTo(get_position(image_out) or (70, 700))
    for i in range(15): scroll(-1000)

def mouse_charrette() -> None:
    click(810, 370)
    mouseUp()

def mouse_recuperer(image: str) -> None:
    click(get_position(image) or (1000, 500))
    mouseUp()
    
def mouse_x(image: str) -> None:
    click(get_position(image) or (1000, 500))
    mouseUp()

def mouse_zoom_out() -> None:
    position: Tuple[int, int] = (w // 2, h // 2)
    moveTo(position)
    for i in range(15): scroll(-1000)