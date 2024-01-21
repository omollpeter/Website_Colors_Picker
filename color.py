from random import randint


"""
Colors are divided into three main categories - primary, secondary and tertiary colors
Primary colors: Red, yellow, blue
Secondary: Green, orange, purple/violet (Achieved by mixing primary colors i.e red-blue, yellow-red)
Tertiary: amber, vermillion, magenta, lavender, cyan, chartreuse-green (Mix primary and secondary colors)

Colors can be presented in a color wheel as follows:
"""


# color_wheel = ["yellow", "orange", "amber", "vermillion" "red", "purple", 
#                "magenta", "lavendar", "blue", "green", "cyan", "chartreuse"]

color_wheel = ["red", "orange", "yellow", "chartreuse-green", "green", "spring-green", 
               "cyan", "azure", "blue", "violet", "magenta", "rose"]
"""
Incase you are wondering
    @amber: Yellow-Orange
    @vermillion: Red-orange
    @magenta: Red-blue
    @lavender: Blue-purple
    @cyan: Blue-green
    @chartreuse: Yellow-green
"""
def pick_a_color():
    """
    Picks and return a random number between 0 and 11 (both 0 and 11 included)
    The number picked represents a color's position in the color_wheel
    """
    return randint(0, 11)

#The following functions represents method of picking contrasting color combinations in a c_wheel

def complementary(colors=color_wheel):
    """
    Returns two colors that are opposite each other in the color wheel
    """
    num1 = pick_a_color()
    num2 = num1 + 6 if num1 < 6 else num1 + 6 - 12
    return colors[num1], colors[num2]

def analogous(colors=color_wheel):
    """
    Returns three colors that are side by side in the color wheel
    """
    num1 = pick_a_color()
    num2 = num1 + 1 if num1 < 11 else num1 + 1 - 12
    num3 = num1 + 2 if num1 < 10 else num1 + 2 - 12
    print("Choose one dominant color, and use the others as accents.")
    return colors[num1], colors[num2], colors[num3]

def triadic(colors=color_wheel):
    """
    Returns three colors that are evenly spaced in the color wheel
    """
    num1 = pick_a_color()
    num2 = num1 + 4 if num1 < 8 else num1 + 4 - 12
    num3 = num1 + 8 if num1 < 4 else num1 + 8 - 12
    return colors[num1], colors[num2], colors[num3]

def tetradic(colors=color_wheel):
    """
    Returns three colors that are evenly spaced in the color wheel
    """
    num1 = pick_a_color()
    num2 = num1 + 3 if num1 < 9 else num1 + 3 - 12
    num3 = num1 + 6 if num1 < 6 else num1 + 6 - 12
    num4 = num1 + 9 if num1 < 3 else num1 + 9 - 12
    print("Choose one dominant color, and use the others as accents.")
    return colors[num1], colors[num2], colors[num3], colors[num4]

def monochromatic(colors=color_wheel):
    """
    Returns a color with three different shades, tones and tints
    """
    num1 = pick_a_color()
    return

print(tetradic())