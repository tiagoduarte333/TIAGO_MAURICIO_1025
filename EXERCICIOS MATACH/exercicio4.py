valor = [10, 20, 30]

if isinstance(valor, int):
    print("Número inteiro")
elif isinstance(valor, float):
    print("Número decimal")
elif isinstance(valor, str):
    if valor.isdigit():
        print("String numérica")
    else:
        print("String textual")
elif isinstance(valor, list):
    print("Lista")
else:
    print("Tipo desconhecido")
