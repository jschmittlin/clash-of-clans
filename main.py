import logging
import time

from utils.window import WindowInterface
from utils.control_mouse import (
    mouse_attack,
    mouse_find_now,
    mouse_select_troop,
    mouse_place_troop,
    mouse_surrender,
    mouse_okay,
    mouse_return_home,
    mouse_zoom_in_out,
    mouse_charrette,
    mouse_recuperer,
    mouse_x,
    mouse_zoom_out,
    is_searching_for_oppenent
)


def script_int_mdo(x: int, y: int) -> None:
    for _x in range(x):
        logging.info(f"Loop {_x+1}/{x}")
        for _y in range(y):
            logging.info(f"Attack {_y+1}/{y}")
            mouse_attack("attaquer.png")
            time.sleep(.1)
            mouse_find_now("trouver.png")
            while True:
                if is_searching_for_oppenent():
                    logging.debug("Searching for opponent...")
                else:
                    logging.debug("Opponent found!")
                    time.sleep(2.5)
                    break
                time.sleep(1)
            mouse_select_troop("bb_dragon.png")
            mouse_place_troop()                                 # TODO: Find better position to place troop
            time.sleep(.2)
            mouse_surrender("capituler.png")
            time.sleep(.1)
            mouse_okay("ok.png")
            time.sleep(.2)
            mouse_return_home("rentrer.png")
            time.sleep(2.5)
        
        mouse_zoom_in_out("or.png", "attaquer.png")
        mouse_charrette()                                       # TODO: Add position with images
        time.sleep(.1)
        mouse_recuperer("recuperer.png")
        mouse_x("x.png")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='[{asctime}] [{levelname:<8}] {name}: {message}', 
        style='{',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    attacks_input: str = input("Enter the number of attacks: ")
    loops_input: str = input("Enter the number of loops: ")
    
    try:
        attacks_input = int(attacks_input)
        loops_input = int(loops_input)
    except ValueError:
        logging.error("Invalid input: must be an integer")
        exit(1)
    
    WindowInterface("Clash of Clans").move_and_resize()
    script_int_mdo(loops_input, attacks_input)