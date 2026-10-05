print("qual sua idade?")
idade = int(input(""))
if idade > 12:
    print("voce é uma criança")
elif 12 <= idade >= 18:
    print("voce é adolescente")
else:
    print("voce é adulto ")