student={}
n=int(input("Enter no of students"))
for i in range(1,n+1):
	l=[]
	sno=int(input("Enter student no"))
	sname=input("Enter student name")
	sgrp=input("Enter student group")
	scol=input("Enter student college name")
	sphn=int(input("Enter student phn no"))
	l.append(sno)
	l.append(sname)
	l.append(sgrp)
	l.append(scol)
	l.append(sphn)
	student[sno]=l
print(student)
sno=int(input("Enter student no for details"))
print("student name",student[sno][0])
print("student group",student[sno][1])
print("student college branch",student[sno][2])
print("student phn no",student[sno][3])
