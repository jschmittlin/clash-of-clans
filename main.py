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

NB_LOOPS: int = 1
NB_ATTACKS: int = 10

attaquer_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/attaquer.png"
trouver_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/trouver.png"
bb_dragon_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/bb_dragon.png"
capituler_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/capituler.png"
ok_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/ok.png"
rentrer_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/renter.png"
or_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/or.png"
recuperer_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/recuperer.png"
x_url: str = "https://raw.githubusercontent.com/jschmittlin/clash-of-clans/main/data/images/x.png"

def script_int_mdo(x: int = NB_LOOPS, y: int = NB_ATTACKS) -> None:
    for _x in range(x):
        logging.info(f"Loop {_x+1}/{NB_LOOPS}")
        for _y in range(y):
            logging.info(f"Attack {_y+1}/{NB_ATTACKS}")
            mouse_attack(attaquer_url)
            time.sleep(.1)
            mouse_find_now(trouver_url)
            while True:
                if is_searching_for_oppenent():
                    logging.debug("Searching for opponent...")
                else:
                    logging.debug("Opponent found!")
                    time.sleep(2.5)
                    break
                time.sleep(1)
            mouse_select_troop(bb_dragon_url)
            mouse_place_troop(bb_dragon_url)        # TODO: Find better position to place troop
            time.sleep(.1)
            mouse_surrender(capituler_url)
            time.sleep(.1)
            mouse_okay(ok_url)
            time.sleep(.2)
            mouse_return_home(rentrer_url)
            time.sleep(2.5)
        
        mouse_zoom_in_out(or_url, attaquer_url)
        mouse_charrette()                           # TODO: Add position with images
        time.sleep(.1)
        mouse_recuperer(recuperer_url)
        mouse_x(x_url)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
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