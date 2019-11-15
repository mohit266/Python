# Print the string like this --
"""Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are"""

string = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

sep = string.split(",")
print(sep)
for index, value in enumerate(sep):
    if index < 3:
        print(value, end=",")

    elif index == 3:
        again_split = value.split("!")
        print(f"\n\t{again_split[0]}")
        print(f"\t\t{again_split[1]}")

    elif index == 4:
        again_split = value.split(".")
        print(f"\t\t{again_split[0]}")
        print(f"{again_split[1]}", end=",")

    elif 4 < index < 7:
        print(value, end=",")

    elif index == 7:
        print(f"\n\t{value}")




