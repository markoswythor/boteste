import random

def pegarDigito(cpf: str) -> int:
    lenCpf = len(cpf) + 1

    multiplication = []
    for cpfIndex, multiplier in enumerate(range(lenCpf, 1, -1)):
        multiplication.append(int(cpf[cpfIndex]) * multiplier)
    total = sum(multiplication)
    digit = 11 - (total % 11)
    return digit if digit < 10 else 0
    

def pegarDigitoUm(cpf: str) -> int:
    return pegarDigito(cpf[:9])

def pegarDigitoDois(cpf: str) -> int:
    return pegarDigito(cpf[:10])

def gerarCpf() -> str:
    noveDigitos = "".join([str(random.randint(0, 9)) for x in range(9)])
    digitOne = pegarDigitoUm(noveDigitos)
    digitTwo = pegarDigitoDois(f"{noveDigitos}{digitOne}")
    novo_Cpf = f"{noveDigitos[0:3]}.{noveDigitos[3:6]}.{noveDigitos[6:9]}-{digitOne}{digitTwo}"
    return novo_Cpf

print(gerarCpf())