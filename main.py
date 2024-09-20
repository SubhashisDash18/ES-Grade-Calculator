def calc(i):
	GAA = int(input("Please input your Graded Assignment Average Score: "))
	Qz1 = int(input("Please input your Quiz 1 Score: "))

	#Input Block
	if i == "MA2101" or i == "MA1101" or i == "EE1101" or i == "EE1102" or i == "EE1103" or i == "EE2101" or i == "HS1101" or i == "HS1102" or i == "EE2102":
		Qz2 = int(input("Please input your Quiz 2 Score: "))
	elif i == "CS2101":
		GrPAA = int(input("Please input your GrPA Average Score: "))
		Qz2 = int(input("Please input your Quiz 2 Score: "))
		IPL = int(input("Please input your in-person lab Score: "))
	elif i == "CS1102":
		PE1 = int(input("Please input your NPPE Score: "))
		PE2 = int(input("Please input your OPPE Score: "))
		VMT = int(input("Please input your VM Task Score: "))
		LAB = int(input("Please input your Lab Score: "))
	elif i == "CS2102":
		GrPAA = int(input("Please input your GrPA Average Score: "))
		PE1 = int(input("Please input your OPPE 1 Score: "))
		PE2 = int(input("Please input your OPPE 2 Score: "))
	elif i == "CS1101":
		WTA = int(input("Please input your Weekly Timed Assignment Scores: "))
		PE1 = int(input("Please input your OPPE 1 Score: "))
		PE2 = int(input("Please input your OPPE 2 Score: "))
	elif i == "EE3101":
		Qz2 = int(input("Please input your Quiz 2 Score: "))
		LE = int(input("Please input your Lab Experiment Score: "))
		LV = int(input("Please input your Lab Viva Score: "))
	
	F = int(input("Please input your End Term Score: "))

	#Formula Block
	if i == "CS2101":
		T = (0.8*(0.1*GAA + 0.1*GrPAA + max((0.5*F + 0.2*max(Qz1, Qz2)), (0.4*F + 0.2*Qz1 + 0.2*Qz2))) + 0.2*(IPL) + 5)
	#Linux needs some double checking
	elif i == "CS1102":
		T = (0.06*GAA + 0.04 * PE1 + 0.2*Qz1 + 0.3*F) + 0.4*min(0.1*VMT + 0.5*LAB + 0.5*PE2, 100) + 5
	elif i == "CS2102":
		T = (min(0.1*GAA + 0.1*GrPAA + 0.1*Qz1 + 0.4*F + 0.25*max(PE1, PE2) + 0.15*min(PE1, PE2), 100) + 5)
	elif i == "EE1101" or i == "EE1102" or i == "EE1103" or i == "EE2101" or i == "MA2101" or i == "MA1101" or i == "HS1101" or i == "HS1102" or i == "EE2102":
		T = (0.1*GAA + max(0.6*F + 0.2*max(Qz1, Qz2), 0.4*F + 0.2*Qz1 + 0.3*Qz2) + 5)
	elif i == "CS1101":
		T = (0.1*GAA + 0.2*Qz1 + 0.4*F + max(0.15*PE1 + 0.15*PE2, 0.2*max(PE1, PE2)) + 0.15*(max(100, WTA)) + 5)
	elif i == "EE3101":
		T = (0.1*GAA + 0.1*LE + 0.05*LV + max(0.55*F + 0.1*max(Qz1, Qz2), 0.45*F + 0.15*Qz1 + 0.15*Qz2) + 5)
	grade(min(T, 100))

def grade(T):
	grade = "Invalid"
	if T >= 90:
		grade = "S"
	elif T >= 80:
		grade = "A"
	elif T >= 70:
		grade = "B"
	elif T >= 60:
		grade = "C"
	elif T >= 50:
		grade = "D"
	elif T >= 40:
		grade = "E"
	else:
		grade = "I"

	if not grade == "I":
		print(f"\nyour Final Score is |{T}| and your grade is |{grade}|\n")
	else:
		print(f"\nYour Final Score is |{T}| and your grade is |{grade}|\nBetter luck next time\n")

codeList = ("EE1101", "EE1102", "EE1103", "EE2101", "CS1101", "CS1102", "CS2101", "CS2102", "MA1101", "MA2101", "HS1101", "HS1102", "EE2102", "EE3101")
__con__ = "yes"

with open("message.txt", "r") as file:
	content = file.read()
print(content)
print("\nAvailable Courses for the term May 2024:\n\nHS1101  |  CS1101  |  EE1101  |  MA1101\nHS1102  |  CS1102  |  EE1102  |  EE1103\nCS2101  |  CS2102  |  MA2101  |  EE2101\n")

while __con__ == "yes":
	#Input
	__code__ = input("Please input the code of the course: ")
	if not __code__ in codeList:
		exit()
	
	#Calculation
	calc(__code__)

	#Continuation
	__con__ = input("Do you want to continue? (yes/no)\n")
	if __con__ == "no":
		print("Exiting the Calculator")
	elif __con__ == "yes":
		q = 0
	else:
		print("Invalid Input")