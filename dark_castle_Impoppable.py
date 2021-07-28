from pyautogui import *
import pyautogui
import time
from time import sleep
import keyboard
import numpy
import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

overtime = 0

path = "pictures\\levelup.png"
victory_path = "pictures\\victory.png"
defeat_path = "pictures\\defeat.png"
menu_path = "pictures\\menu.png"
event_path = "pictures\\event.png"
obyn_hero_path = "pictures\\obyn.png"
next_path = "pictures\\next.png"

monkeys = {
    "DART": "Q",
    "BOOMERANG": "W",
    "BOMB": "E",
    "TACK": "R",
    "ICE": "T",
    "GLUE": "Y",
    "SNIPER": "Z",
    "SUBMARINE": "X",
    "BUCCANEER": "C",
    "ACE": "V",
    "HELI": "B",
    "MORTAR": "N",
    "DARTLING": "M",
    "WIZARD": "A",
    "SUPER": "S",
    "NINJA": "D",
    "ALCHEMIST": "F",
    "DRUID": "G",
    "BANANA": "H",
    "ENGINEER": "L",
    "SPIKE": "J",
    "VILLAGE": "K",
    "HERO": "U"
}

button_positions = {  # Creates a dictionary of all positions needed for monkeys (positions mapped to 2160 x 1440 resolution)
    "HOME_MENU_START": [842, 936],
    "EXPERT_SELECTION": [1333, 978],
    "RIGHT_ARROW_SELECTION": [1644, 436],
    "DARK_CASTLE": [960, 260],  # ORIGINAL 720, 350 || winspy 960, 260
    "HARD_MODE": [1300, 400],
    "IMPOPPABLE_GAME_MODE": [1285, 736],
    "OVERWRITE_SAVE": [1140, 730],
    "TEMP_DART_MONKEY_1_LOCATION": [740, 664],
    "TEMP_DART_MONKEY_2_LOCATION": [810, 662],
    "SUBMARINE_1_LOCATION": [1094, 701],
    "HERO_LOCATION": [883, 665],
    "CAMO_DART_MONKEY_LOCATION": [740, 664],
    "BANANA_FARM_1_LOCATION": [986, 1005],
    "ALCHEMIST_LOCATION": [1025, 845],
    "SPIKE_FACTORY_LOCATION": [1525, 561],
    "BANANA_FARM_2_LOCATION": [817, 1001],
    "SUBMARINE_2_LOCATION": [1183, 696],
    "VILLAGE_LOCATION": [1005, 758],
    "BANANA_FARM_3_LOCATION": [973, 81],
    "BANANA_FARM_4_LOCATION": [803, 79],
    "SUBMARINE_3_LOCATION": [1105, 772],
    "SUBMARINE_4_LOCATION": [1190, 771],
    "SUBMARINE_5_LOCATION": [1253, 725],
    "SUBMARINE_6_LOCATION": [1100, 846],
    "SUBMARINE_6_LOCATION": [1190, 842],
    "VICTORY_CONTINUE": [962, 911],
    "VICTORY_HOME": [793, 851],  # 790, 850
    "EVENT_COLLECTION": [959, 683],  # 960 ,910
    "F_LEFT_INSTA": [651, 542],
    "F_RIGHT_INSTA": [1260, 542],
    "LEFT_INSTA": [805, 544],
    "RIGHT_INSTA": [1109, 543],
    "MID_INSTA": [957, 545],
    "EVENT_CONTINUE": [960, 998],
    "EVENT_EXIT": [75, 80],
    "QUIT_HOME": [845, 851],
    "XP_TOWER_1": [651, 129],
    "XP_TOWER_2": [815, 212],
    "HERO_SELECT": [599, 954],
    "SELECT_OBYN": [747, 972],
    "CONFIRM_HERO": [641, 670]
}


def click(location):
    pyautogui.click(button_positions[location])
    sleep(0.5)


def move_mouse(location):
    pyautogui.moveTo(location)
    time.sleep(0.5)


