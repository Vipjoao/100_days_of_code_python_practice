# A set of colors that are compatible with the 'turtle' package
import random

tur_colors = [
    "red", "green", "blue", "yellow", "orange",
    "purple", "pink", "brown", "black", "tan",
    "gray", "cyan", "magenta", "violet", "indigo",
    "turquoise", "gold", "silver", "maroon", "lime",
    "olive", "navy", "teal", "aqua", "coral",
    "salmon", "khaki", "orchid", "plum",
]

def random_color():
    r = random.randint(0, 255) / 255.0
    g = random.randint(0, 255) / 255.0
    b = random.randint(0, 255) / 255.0
    return (r, g, b)
