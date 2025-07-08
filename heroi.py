def classificar_heroi(nome: str, xp: int) -> str:
    if xp <1000:
        nivel = "Ferro"
    elif xp <= 2000:
        nivel = "Bronze"
    elif xp <= 5000:
        nivel = "Prata"
    elif xp <= 7000:
        nivel = "Ouro"
    elif xp <= 8000:
        nivel = "Diamante"
    elif xp <= 9000:
        nivel = "Ascendente"
    elif xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    return f"O Herói {nome} está no nível {nivel}" 
try: 
    nome_heroi = input("Digite o nome do herói:")
    xp_heroi = int(input("Digite a quantidade de XP do herói:"))
    print(classificar_heroi(nome_heroi, xp_heroi))
except ValueError:
    print("Por favor, insira um número válido para a quantidade de XP.")
