studentList = []
tgrpsTeamsList = {}

with open('sample.csv') as records:
    records.__next__() # Skip the header row
    lines = records.read().strip().split('\n')
    
    for line in lines:
        line = line.split(',')
        
        studentList.append(line)

def MakeTutGrp(studentList, tutorialnum): ### Makes a list of the students in a tutorial group
    tutorialGroup = []
    for student in studentList:
        if student[0] == tutorialnum:
            tutorialGroup.append(student)
    return tutorialGroup

def GenderCount(tutorialGroup):            ### Counts how many boys and girls there are in a tutorial group
    boyCount = 0
    girlCount = 0
    for student in tutorialGroup:
        if student[4] == 'Male':
            boyCount = boyCount + 1
        else:
            girlCount = girlCount + 1
    return boyCount, girlCount

def GenderSlap (List, count, FCount, MCount, tutorialGroup):   ###  Assigns only based on gender to a group with what gender requirements.
    FMember = 0
    MMember = 0                                                ###  ^e.g  Make group for 3 females and 2 male
    while True:
        for student in tutorialGroup:
            if MMember + FMember == 5:
                break
            if FMember < FCount:
                if student[4] == "Female":
                    List[count].append(student)
                    FMember = FMember + 1
            if MMember < MCount:
                if str(student[4]) == 'Male':
                    List[count].append(student)
                    MMember = MMember + 1
        break
    for student in List[count]:
        tutorialGroup.remove(student)
    count = count + 1
    return List, count, tutorialGroup
    
def GenderAssignment(tutorialGroup, domGender, Grp2, Grp3, Grp0):     ### To tell the function GenderSlap above how many groups of what ratio it is to produce and organise them to make the actual lists of groups

    if domGender == "Female":                                         
        F0count = 5
        F1count = 2
    else:
        F0count = 0
        F1count = 3
    M0count = 5 - F0count
    M1count = 5 - F1count
    F2count = M1count
    M2count = F1count

    GrpTwo = 0
    GrpThree = 0
    GrpZero = 0

    List = []
    for i in range(0, 10):
        Group = []
        List.append(Group)
    count = 0
    while True:
        while True:
            if GrpZero == Grp0:
                break
            else:
                List, count, tutorialGroup = GenderSlap(List, count, F0count, M0count, tutorialGroup)
                GrpZero = GrpZero + 1
        while True:
            if GrpThree == Grp3:
                break
            else:
                List, count, tutorialGroup = GenderSlap(List, count, F1count, M1count, tutorialGroup)
                GrpThree = GrpThree + 1
        while True:
            if GrpTwo == Grp2:
                break
            else:
                List, count, tutorialGroup = GenderSlap(List, count, F2count, M2count, tutorialGroup)
                boyCount = GenderCount(tutorialGroup)
                GrpTwo = GrpTwo + 1
        if count == 10:
            break
    return List

def GroupAssignmentGender(studentList, tutorialnum):                     ### To calculate how many groups of what ratio is needed and then give the lists of groups
    tutorialGroup = MakeTutGrp(studentList, tutorialnum)
    boyCount, girlCount = GenderCount(tutorialGroup)
    if boyCount < 20:
        if boyCount % 2 == 1:
            boy2Grp = int(boyCount//2)
            boy3Grp = 1
            boy0Grp = 9 - boy2Grp
            GroupList = GenderAssignment(tutorialGroup, 'Female', boy2Grp, boy3Grp, boy0Grp)

        elif boyCount % 2 == 0:
            boy2Grp = int(boyCount//2)
            boy3Grp = 0
            boy0Grp = 10 - boy2Grp
            GroupList = GenderAssignment(tutorialGroup, 'Female', boy2Grp, boy3Grp, boy0Grp)

    
    elif girlCount < 20:
        if girlCount % 2 == 1:
            girl2Grp = int(girlCount//2)
            girl3Grp = 1
            girl0Grp = 9 - girl2Grp
            GroupList = GenderAssignment(tutorialGroup, 'Male', girl2Grp, girl3Grp, girl0Grp)

        elif girlCount % 2 == 0:
            girl2Grp = int(girlCount//2)
            girl3Grp = 0
            girl0Grp = 10 - girl2Grp
            GroupList = GenderAssignment(tutorialGroup, 'Male', girl2Grp, girl3Grp, girl0Grp)

    else:
        GroupList = []
        for i in range(0,10):
            MMember = 0
            FMember = 0
            GroupXlist = []
            GroupList.append(GroupXlist)
            while True:
                if MMember == 2 and FMember == 2:
                  break
                for student in tutorialGroup:
                    if student[4] == "Male":
                        if MMember < 2:
                            GroupList[i].append(student)
                            tutorialGroup.remove(student)
                            MMember = MMember + 1
                    elif student[4] == "Female":
                        if FMember < 2:
                            GroupList[i].append(student)
                            tutorialGroup.remove(student)
                            FMember = FMember + 1
        for i in range(0,10):
            GroupList[i].append(tutorialGroup[i])

    return GroupList

GroupList = GroupAssignmentGender(studentList, 'G-2')

#print(GroupList)

#print(len(GroupList))         # Test for how many groups there are and students per group
#for i in GroupList:
#    print(len(i))

#List = []
#for i in range(0, 10):
#    Group = []
#    List.append(Group)
#count = 0
#List[count].append('a')
#print(List[count])