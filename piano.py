from playsound import playsound
from time import sleep
import random
import string
from pathlib import Path


s = input("Please Enter the path of your file: ")
file = open(s, "r")
c=[ch for ch in file.read()]

home = str(Path.home())

for char in c:
    sleep(0.5)

    if char.isupper() == True:
        char = char.lower()

    if char == '\n':
        break

    alph = list(string.ascii_lowercase)
    sounds = ['28', '26', '25', '27',  '24', '25', '26', '29', '26', '28', '29', '28', '27', '28', '29', '26', '28', '25', '27', '23', '24', '28', '27', '22', '26', '19']

    index_of_char = alph.index(f'{char}')
    sound = sounds[index_of_char]
    playsound(f'{home}/sounds/piano/{sound}.mp3')
    
