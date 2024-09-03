tenho_fome = False
tenho_sede = True
estou_dieta = False

if tenho_fome and tenho_sede:
    print("Vou sentir cansaço se continuar")
    print("vou comer e beber coca")
elif tenho_fome and not(tenho_sede):
    print("Comer algo")
elif not(tenho_fome) and tenho_sede:
    if estou_dieta:
        print("beber água")
    else:
        print("beber coca")
else:
    print("Continuar estudando")

#Operadores de comparação:    == ; != ; < ; > ; <= ; >=
#operadores lógicos:    and ; or ; not()