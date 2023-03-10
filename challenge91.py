#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi["sprites"]["front_default"])

    for move in pokeapi["moves"]:
        print(move["move"]["name"])

    game_count = 0
    for game in pokeapi["game_indices"]:
        game_count += 1

    print(f"Total Games: {game_count}")
main()

