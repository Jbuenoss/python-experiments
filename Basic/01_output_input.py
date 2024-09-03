name = "João"
age = 19
is_male = True
print(f"Hi! my names is {name} and I am {age} years old")
print(f"Am I a man? : {is_male}")

months = float(age * 12)
print(str(type(months)) + ' ' + str(months)) #somente pode concatenar string

months = int(months) #sempre que converter um float para int estará retirando o que estiver após o ponto
print(str(type(months)) + ' ' + str(months)) 

age2 = "10.3"
print(type(age2))

age2 = int(float(age2))
print(type(age2))

print(f"divisão normal: {age / age2}")
print(f"divisão inteira {age // age2} com resto {age % age2}")

print(f"Raiz quadrada da idade: {age ** (1/2)}")

name = input("Type your name: ") #ler a linha toda
age = int(input(f"type the year you born {name} "))
print(f"you are {2023-age} years old")
