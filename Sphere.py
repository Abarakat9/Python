# This program displays a sphere diameter, surface area,
# and volume based upon a user-entered radius.
# @author Ahmad Barakat

from math import pi, pow

# Get the Radius
radius = float(input("Sphere radius: "))
print()

# Compute and display the diameter, surface area, and volume

diameter = 2 * radius
surfaceArea = 4 * pi * (pow(radius, 2))
volume = 4/ 3 * pi * (pow(radius, 3))

print(f"Diameter: {diameter:,.2f} units")
print(f"Surface area: {surfaceArea:,.2f} square units")
print(f"Volume: {volume:,.2f} cubic units")
