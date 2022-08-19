'''
############
# Lab 0.01 #
############

In this lab we will create a class that will represent colors 
and build a function to combine two colors.


1.  Create a class, Color.
2.  Instantiate at least 3 colors.
3.  Add attributes of r, g, and b to those instances.
4.  Create a function, add_color, which takes in two colors 
    and returns a color that is the sum of the two reds, greens, 
    and blues. Don't forget: the maximum value for R, G, or B is 255.
'''
from urllib.response import addclosehook


class Color():
    '''This creates different colors'''

# instantiate 3 color objects
color1 = Color()
color2 = Color()
color3 = Color()

# set color attributes
color1.r = 100
color1.g = 95
color1.b = 201
##################
color2.r = 23
color2.g = 137
color2.b = 1
##################
color3.r = 255
color3.g = 55
color3.b = 62

def add_colors(color_a, color_b):
    #instantiate a new color
    new_color = Color()

    # assign red for the new color object
    new_color.r = color_a.r + color_b.r
    if new_color.r > 255:
        new_color.r = 255

    new_color.g = color_a.g + color_b.g
    if new_color.g > 255:
        new_color.g = 255

    new_color.b = color_a.b + color_b.b
    if new_color.b > 255:
        new_color.b = 255
    

    return new_color

color4 = add_colors(color3, color2)
color5 = add_colors(color1, color3)
color6 = add_colors(color1, color2)

print(f"Color 4's RBG value is: {color4.r},{color4.g},{color4.b}.")
print(f"Color 5's RBG value is: {color5.r},{color5.g},{color5.b}.")
print(f"Color 6's RBG value is: {color6.r},{color6.g},{color6.b}.")

