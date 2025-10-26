# A function to retrieve and return the sorted specified Tutorial Group by gpa
def retrieveTutorialGroup(studentList, groupNum):
    studList = sortCGPA(studentList)
    tgrpList = []
    
    for student in studList:
        if student.tutorialGrp == groupNum:
            tgrpList.append(student)
    
    return tgrpList

# Counts how many boys and girls there are in a tutorial group
def genderCount(tutorialGroup):
    boyCount = 0
    girlCount = 0

    for student in tutorialGroup:
        if student.gender == 'Male':
            boyCount += 1
        else:
            girlCount += 1
            
    return boyCount, girlCount

# Main Body
tgrp = retrieveTutorialGroup(studentList, 56)

#make it fluid . 1 b 1 g always. the spare fill them up. if more g, fill g, if more b, fill b. if run out, fill in remaining.
# calculate no. of teams formed based on no. of ppl per team
# % gives remainder. add extra grp is thrs one. else ignore
teamsize = 7 #input size (4-10)
split = teamsize // 2 #determine max even no. of girls and boys in each grp. If max grp size is 5, thr will be 2 girls and 2 boys
numm, numf = genderCount(retrieveTutorialGroup(studentList, 1))
totalst = numm + numf
leftovers = totalst % teamsize #create a list if thrs leftovers
numteam = totalst // teamsize #create a list based on num team
grplist = []

for i in range (numteam): #generate grp
    grplist.append([])

#separate male and female
malelist = []
femalelist = []
for st in tgrp:
    if st.gender == 'Female':
        femalelist.append(st)
    elif st.gender == 'Male':
        malelist.append(st)
# print(len(malelist)) #21
# print(len(femalelist)) #29
maxmale=0 #store max count
maxfemale=0 #store max count
icount=0 #add students sequentially
for num in range(len(grplist)):
    for i in range(split): #add students according to split
        if len(malelist) == 0 and len(femalelist) == 0:
            print("no students found for both male/female list")
            break
        elif icount >= len(malelist) and icount >= len(femalelist): #if both hit, break
            #no one to add alr since both exceed list limit
            break
        elif icount >= len(malelist): #if male hit limit, # add female last iter
            maxfemale = icount #record down last iteration after adding last iter
            break
        elif icount >= len(femalelist): #if female hit limit, # add male last iter
            maxmale = icount #record down last iteration after adding last iter
            break
        else: #continue append if no issue
            #print(icount)
            grplist[num].append(malelist[icount])
            grplist[num].append(femalelist[icount])
            icount+=1
            if grplist[num] == grplist[-1]: #if last grp and all grps filled up nice nice with no issue,
                maxmale = icount #record down last iteration but doesnt add last iter
                maxfemale = icount #record down last iteration but doesnt add last iter

# check who hit limit
if maxfemale !=0 and maxmale !=0: #if both genders didnt hit limit
    for grp in grplist:
        while len(grp) != teamsize: #if grp full, next grp.
            if maxfemale < len(femalelist): #if doesnt exceed female. add female first
                grp.append(femalelist[maxfemale])
                maxfemale+=1
            elif maxmale < len(malelist): #if female no more, add male but check if exceed malelist
                grp.append(malelist[maxmale]) 
                maxmale+=1
            else:
                print('no one to add')
                break
    if leftovers !=0: #generate last grp for leftovers
        grplist.append([]) 
        while maxfemale < len(femalelist): #add remaining females/males to last grp
            grplist[-1].append(femalelist[maxfemale]) 
            maxfemale+=1
        while maxmale < len(malelist):
            grplist[-1].append(malelist[maxmale]) 
            maxmale+=1 

elif maxfemale !=0: #if male hit limit, add from female list until full
    for grp in grplist:
        while len(grp) != teamsize: #if grp full, next grp
            if maxfemale < len(femalelist):
                grp.append(femalelist[maxfemale])
                maxfemale+=1
            else:
                print('no one to add')
                break
    if leftovers !=0: #generate last grp for leftovers
        grplist.append([]) 
        while maxfemale < len(femalelist): #add remaining females to last grp
            grplist[-1].append(femalelist[maxfemale]) 
            maxfemale+=1

elif maxmale !=0: #else if female hit limit, add from male list until full
    for grp in grplist:
        while len(grp) != teamsize: #if grp full, next grp
            if maxmale < len(malelist):
                grp.append(malelist[maxmale])
                maxmale+=1
            else:
                print('no one to add')
                break
    if leftovers !=0: #generate last grp for leftovers
        grplist.append([]) 
        while maxmale < len(malelist): #add remaining males to last grp
            grplist[-1].append(malelist[maxmale]) 
            maxmale+=1
else:
    print("no student found for both male/female list")

#debugging output
grpnum=1
print("tutorial Grp:", 1)
for grp in grplist:
    print("Group No.:", grpnum)
    for st in grp:
        print(st.name, st.gender)
        print()
    grpnum+=1