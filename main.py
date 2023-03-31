from typing import Counter
from mss import mss
import pytesseract 
import torch
import cv2
import numpy as np
import time
import math
import os
import keyboard
import pyscreenshot as ImageGrab
import pyautogui
import threading
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageEnhance, ImageFilter

def heading():
    print(
    '''
    ██╗   ██╗ █████╗ ██╗      ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗     █████╗ ██╗
    ██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██║
    ██║   ██║███████║██║     ██║   ██║██████╔╝███████║██╔██╗ ██║   ██║       ███████║██║
    ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║       ██╔══██║██║
     ╚████╔╝ ██║  ██║███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║       ██║  ██║██║
      ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═╝╚═╝
     __  __           _        ______   __         _                                _        _  __ 
    |  \/  | __ _  __| | ___  | __ ) \ / /  _     / \   __ _ _   _  __ _ _ __      / \   ___(_)/ _|
    | |\/| |/ _` |/ _` |/ _ \ |  _  \ V /  (_)   / _ \ / _` | | | |/ _` | '_ \    / _ \ / __| | |_ 
    | |  | | (_| | (_| |  __/ | |_) || |    _   / ___ \ (_| | |_| | (_| | | | |  / ___ \|__ \ |  _|
    |_|  |_|\__,_|\__,_|\___| |____/ |_|   (_) /_/   \_\__,_|\__, |\__,_|_| |_| /_/   \_\___/_|_|  
                                                            |___/                                 
''')
    
def menu():
    os.system("cls")
    heading()
    print("\n This is the menu, choose as required.")
    print('''
[1] AI Helper
[2] Instant Reyna lock
[3] About the Economey Management
[4] About
[5] Instructions
          ''')
    ans2 = input("> ")
    if ans2 == "1":
        os.system('cls')
        aim_helper()
    elif ans2 == "2":
        os.system('cls')
        instalock_reyna()
    elif ans2 == "3":
        os.system('cls')
        ecoinfo()
        instalock_reyna()
    elif ans2 == "4":
        os.system('cls')
        about()
    elif ans2 == "5":
        os.system('cls')
        Instructions()
    else: 
        os.system('cls')
        menu()
        
def instalock_reyna():
    heading()
    print("- This place will instalock Reyna for you, as thats the only compatible agent with the Eco management.")
    while True:
        if keyboard.is_pressed('e') == True:
            menu()
            break
        try:
            x, y = pyautogui.locateCenterOnScreen("Assets\\reyna.png")
        except TypeError:
            print("Waiting for selection screen..\r".format(),end="")
        else:
            pyautogui.moveTo(x=x,y=y)
            pyautogui.click()
            pyautogui.click(x=954,y=809)
            os.system('cls')
            menu()

def about():
    heading()
    print('''
This is the about page!

- The program is made by Aayan Asif
- The program isn't a hacking tool
- The program is made for Personal project
- The program can only be used with the Agent Reyna
          
Press 'x' to go back.
          ''')
    back = input("> ")
    if back == "x":
        os.system('cls')
        menu()

def Instructions():
    heading()
    print('''
This is the Instructions page!

- To enable/disable aim assist, press ' ` ' (The tilde key)
- To close the program, press '=' (Equals key)
- To close the Instant Reyna Lock program, press 'e' 
- To go to the economy management, press 'b'
- When you will press 'b', there would be a box asking for some info, You have to answer it right!

Press 'x' to go back.
          ''')
    back = input("> ")
    if back == "x":
        os.system('cls')
        menu()

def ecoinfo():
    heading()
    print(''' 
Here you will find the info about how the economey is managed.  

If 800 and round 1 --> Revolver
If 800 and round > 1 --> Save
If <= 2000 --> Specter + Devour
If <= 3000 => 2000 --> Bulldog + Devour + Leer + light shield
If <= 4000 => 3000 --> Vandal + Devour + Leer(2) + light shield
If <= 5000 => 4000 --> Vandal + Devour + Leer(2) + Heavy shield
          
Press 'x' to go back.
          ''')
    back = input("> ")
    if back == "x":
        os.system('cls')
        menu()

