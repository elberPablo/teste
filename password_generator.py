import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '@', '|', '*', '+']

print("Bem Vindo ao Gerador de senhas!")
nr_letters= int(input("Quantas letras você quer?\n")) 
nr_symbols = int(input("Quantos símbolos você quer?\n"))
nr_numbers = int(input("Quantos números você quer?\n"))
print('~'*22)

password = []
for letras in range(nr_letters):
    password.append(random.choice(letters))  

for simbolos in range(nr_symbols):
    password.append(random.choice(symbols))

for numeros in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
password = ''.join(password)
print(f'Senha gerada: {password}')   
