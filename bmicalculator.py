weight = float(input("input your weight in pounds: "))
height = float(input("input your height in inches: "))
bmi = weight/(height**2) * 703

print(f"your BMI is: {bmi:.2f}")
