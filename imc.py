# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
imc = round(weight / (height**2))
if imc <= 18:
    print(f'Seu IMC é de {imc} , você está abaixo do peso')
elif imc <= 22:
    print(f'Seu IMC é de {imc} , você está com o peso normal')	
elif imc <= 28:
    print(f'Seu IMC é de {imc} , você está um pouco acima do peso')
elif imc <= 33:
    print(f'Seu IMC é de {imc} , você está obeso')
else:
    print(f'Seu IMC é de {imc} , você está clinicamente obeso')