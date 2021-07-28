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
# startround_path = "pictures\\startround.png"

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
    "DART_MONKEY_LOCATION": [740, 664],
    "SUBMARINE_1_LOCATION": [1094, 701],
    "HERO_LOCATION": [883, 665],
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
    "SUBMARINE_7_LOCATION": [1190, 842],
    "GLUE_MONKEY_1_LOCATION": [429, 295],
    "GLUE_MONKEY_2_LOCATION": [460, 794],
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
    "CONFIRM_HERO": [641, 670],
    "COLLECT_LEFT": [1390, 375],
    "COLLECT_RIGHT": [160, 370]
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


def Level_Up_Check_End(seconds):

    global overtime
    overtime = 0
    roundover = True

    t_end = time.time() + seconds

    while time.time() < t_end and roundover:
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

        """
        roundcheck = pyautogui.locateOnScreen(startround_path, grayscale=True, confidence=0.9)
        if roundcheck != None:
            roundover = False\
        """

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
    click("HARD_MODE")  # Move Mouse to select hard mode
    click("IMPOPPABLE_GAME_MODE")  # Move mouse to select Impoppable mode
    click("OVERWRITE_SAVE")  # Move mouse to overwrite save if exists
    print(f'{Fore.CYAN}Map selected.')


def Bank_Collection(position):
    click(position)
    click("COLLECT_LEFT")
    click(position)
    click("COLLECT_RIGHT")
    click(position)


def Null_Round(length):
    press_key("space")  # Start the round
    Level_Up_Check_End(length)


def Powers_Round(length):
    press_key("space")  # Start the round
    press_key("4") # Use Brambles
    press_key("5") # Use Wall of Trees
    Level_Up_Check_End(length)


def Null_Farming_Round(length, farm_position):
    press_key("space")  # Start the round
    move_mouse(button_positions[farm_position])
    Level_Up_Check_End(length)


def Powers_Farming_Round(length, farm_position):
    press_key("space")  # Start the round
    press_key("4") # Use Brambles
    press_key("5") # Use Wall of Trees
    move_mouse(button_positions[farm_position])
    Level_Up_Check_End(length)


def Round_100():
    press_key("space")  # Start the round
    press_key("4") # Use Brambles
    press_key("5") # Use Wall of Trees
    press_key("6") # Use CTA
    press_key("7") # Just in Case you have an extra for some reason
    Level_Up_Check_End(20)


