# -*- coding: utf-8 -*-
from sys import exit

def gold_room():
    print "This romm is full of gold. How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
        exit(0)
    if how_much < 50:
        dead("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch if honey."
    print "That fat bear is in front if another door."
    print "How are you going to move the bear?"
    bear_moved = False
    while True:
        next = raw_input(" >")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. you can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets plssed off and chews your lef off.")
        elif next == "Open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
        
def cthulhu_room():
    print "Here you see the great evil cthulhu."
    print "He, it, whatever stares at you and you go insance."
    print "Do you flee for your life or eat your head?"
    next = raw_input("> ")

    if "Flee" in next:
        start()
    elif "Head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take."

    next = raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "rigth":
        cthulhu_room()
    else:
        dead("You stumble around the romm until you starve.")

start()