def press_key(key):
    pyautogui.press(key)
    time.sleep(0.5)


def menu_check():
    while True:  # Not doing anything until menu screen is open
        menu_on = pyautogui.locateOnScreen(menu_path, grayscale=True, confidence=0.9)
        if menu_on != None:
            print(f'{Fore.RED}Menu screen found. Continuing...')
            break
        else:
            print(f'{Fore.GREEN}Menu screen not found. Trying again...')
            sleep(2)


def hero_obyn_check():

    menu_check()

    print(f'{Fore.CYAN}Checking for OBYN...')
    found = pyautogui.locateOnScreen(obyn_hero_path, grayscale=True, confidence=0.9)

    if found == None:
        print(f'{Fore.CYAN}Not found. Selecting OBYN...')
        click("HERO_SELECT")
        click("SELECT_OBYN")
        click("CONFIRM_HERO")
        press_key("esc")
        print(f'{Fore.CYAN}OBYN selected.')


def place_tower(tower, location):

    Level_Up_Check(1)
    print(f'{Fore.CYAN}Placing ' + tower + '...')
    move_mouse(button_positions[location])
    press_key(monkeys[tower])
    pyautogui.click()
    print(f'{Fore.CYAN}' + tower + ' placed.')
    sleep(0.5)


def upgrade_tower(path, location):

    Level_Up_Check(1)
    print(f'{Fore.CYAN}Upgrading tower path ' + path + '...')
    click(location)
    press_key(path)
    time.sleep(1)
    press_key("esc")
    print(f'{Fore.CYAN}Path ' + path + ' upgraded.')
    sleep(0.5)


def Level_Up_Check(seconds):

    global overtime
    overtime = 0

    t_end = time.time() + seconds

    while time.time() < t_end:
        found = pyautogui.locateOnScreen(path, grayscale=True, confidence=0.9)

        if found != None:
            print(f'{Fore.RED}Level Up notification detected. Getting rid of it...')
            click("LEFT_INSTA")  # Accept lvl
            time.sleep(1)
            click("LEFT_INSTA")  # Accept knoledge
            time.sleep(1)
            '''
            click("LEFT_INSTA")  # unlock insta
            time.sleep(1)
            click("LEFT_INSTA")  # collect insta
            time.sleep(1)

            click("MID_INSTA")  # unlock insta
            time.sleep(1)
            click("MID_INSTA")  # collect insta
            time.sleep(1)

            click("RIGHT_INSTA")  # unlock r insta
            time.sleep(1)
            click("RIGHT_INSTA")  # collect r insta
            time.sleep(2)
            press_key("esc")
            sleep(0.5)
            '''
            press_key("space")  # Start the game
            print(f'{Fore.GREEN}Notification kyssed.')
        else:
            sleep(0.2)

    overtime = time.time() - t_end


def event_check():

    found = pyautogui.locateOnScreen(event_path, grayscale=True, confidence=0.9)

    if found != None:
        print(f"{Fore.RED}Event notification detected. Getting rid of it...")
        click("EVENT_COLLECTION")  # DUE TO EVENT:
        time.sleep(1)
        click("LEFT_INSTA")  # unlock insta
        time.sleep(1)
        click("LEFT_INSTA")  # collect insta
        time.sleep(1)
        click("RIGHT_INSTA")  # unlock r insta
        time.sleep(1)
        click("RIGHT_INSTA")  # collect r insta
        time.sleep(1)
        click("F_LEFT_INSTA")
        time.sleep(1)
        click("F_LEFT_INSTA")
        time.sleep(1)
        click("MID_INSTA")  # unlock insta
        time.sleep(1)
        click("MID_INSTA")  # collect insta
        time.sleep(1)
        click("F_RIGHT_INSTA")
        time.sleep(1)
        click("F_RIGHT_INSTA")
        time.sleep(1)

        time.sleep(1)
        click("EVENT_CONTINUE")

        # awe try to click 3 quick times to get out of the event mode, but also if event mode not triggered, to open and close profile quick
        click("EVENT_EXIT")
        print(f'{Fore.GREEN}Event notification kyssed.')
        time.sleep(1)


