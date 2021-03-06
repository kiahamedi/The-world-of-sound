from playsound import playsound
from time import sleep
from random import uniform 
import string
from pathlib import Path

def pause():
    rand = uniform(0.1, 0.9)
    pause_dure = round(rand, 1)
    return pause_dure

s = input("Please Enter the path of your file: ")
file = open(s, "r")
c=[ch for ch in file.read()]

home = str(Path.home())

for char in c:
    sleep(pause())    

    if char.isupper() == True:
        char = char.lower()

    if char == '\n':
        continue

    alph = list(string.ascii_lowercase)
    sounds = ['28', '26', '25', '27',  '24', '25', '26', '29', '26', '28', '29', '28', '27', '28', '29', '26', '28', '25', '27', '23', '24', '28', '27', '22', '26', '19']

    index_of_char = alph.index(f'{char}')
    sound = sounds[index_of_char]
    playsound(f'{home}/sounds/piano/{sound}.mp3')
    
