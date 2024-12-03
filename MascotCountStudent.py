# @author Ahmad Barakat

def main():
    schools = getSchoolMascots("KansasHighSchoolsSubsetUnclean.txt")
    mascotCount = getMascotCount(schools)
    showMascotCount(mascotCount)
    

# getSchoolMascots reads each school and their mascot from the given file.
# @param filename The file containing the schools and mascots.
# @precondition Each line in the file is of the form school:mascot
# @return A dictionary of school-mascot pairs   
def getSchoolMascots(filename):
    schools = {}
    with open(filename, 'r') as file:
        for line in file:
            school, mascot = line.split(":")
            mascot = mascot.strip().title()
            school = school.strip()
            schools[school] = mascot
    return schools


# getMascotCount tallies the number of times each mascot occurs
# @param schools A dictionary of school-mascot pairs
# @return A dictionary of mascot-count pairs
def getMascotCount(schools):
    mascotCount = {}
    for mascot in schools.values():
        if mascot in mascotCount:
            mascotCount[mascot] += 1
        else:
            mascotCount[mascot] = 1
    return mascotCount


# showMacotCount displays the mascots in sorted order. Each mascot 
# count is shown by the mascot.
# @param mascotCount A dictionary containing each mascot and the number
#        of times it occurred.
def showMascotCount(mascotCount):
    for mascot in sorted(mascotCount.keys()):
        print(f"{mascot}: {mascotCount[mascot]}")


main()