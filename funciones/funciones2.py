def palindromo(pal):
    palabraMin      =    pal.lower() #minusculas
    palabraRep = palabraMin.replace(" ", "") #quitando espacios
    if palabraRep == palabraRep[::-1]:
        return "Si"
    else:
        return "No"
    

palabra=input("Digite la palabra: ")

#print
print(f"{palabra } es palindroma?????? {palindromo(palabra)}")