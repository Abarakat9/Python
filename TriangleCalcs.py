# This program displays a triangle's area given a
# user-entered base and height.
# Ahmad



#ask user to input base and height
base = int(input("Triangle base (inches): "))
height = int(input("Triangle height (inches):  "))
print()
area = 0.5 * base * height

# Display the area
print(f'Area: {area:.1f} sq inches')
