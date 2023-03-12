"""
Random funny name generator
"""
import random

nouns = ["person", "dog", "cat", "man", "woman", "fountain", "hand", "mouth", "unicorn",
         "eye", "child", "wolf", "bird", "computer", "salad", "mouse"]

adjectives = ["alcoholic", "concerned", "terrific", "lumpy", "fishy", "fierce", "weak",
              "grumpy", "happy", "courageous", "gorgeous", "old", "psychotic", "long",
              "naughty", "naive"]


def random_game_names():
    for adj in adjectives:
        for noun in nouns:
            continue
    print(f"The {adj} {noun}")


random.shuffle(nouns)
random.shuffle(adjectives)

random_game_names()
