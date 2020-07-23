#!/usr/bin/python3

import argparse

from kaufer import Kaufer

parser = argparse.ArgumentParser()
parser.add_argument("game", help="The game you're looking for")

args = parser.parse_args()

if args.game == None:
    print("You have not provided the game!")
    quit()
else:
    query = args.game

app = Kaufer()

print("Käufer CLI started")
app.search(query)

print("Exiting")