def Start_Select_Map():
    menu_check()
    print(f'{Fore.CYAN}Selecting map...')
    click("HOME_MENU_START")  # Move Mouse and click from Home Menu, Start
    click("EXPERT_SELECTION")  # Move Mouse to expert and click
    click("RIGHT_ARROW_SELECTION")  # Move Mouse to arrow and click
    click("DARK_CASTLE")  # Move Mouse to Dark Castle
    click("HARD_MODE")  # Move Mouse to select easy mode
    click("IMPOPPABLE_GAME_MODE")  # Move mouse to select Standard mode
    click("OVERWRITE_SAVE")  # Move mouse to overwrite save if exists
    print(f'{Fore.CYAN}Map selected.')


def Main_Game():

    sleep(2)

    print(f'{Fore.CYAN}Game started.')

    place_tower("HERO", "HERO_LOCATION")

    press_key("space")  # Start the game
    press_key("space")  # Fast forward the game

    Level_Up_Check(20 - overtime)
    place_tower("SUBMARINE", "SUBMARINE_1_LOCATION")  # 8.5
    Level_Up_Check(8.5 - overtime)
    upgrade_tower('1', "SUBMARINE_LOCATION")  # 18
    Level_Up_Check(18 - overtime)
    upgrade_tower('3', "SUBMARINE_LOCATION")  # 45
    Level_Up_Check(45 - overtime)
    upgrade_tower('3', "SUBMARINE_LOCATION")  # 24
    Level_Up_Check(24 - overtime)
    upgrade_tower('1', "SUBMARINE_LOCATION")  # 15
    Level_Up_Check(15 - overtime)
    place_tower("NINJA", "NINJA_LOCATION")  # 11.5
    Level_Up_Check(11.5 - overtime)
    upgrade_tower('1', "NINJA_LOCATION")  # 11.5
    Level_Up_Check(11.5 - overtime)
    upgrade_tower('1', "NINJA_LOCATION")  # 4
    Level_Up_Check(4 - overtime)
    upgrade_tower('3', "NINJA_LOCATION")  # 12
    Level_Up_Check(12 - overtime)
    upgrade_tower('1', "NINJA_LOCATION")  # 23
    Level_Up_Check(23 - overtime)
    upgrade_tower('3', "SUBMARINE_LOCATION")  # 39
    Level_Up_Check(39 - overtime)
    upgrade_tower('3', "SUBMARINE_LOCATION")  # 40
    Level_Up_Check(20 - overtime)
    upgrade_tower('1', "NINJA_LOCATION")
    Level_Up_Check(20 - overtime)


def Exit_Game():

    Level_Up_Check(1)

    found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=0.9)

    while found == None:
        sleep(2)
        print('Next button not found.')
        found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=0.9)

    print(f'{Fore.CYAN}Game ended. Going back to homescreen...')
    pyautogui.click(x=960, y=910)
    time.sleep(2)
    pyautogui.click(x=790, y=850)
    time.sleep(6)
    print(f'{Fore.CYAN}Back in homescreen. Checking for event notification...')
    event_check()
    sleep(2)
    tries = 0
    for x in range(0, 4):  # checking for menu screen
        menu_on = pyautogui.locateOnScreen(menu_path, grayscale=True, confidence=0.9)
        if menu_on != None:
            print(f'{Fore.CYAN}Menu screen found. Continuing...')
            break
        else:
            click("EVENT_EXIT")
            sleep(3)

# Main


print(f'{Fore.CYAN}Starting in 5 seconds... move to BTD6 homescreen.')
sleep(5)
hero_obyn_check()
print(f'{Fore.CYAN}Starting loop.')
while True:
    Start_Select_Map()
    Main_Game()
    Exit_Game()
