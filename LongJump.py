# This program convers a long jump given in
# centimeters to feet and inches
# @Author Ahmad Barakat


# Get the athlete's name and distance jumped
firstName = input("Long jumper's first name: ")
lastName = input("Long jumper's last name: ")
distJumped = float(input("Distance jumped (cm): "))
print()

# Convert distance to feet and inches
CMS_PER_INCH = 2.54
INCHES_PER_FEET = 12
distInches = distJumped / CMS_PER_INCH

feet = int(distInches / INCHES_PER_FEET)

inches = distInches - (INCHES_PER_FEET * feet)


#Display the converted distance

print(f'''{firstName[0]}. {lastName} jumped {feet}' {inches:.1f}"''')