def aim_helper():
    heading()
    print("----------------------------------IGNORE BELOW----------------------------------\n")
    def cooldown(cooldown_bool,wait):
        time.sleep(wait)
        cooldown_bool[0] = True

    MONITOR_WIDTH = 1920#game res
    MONITOR_HEIGHT = 1080#game res
    MONITOR_SCALE = 5#how much the screen shot is downsized by eg. 5 would be one fifth of the monitor dimensions
    region = (int(MONITOR_WIDTH/2-MONITOR_WIDTH/MONITOR_SCALE/2),int(MONITOR_HEIGHT/2-MONITOR_HEIGHT/MONITOR_SCALE/2),int(MONITOR_WIDTH/2+MONITOR_WIDTH/MONITOR_SCALE/2),int(MONITOR_HEIGHT/2+MONITOR_HEIGHT/MONITOR_SCALE/2))
    x,y,width,height = region
    screenshot_center = [int((width-x)/2),int((height-y)/2)]
    triggerbot = False
    triggerbot_toggle = [True]
    model = torch.hub.load(r'yolov5' , 'custom', path= r'best.pt',source='local')
    model.conf = 0.40
    model.maxdet = 10
    model.apm = True 
    model.classes = [1,2]

    print("\n----------------------------------IGNORE ABOVE----------------------------------\n")

    start_time = time.time()
    x = 1
    counter = 0
    avg_fps = 0
    fps_count = 0
    
    with mss() as stc:
        global eyes
        eyes = False
        q1 = input("Do you want to see the detections that aim assist makes? -- |THE FPS WOULD DECREASE| (yes(Y) or no(N)) : ")
        print("\n----------------------------------Program logs----------------------------------\n")
        if q1 == "Y":
            eyes = True
        while True:
            
            closest_part_distance = 100000
            closest_part = -1
            screenshot = np.array(stc.grab(region))
            df = model(screenshot, size=736).pandas().xyxy[0]
            
            counter+= 1
            
            team_rounds = ""
            enemy_rounds = ""
            
            def save_and_close():
                global team_rounds, enemy_rounds
                team_rounds = team_entry.get()
                enemy_rounds = enemy_entry.get()
                if team_rounds != "":
                    print(f"You have won {team_rounds} rounds.")
                elif team_rounds == "" :
                    print("YOU LEFT YOUR ROUND AS EMPTY, ASSUMING 0!")
                    team_rounds = "0"
                if  enemy_rounds != "":    
                    print(f"The enemy has won {enemy_rounds} rounds.")
                elif enemy_rounds == "" :
                    print("YOU LEFT ENEMY ROUND AS EMPTY, ASSUMING 0!")
                    enemy_rounds = "0"
                    
                new_team_round = ""

                for char in team_rounds:
                    if char.isdigit():
                        new_team_round += char

                team_round_new = new_team_round if new_team_round else ""
                
                new_enemy_round = ""

                for char in enemy_rounds:
                    if char.isdigit():
                        new_enemy_round += char

                enemy_round_new = new_enemy_round if new_enemy_round else ""
                
                try:
                    global total_round
                    total_round = int(enemy_round_new) + int(team_round_new)
                except ValueError:
                    print("There was a value error when adding team and enemy rounds.")
                window.destroy()
            
            if keyboard.is_pressed('b'): 
                window = tk.Tk()
                window.attributes('-topmost', True)       
                        
                window.title("Round Scores")

                window.geometry("250x150")

                icon_photo = PhotoImage(file = "Assets\\num9.png")
                window.iconphoto(False, icon_photo)

                team_label = tk.Label(window, text="Team Round Number:")
                team_label.pack()
                team_entry = tk.Entry(window)
                team_entry.pack()

                enemy_label = tk.Label(window, text="Enemy Team Round Number:")
                enemy_label.pack()
                enemy_entry = tk.Entry(window)
                enemy_entry.pack()

                save_button = tk.Button(window, text="Save and Close", command=save_and_close)
                save_button.pack()

                window.mainloop()
                
                pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\\tesseract.exe'
                upscale_factor = 10
            
                credits = ImageGrab.grab((275, 124, 352, 151 ))
                credits.save("Assets\\credits_image.png")
                
                down_scaled_credits = Image.open("Assets\\credits_image.png")
                new_size = (down_scaled_credits.width * upscale_factor, down_scaled_credits.height * upscale_factor)
                upscaled_image = credits.resize(new_size, resample= Image.NEAREST)
                upscaled_image.save("Assets\\output_cred.jpg")
                
                enhance_image = Image.open("Assets\\output_cred.jpg")
                contrast_image = ImageEnhance.Contrast(enhance_image)
                enhance_image = contrast_image.enhance(1.5)
                enhance_image = enhance_image.filter(ImageFilter.SHARPEN)
                enhance_image.save("Assets\\enhanced_image.jpg")
                
                credits = pytesseract.image_to_string("Assets\\output_cred.jpg")
                if credits == "":
                    credits = pytesseract.image_to_string("Assets\\enhanced_image.jpg")
                
                # x:940, y:881 --> Devour
                # x:1433, y:288 --> light shield
                # x:1431, y:578 --> Heavy shield
                # x:579, y:877 --> Leer
                # x:455 y:668 --> Revolver
                # x:912, y:206 --> Bulldog
                # x:660, y:348 --> Spectre  
                # x:911, y:651 --> Vandal
                
                new_credits = ""

                for char in credits:
                    if char.isdigit():
                        new_credits += char

                credits_new = new_credits if new_credits else ""
                
                print(f"Credits: {credits_new}")
                
                
                global vandal_baught, spectre_baught, bulldog_baught
                vandal_baught = False
                spectre_baught = False
                bulldog_baught = False
                
                try:
                    x, y = pyautogui.locateCenterOnScreen("Assets\\vandal_owned.png")
                except TypeError:
                    print("Vandal isn't owned")
                else:
                    print("Vandal is owned!")
                    vandal_baught = True
                    
                try:
                    x, y = pyautogui.locateCenterOnScreen("Assets\\bulldog_owned.png")
                except TypeError:
                    print("Bulldog isn't owned")
                else:
                    print("Bulldog is owned!")
                    bulldog_bught = True
                
                try:
                    x, y = pyautogui.locateCenterOnScreen("Assets\\spectre_owned.png")
                except TypeError:
                    print("Spectre isn't owned")
                else:
                    print("Spectre is owned!")
                    spectre_baught = True
                    
                if new_credits != "":
                    int_credits = int(new_credits)

                    if int_credits == 800 and total_round in [0, 4, 12]:
                        pyautogui.moveTo(x=458, y=665)
                        pyautogui.click()

                    elif int_credits > 800 and int_credits <= 2000 :
                        if spectre_baught != True:
                            pyautogui.moveTo(x=660, y=348)  # Spectre
                            pyautogui.click()
                            print("Bought Spectre!")
                            spectre_baught = True

                    elif int_credits > 2000 and int_credits <= 3000 :
                        if bulldog_baught != True:
                            pyautogui.moveTo(x=912, y=206)  # Bulldog
                            pyautogui.click()
                            print("Bought Bulldog!")
                            bulldog_baught = True
                        pyautogui.moveTo(x=940, y=881)
                        pyautogui.click()
                        pyautogui.moveTo(x=579, y=877)
                        pyautogui.click()
                        pyautogui.moveTo(x=1433, y=288)
                        pyautogui.click()

                    elif int_credits >= 3000 and int_credits < 4000:
                        if vandal_baught != True:
                            pyautogui.moveTo(x=911, y=651)  # Vandal
                            pyautogui.click()
                            print("Bought Vandal!")
                            vandal_baught = True
                        pyautogui.moveTo(x=940, y=881)
                        pyautogui.click()
                        pyautogui.moveTo(x=579, y=877)
                        pyautogui.click()
                        pyautogui.moveTo(x=579, y=877)
                        pyautogui.click()
                        pyautogui.moveTo(x=1433, y=288)
                        pyautogui.click()

                    elif int_credits >= 4000 and int_credits <= 5000 :
                        if vandal_baught != True:
                            pyautogui.moveTo(x=911, y=651)  # Vandal
                            pyautogui.click()
                            print("Bought Vandal!")
                            vandal_baught = True
                        pyautogui.moveTo(x=940, y=881)
                        pyautogui.click()
                        pyautogui.moveTo(x=579, y=877)
                        pyautogui.click()
                        pyautogui.moveTo(x=579, y=877)
                        pyautogui.click()
                        pyautogui.moveTo(x=1431, y=578)
                        pyautogui.click()

                    elif int_credits >= 5000:
                        if vandal_baught != True:
                            pyautogui.moveTo(x=911, y=651)  # Vandal
                            pyautogui.click()
                            print("Bought Vandal!")
                            vandal_baught = True
                        pyautogui.moveTo(x=940, y=881)  
                        pyautogui.click()
                        pyautogui.moveTo(x=940, y=881)
                        pyautogui.click()
                        pyautogui.moveTo(x=579, y=877)
                        pyautogui.click()
                        pyautogui.moveTo(x=579, y=877)
                        pyautogui.click()
                        pyautogui.moveTo(x=1431, y=578)
                        pyautogui.click()
                else:
                    continue
            
            if keyboard.is_pressed("="):
                print('''
   ___      _                       _              __ _                                                   
  / __|    | |     ___     ___     (_)    _ _     / _` |                                                  
 | (__     | |    / _ \   (_-<     | |   | ' \    \__, |    _       _       _                             
  \___|   _|_|_   \___/   /__/_   _|_|_  |_||_|   |___/   _(_)_   _(_)_   _(_)_                           
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|                          
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'                          
    ___     _                                                                _      _                     
   | _ \   | |     ___    __ _     ___     ___      o O O __ __ __ __ _     (_)    | |_                   
   |  _/   | |    / -_)  / _` |   (_-<    / -_)    o      \ V  V // _` |    | |    |  _|     _       _    
  _|_|_   _|_|_   \___|  \__,_|   /__/_   \___|   TS__[O]  \_/\_/ \__,_|   _|_|_   _\__|   _(_)_   _(_)_  
_| """ |_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 

                      ''')
                print("The Average FPS is: " + str(avg_fps / fps_count))
                os.system('cls')
                menu()
                
            if(time.time() - start_time) > x:
                ffps = str(int(counter/(time.time() - start_time)))
                fps = "Current FPS:"+ ffps
                print(fps+"\r".format(), end="")
                counter = 0
                start_time = time.time()
                avg_fps = avg_fps + float(ffps)
                fps_count = fps_count + 1
            
            for i in range(0,10):
                try:
                    xmin = int(df.iloc[i,0])
                    ymin = int(df.iloc[i,1])
                    xmax = int(df.iloc[i,2])
                    ymax = int(df.iloc[i,3])

                    centerX = (xmax-xmin)/2+xmin 
                    centerY = (ymax-ymin)/2+ymin

                    distance = math.dist([centerX,centerY],screenshot_center)

                    if int(distance) < closest_part_distance:
                        closest_part_distance = distance
                        closest_part = i
                    if eyes == True:
                        cv2.rectangle(screenshot,(xmin,ymin),(xmax,ymax), (255,0,0),3)
                    else: 
                        continue
                except:
                    print("",end="")


            if keyboard.is_pressed('`'):
                if triggerbot_toggle[0] == True:
                    triggerbot = not triggerbot
                    print(f"\nAim helper is now at : {triggerbot}\n")
                    triggerbot_toggle[0] = False
                    thread = threading.Thread(target=cooldown, args=(triggerbot_toggle,0.2,))
                    thread.start()

            if closest_part != -1:
                xmin = df.iloc[closest_part,0]
                ymin = df.iloc[closest_part,1]
                xmax = df.iloc[closest_part,2]
                ymax = df.iloc[closest_part,3]
                if triggerbot == True and screenshot_center[0] in range(int(xmin),int(xmax)) and screenshot_center[1] in range(int(ymin),int(ymax)):
                    keyboard.press_and_release("k")
            if eyes == True:
                cv2.imshow("frame",screenshot)
                if(cv2.waitKey(1) == ord('l')):
                    cv2.destroyAllWindows()
                    break
            else: 
                continue
            
            
menu()