def Main_Game():

    sleep(4)

    print(f'{Fore.YELLOW}Prepping Field.')
    click("EVENT_EXIT")
    place_tower("DART", "DART_MONKEY_LOCATION")
    place_tower("SUBMARINE", "SUBMARINE_1_LOCATION")
    
    press_key("space")  # Start the game
    print(f'{Fore.CYAN}Game started.')

    Null_Round(10) # Round 6
    Null_Round(12) # Round 7
    place_tower("HERO", "HERO_LOCATION")
    Null_Round(14) # Round 8
    Null_Round(11) # Round 9
    Null_Round(21) # Round 10
    upgrade_tower('3', "SUBMARINE_1_LOCATION") # Sub_1 001
    upgrade_tower('1', "SUBMARINE_1_LOCATION") # Sub_1 101
    Null_Round(10) # Round 11
    Null_Round(9) # Round 12
    Null_Round(15) # Round 13
    upgrade_tower('1', "SUBMARINE_1_LOCATION") # Sub_1 201
    Null_Round(13) # Round 14
    Null_Round(12) # Round 15
    Null_Round(8) # Round 16
    Null_Round(4) # Round 17
    Null_Round(13) # Round 18
    upgrade_tower('3', "SUBMARINE_1_LOCATION") # Sub_1 202
    Null_Round(8) # Round 19
    upgrade_tower('3', "DART_MONKEY_LOCATION") # Dart Monkey 001
    upgrade_tower('3', "DART_MONKEY_LOCATION") # Dart Monkey 002
    Null_Round(4) # Round 20
    Null_Round(9) # Round 21
    Null_Round(5) # Round 22
    Null_Round(5) # Round 23
    Null_Round(6) # Round 24
    upgrade_tower('3', "SUBMARINE_1_LOCATION") # Sub_1 203
    Null_Round(10) # Round 25
    Null_Round(8) # Round 26
    Null_Round(15) # Round 27
    place_tower("BANANA", "BANANA_FARM_1_LOCATION") 
    Null_Farming_Round(5, "BANANA_FARM_1_LOCATION") # Round 28
    Null_Farming_Round(8, "BANANA_FARM_1_LOCATION") # Round 29
    upgrade_tower('1', "BANANA_FARM_1_LOCATION") # farm_1 100
    Null_Farming_Round(8, "BANANA_FARM_1_LOCATION") # Round 30
    upgrade_tower('1', "BANANA_FARM_1_LOCATION") # farm_1 200
    Null_Farming_Round(8, "BANANA_FARM_1_LOCATION") # Round 31
    place_tower("ALCHEMIST", "ALCHEMIST_LOCATION")
    Null_Farming_Round(13, "BANANA_FARM_1_LOCATION") # Round 32
    upgrade_tower('1', "ALCHEMIST_LOCATION") # alch 100
    upgrade_tower('1', "ALCHEMIST_LOCATION") # alch 200
    Null_Farming_Round(12, "BANANA_FARM_1_LOCATION") # Round 33
    Null_Farming_Round(15, "BANANA_FARM_1_LOCATION") # Round 34
    upgrade_tower('1', "ALCHEMIST_LOCATION") # alch 300
    Null_Farming_Round(15, "BANANA_FARM_1_LOCATION") # Round 35
    upgrade_tower('3', "ALCHEMIST_LOCATION") # alch 301
    Null_Farming_Round(10, "BANANA_FARM_1_LOCATION") # Round 36
    Null_Farming_Round(19, "BANANA_FARM_1_LOCATION") # Round 37
    Null_Farming_Round(13, "BANANA_FARM_1_LOCATION") # Round 38
    upgrade_tower('3', "SUBMARINE_1_LOCATION") # Sub_1 204
    Null_Farming_Round(17, "BANANA_FARM_1_LOCATION") # Round 39
    upgrade_tower('2', "BANANA_FARM_1_LOCATION") # farm_1 210
    upgrade_tower('2', "BANANA_FARM_1_LOCATION") # farm_1 220
    place_tower("SPIKE", "SPIKE_FACTORY_LOCATION")
    Powers_Farming_Round(4, "BANANA_FARM_1_LOCATION") # Round 40
    Null_Farming_Round(20, "BANANA_FARM_1_LOCATION") # Round 41
    Null_Farming_Round(6, "BANANA_FARM_1_LOCATION") # Round 42
    upgrade_tower('1', "ALCHEMIST_LOCATION") # alch 401
    Null_Farming_Round(6, "BANANA_FARM_1_LOCATION") # Round 43
    Null_Farming_Round(11, "BANANA_FARM_1_LOCATION") # Round 44
    Null_Farming_Round(23, "BANANA_FARM_1_LOCATION") # Round 45
    upgrade_tower('2', "BANANA_FARM_1_LOCATION") # farm_1 230
    place_tower("BANANA", "BANANA_FARM_2_LOCATION")
    Null_Farming_Round(30, "BANANA_FARM_2_LOCATION") # Round 46
    upgrade_tower('1', "BANANA_FARM_2_LOCATION") # farm_2 100
    upgrade_tower('1', "BANANA_FARM_2_LOCATION") # farm_2 200
    Null_Farming_Round(30, "BANANA_FARM_2_LOCATION") # Round 47
    upgrade_tower('2', "BANANA_FARM_2_LOCATION") # farm_2 210
    upgrade_tower('2', "BANANA_FARM_2_LOCATION") # farm_2 220
    Null_Farming_Round(30, "BANANA_FARM_2_LOCATION") # Round 48
    Powers_Farming_Round(30, "BANANA_FARM_2_LOCATION") # Round 49
    upgrade_tower('2', "BANANA_FARM_2_LOCATION") # farm_2 230
    place_tower("SUBMARINE", "SUBMARINE_2_LOCATION")
    upgrade_tower('1', "SUBMARINE_2_LOCATION") # Sub_2 100
    upgrade_tower('1', "SUBMARINE_2_LOCATION") # Sub_2 200
    upgrade_tower('3', "SUBMARINE_2_LOCATION") # Sub_2 201
    upgrade_tower('3', "SUBMARINE_2_LOCATION") # Sub_2 202
    upgrade_tower('3', "SUBMARINE_2_LOCATION") # Sub_2 203
    Null_Round(30) # Round 50
    place_tower("VILLAGE", "VILLAGE_LOCATION")
    Null_Round(30) # Round 51
    upgrade_tower('1', "VILLAGE_LOCATION") # village 100
    upgrade_tower('1', "VILLAGE_LOCATION") # village 200
    Null_Round(30) # Round 52
    Null_Round(30) # Round 53
    Null_Round(30) # Round 54
    Null_Round(30) # Round 55
    Null_Round(30) # Round 56
    Null_Round(30) # Round 57
    Bank_Collection("BANANA_FARM_1_LOCATION")
    Null_Round(30) # Round 58
    Powers_Round(30) # Round 59
    Null_Round(30, "BANANA_FARM_3_LOCATION") # Round 60
    Null_Round(30, "BANANA_FARM_3_LOCATION") # Round 61
    Bank_Collection("BANANA_FARM_2_LOCATION")
    upgrade_tower('3', "SUBMARINE_1_LOCATION") # Sub_1 205
    upgrade_tower('3', "SUBMARINE_2_LOCATION") # Sub_2 204
    place_tower("BANANA", "BANANA_FARM_3_LOCATION")
    Null_Farming_Round(30, "BANANA_FARM_3_LOCATION") # Round 62
    upgrade_tower('1', "BANANA_FARM_3_LOCATION") # farm_3 100
    upgrade_tower('1', "BANANA_FARM_3_LOCATION") # farm_3 200
    upgrade_tower('2', "BANANA_FARM_3_LOCATION") # farm_3 210
    Powers_Farming_Round(30, "BANANA_FARM_3_LOCATION") # Round 63
    upgrade_tower('2', "BANANA_FARM_3_LOCATION") # farm_3 220
    Null_Farming_Round(30, "BANANA_FARM_3_LOCATION") # Round 64
    Null_Farming_Round(30, "BANANA_FARM_3_LOCATION") # Round 65
    upgrade_tower('2', "BANANA_FARM_3_LOCATION") # farm_3 230
    place_tower("BANANA", "BANANA_FARM_4_LOCATION")
    Null_Farming_Round(30, "BANANA_FARM_4_LOCATION") # Round 66
    upgrade_tower('1', "BANANA_FARM_4_LOCATION") # farm_4 100
    upgrade_tower('1', "BANANA_FARM_4_LOCATION") # farm_4 200
    upgrade_tower('2', "BANANA_FARM_4_LOCATION") # farm_4 210
    Null_Farming_Round(30, "BANANA_FARM_4_LOCATION") # Round 67
    upgrade_tower('2', "BANANA_FARM_4_LOCATION") # farm_4 220
    Null_Farming_Round(30, "BANANA_FARM_4_LOCATION") # Round 68
    Null_Farming_Round(30, "BANANA_FARM_4_LOCATION") # Round 69
    Bank_Collection("BANANA_FARM_1_LOCATION")
    upgrade_tower('2', "BANANA_FARM_4_LOCATION") # farm_4 230
    Null_Round(30) # Round 70
    Null_Round(30) # Round 71
    Null_Round(30) # Round 72
    Null_Round(30) # Round 73
    Bank_Collection("BANANA_FARM_2_LOCATION")
    Null_Round(30) # Round 74
    Null_Round(30) # Round 75
    Null_Round(30) # Round 76
    Null_Round(30) # Round 77
    Bank_Collection("BANANA_FARM_3_LOCATION")
    Null_Round(30) # Round 78
    Null_Round(30) # Round 79
    Powers_Round(30) # Round 80
    Null_Round(30) # Round 81
    Bank_Collection("BANANA_FARM_1_LOCATION")
    Bank_Collection("BANANA_FARM_4_LOCATION")
    upgrade_tower('1', "ALCHEMIST_LOCATION") # alch 501
    place_tower("SUBMARINE", "SUBMARINE_3_LOCATION")
    upgrade_tower('1', "SUBMARINE_3_LOCATION")
    upgrade_tower('1', "SUBMARINE_3_LOCATION")
    upgrade_tower('3', "SUBMARINE_3_LOCATION")
    upgrade_tower('3', "SUBMARINE_3_LOCATION")
    upgrade_tower('3', "SUBMARINE_3_LOCATION")
    upgrade_tower('3', "SUBMARINE_3_LOCATION")
    Powers_Round(30) # Round 82
    Null_Round(30) # Round 83
    place_tower("SUBMARINE", "SUBMARINE_4_LOCATION")
    upgrade_tower('1', "SUBMARINE_4_LOCATION")
    upgrade_tower('1', "SUBMARINE_4_LOCATION")
    upgrade_tower('3', "SUBMARINE_4_LOCATION")
    upgrade_tower('3', "SUBMARINE_4_LOCATION")
    upgrade_tower('3', "SUBMARINE_4_LOCATION")
    upgrade_tower('3', "SUBMARINE_4_LOCATION")
    Null_Round(30) # Round 84
    Null_Round(30) # Round 85
    Bank_Collection("BANANA_FARM_2_LOCATION")
    place_tower("SUBMARINE", "SUBMARINE_5_LOCATION")
    upgrade_tower('1', "SUBMARINE_5_LOCATION")
    upgrade_tower('1', "SUBMARINE_5_LOCATION")
    upgrade_tower('3', "SUBMARINE_5_LOCATION")
    upgrade_tower('3', "SUBMARINE_5_LOCATION")
    upgrade_tower('3', "SUBMARINE_5_LOCATION")
    upgrade_tower('3', "SUBMARINE_5_LOCATION")
    place_tower("SUBMARINE", "SUBMARINE_6_LOCATION")
    upgrade_tower('1', "SUBMARINE_6_LOCATION")
    upgrade_tower('1', "SUBMARINE_6_LOCATION")
    upgrade_tower('3', "SUBMARINE_6_LOCATION")
    upgrade_tower('3', "SUBMARINE_6_LOCATION")
    upgrade_tower('3', "SUBMARINE_6_LOCATION")
    upgrade_tower('3', "SUBMARINE_6_LOCATION")
    Null_Round(30) # Round 86
    Null_Round(30) # Round 87
    place_tower("SUBMARINE", "SUBMARINE_7_LOCATION")
    upgrade_tower('1', "SUBMARINE_7_LOCATION")
    upgrade_tower('1', "SUBMARINE_7_LOCATION")
    upgrade_tower('3', "SUBMARINE_7_LOCATION")
    upgrade_tower('3', "SUBMARINE_7_LOCATION")
    upgrade_tower('3', "SUBMARINE_7_LOCATION")
    upgrade_tower('3', "SUBMARINE_7_LOCATION")
    Null_Round(30) # Round 88
    Null_Round(30) # Round 89
    Bank_Collection("BANANA_FARM_3_LOCATION")
    upgrade_tower('2', "VILLAGE_LOCATION") # village 210
    upgrade_tower('2', "VILLAGE_LOCATION") # village 220
    upgrade_tower('2', "VILLAGE_LOCATION") # village 230
    Null_Round(30) # Round 90
    Null_Round(30) # Round 91
    Null_Round(30) # Round 92
    Null_Round(30) # Round 93
    Bank_Collection("BANANA_FARM_1_LOCATION")
    Bank_Collection("BANANA_FARM_4_LOCATION")
    upgrade_tower('2', "VILLAGE_LOCATION") # village 240
    Null_Round(30) # Round 94
    Null_Round(30) # Round 95
    place_tower("GLUE", "GLUE_MONKEY_1_LOCATION")
    upgrade_tower('2', "GLUE_MONKEY_1_LOCATION") # glue_1 010
    upgrade_tower('2', "GLUE_MONKEY_1_LOCATION") # glue_1 020
    upgrade_tower('3', "GLUE_MONKEY_1_LOCATION") # glue_1 021
    upgrade_tower('3', "GLUE_MONKEY_1_LOCATION") # glue_1 022
    upgrade_tower('3', "GLUE_MONKEY_1_LOCATION") # glue_1 023
    place_tower("GLUE", "GLUE_MONKEY_2_LOCATION")
    upgrade_tower('2', "GLUE_MONKEY_2_LOCATION") # glue_2 010
    upgrade_tower('2', "GLUE_MONKEY_2_LOCATION") # glue_2 020
    upgrade_tower('3', "GLUE_MONKEY_2_LOCATION") # glue_2 021
    upgrade_tower('3', "GLUE_MONKEY_2_LOCATION") # glue_2 022
    upgrade_tower('3', "GLUE_MONKEY_2_LOCATION") # glue_2 023
    Null_Round(30) # Round 96
    Null_Round(30) # Round 97
    Bank_Collection("BANANA_FARM_2_LOCATION")
    upgrade_tower('1', "SPIKE_FACTORY_LOCATION")
    upgrade_tower('1', "SPIKE_FACTORY_LOCATION")
    upgrade_tower('1', "SPIKE_FACTORY_LOCATION")
    upgrade_tower('1', "SPIKE_FACTORY_LOCATION")
    upgrade_tower('2', "SPIKE_FACTORY_LOCATION")
    upgrade_tower('2', "SPIKE_FACTORY_LOCATION") # spike factory to 420
    Null_Round(30) # Round 98
    Powers_Round(30) # Round 99
    Round_100()# Round 100
    



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
