# praktikum hal 15
# get user first name and last name
first=input("please enter your first name(all lowercase): ")
last=input("please enter your last name(all lowercase): ")

#concantenate first initial with7 char of last name
uname=first[0]+last[:7]
print(uname)

#praktikum hal 16
print([1,2]+[3,4])
print([1,2]*3)
grades=['A','B'+'C'+'D'+'F']
print(grades[0])
print(grades[2:4])
print([len(grades)])