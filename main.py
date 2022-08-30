# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height*height)
bmi = round(bmi)
if bmi < 18.5 :
	print("your bmi is "+ str(bmi) +" , you are underweight")
elif bmi < 25 :
	print("your bmi is "+ str(bmi) +" , you are normal weight")
elif bmi < 30 :
	print("your bmi is "+ str(bmi) +" , you are slightly overweight")
elif bmi < 35 :
	print("your bmi is "+ str(bmi) +" , you are obese")
else:
	print("your bmi is "+ str(bmi) +" , you are clinically obese")