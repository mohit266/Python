# This program will reminds you to drink water, eyes exercise and do some physical exercise
from pygame import mixer
from datetime import datetime
import datetime
import time


def water():
    # time.sleep(1800)
    file = 'water.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        inp_water = input("Please write drank to stop the remainder:")
        if inp_water.lower() == 'drank':
            mixer.music.stop()
            break
    with open('schedule.txt', 'a') as f:
        f.write(f"Water drink at {datetime.datetime.now()} \n")
        f.close()


def eyes():
    # time.sleep(900)
    file = 'eyes.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        inp_eyes = input("Please write eydone to stop the remainder:")
        if inp_eyes.lower() == 'eydone':
            mixer.music.stop()
            break
    with open('schedule.txt', 'a') as f:
        f.write(f"Eyes Exercise done at {datetime.datetime.now()} \n")
        f.close()


def physical():
    # time.sleep(2700)
    file = 'healthy.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        inp_health = input("Please write exdone to stop the remainder:")
        if inp_health.lower() == 'exdone':
            mixer.music.stop()
            break
    with open('schedule.txt', 'a') as f:
        f.write(f"Physical exercise done at {datetime.datetime.now()} \n")
        f.close()

if __name__ == '__main__':
    water_level = 0
    Total_water = 3500
    while water_level != 3500:
        water()
        inp_amount_wtr = eval(input("Enter how much water did you drink:"))
        if inp_amount_wtr < (Total_water - water_level):
            water_level = water_level + inp_amount_wtr
        else:
            water_level = 3500
        print(f"{Total_water - water_level} ml water remaining")
        eyes()
        physical()
