import time
import webbrowser

print("Hey, I am the biggest fan of Elon Musk.\n")
time.sleep(1)
print("That's why I made this.\n")aimport time
import webbrowser
import os
import sys

print("Hey, I am the biggest fan of Elon Musk.\n")
time.sleep(1)
print("That's why I made this.\n")

ask = input("Do you like Elon Musk? (y/n): ")
print("")

webpage = "https://www.google.com/search?q=elon+musk+is+awesome"

if ask == "y":
    time.sleep(2)
    print("Great! I am also a great fan of him. Give this project to your friends that don't like Elon Musk and tell them to say no.\n")
    time.wait(5)

elif ask == "n":
    time.sleep(2)
    print("Great! You deserves Death.")
    time.sleep(2)

    for i in range(200):
        webbrowser.open(webpage)

else:
    print("Wrong Command, Restarting the Program.........")
    time.sleep(2)
    os.startfile("muskoz.py")
    sys.exit()

ask = input("Do you like Elon Musk? (y/n): ")
print("")

webpage = "https://www.google.com/search?q=elon+musk+is+awesome"

if ask == "y":
    time.sleep(2)
    print("Great! I am also a great fan of him. Give this project to your friends that don't like Elon Musk and tell them to say no.\n")
    time.wait(5)

elif ask == "n":
    time.sleep(2)
    print("Great! You deserves Death.")
    time.sleep(2)
    
    for i in range(200):
        webbrowser.open(webpage)
