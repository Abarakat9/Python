from PersonClass import Person

def main():

    family = [Person("Nick", 23), Person("Tyler", 22),
            Person("Sydney", 19), Person("Kiley", 16)]
    
    showFamily(family)
    increaseAge(family)
    print("\nAfter aging")
    showFamily(family)

def showFamily(family):
    for member in family:
        print(member)

def increaseAge(family, amount = 1):
    for member in family:
        member.setAge(member.getAge() + amount)

main()