#BMI CALCULATOR

print("\n")
print("BML CALCULATOR")
print("\n")

weight = float(input("Enter your weight(LB)"))
height = float(input("Enter your height(FEET)"))

try:
    value =  weight/(height**2) #BMI FORMULA
except:
    print("You cannot devide 0")

if value < 18.5:
    print(round(value,2) , " underweight")
elif value >= 18.5 and value < 25:
    print(round(value,2) , " Normal")
elif value >= 25 and value < 30:
    print(round(value,2) , " Overweight")
elif value >= 30:
    print(round(value,2) , " Obesity")
else:
    print("error")