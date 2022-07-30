idade = bool(int(input("Você é maior de idade? (digite 1 se sim, 0 se não):")))
estado = bool(int(input("Você é casado(a)? (digite 1 se sim, 0 se não):")))

resp = "Você é "

if idade:
    resp += "maior de idade e "
else:
    resp += "menor de idade e "

if estado:
    resp += "casado."
else:
    resp += "solteiro."

print(resp)