user = {"nome": "João", "idade": 30, "tipo": "admin"}

if user["idade"] < 18:
    print("Utilizador menor de idade")
elif user["tipo"] == "admin":
    print("Administrador")
else:
    print("Utilizador comum")
