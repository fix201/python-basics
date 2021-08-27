# Old BMI Calculator

# BMI = weight / height ^ 2

size = int(input("How many body mass indexes would you be chacking: "))
inputs = []

for i in range(size):
  w, h = map(float,  input("Enter weight followed by height: ").split())
  inputs.append((w,h))

def checkResults(bmi):
  if bmi < 18.5:
    return 'under'
  elif 18.5 <= bmi and bmi < 25:
    return 'normal'
  elif 25 <= bmi and bmi < 30.0:
    return 'over'
  elif 30 <= bmi:
    return 'obese'

print(inputs)
bmi = list(map(checkResults, list(map(lambda w: w[0] / w[1] ** 2, inputs))))
print(bmi)