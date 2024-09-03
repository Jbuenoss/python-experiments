try:
    number = int(input("Digite um numero: "))
    print(number)
    # 10/0
except ValueError:
    print("invalid Value")
except:
    print("excessão genérica")
finally:
    print("De qualquer forma muito obrigado")

