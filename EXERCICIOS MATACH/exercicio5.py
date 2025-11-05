msg = input("Mensagem: ").lower()

if msg in ["olá", "bom dia"]:
    print("Saudação")
elif msg.endswith("?"):
    print("Pergunta")
elif "xau" in msg or "adeus" in msg:
    print("Despedida")
else:
    print("Mensagem genérica")
