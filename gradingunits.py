stds=[]
for i in range(1,6):
Std_Name = input("Your name:")
Std_Adm = input("Admission Number:")
Age = int(input("Your current age:"))
Mark1 = int(input("Marks for the first subject:"))
Mark2 = int(input("Marks for the second subject:"))
Mark3 = int(input("Marks for the third subject:"))

SumTotal = int(Mark1 + Mark2 + Mark3)
Average = float(SumTotal / 3)

def calculate_average():
    if Average <=100 and Average<=79:
        Grade= "A"
    elif Average >=60:
        Grade= "B"
    elif Average >=50:
        Grade= "C"
    elif Average >=40:
        Grade= "D"
    else:
        Grade= "F"
    return Grade
def classify_grade():
    if calculate_average() == "A":
        Status = "First Class"
    elif calculate_average() == "B":
        Status = "Second Class"
    elif calculate_average() == "C":
        Status = "Second class lower"
    elif calculate_average() == "D":
        Status = "Pass"
    else:
        Status = "Fail"
    return Status
    stdlist = [Std_Name, Std_Adm, Age, SumTotal, Average, calculate_average(), classify_grade()]
    stds.append(stdlist)
print("------------Student Result-------------")
print(Std_Name)
print(Std_Adm)
print(SumTotal)
print(Average)
print(calculate_average())
print(classify_grade())
