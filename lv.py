#dia 3 ex 3
print('love calculator')
nome = str(input('Nome: ')).lower()
nome2 = str(input('Nome: ')).lower()

true = nome.count('t')+nome.count('r')+nome.count('u')+nome.count('e')+nome2.count('t')+nome2.count('r')+nome2.count('u')+nome2.count('e')
love = nome.count('l')+nome.count('o')+nome.count('v')+nome.count('e')+nome2.count('l')+nome2.count('o')+nome2.count('v')+nome2.count('e')

score = int(str(true)+str(love))

if score < 10 or score > 90:
    print(f'seu score é {score} , o negocio parece que não vai dar certo!')
elif score >= 40 and score <= 50:
    print(f'seu score é {score} , vocês vão se dar bem juntos!')
else:
    print(f'seu score é {score}')
print('FIM...')

