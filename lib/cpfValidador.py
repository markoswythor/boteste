import re
import sys

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

def soNumero(cpf: str) -> str:
    return re.sub(r'\D', '', cpf)

def onzeCaracter(value: str) -> bool:
    return len(value) == 11

def sequencia(value: str) -> bool:
    return (value[0] * len(value)) == value

def validar(cpf: str) -> bool:
    cleanCpf = soNumero(cpf)

    if not onzeCaracter(cleanCpf):
        return "O CPF não tem 11 digitos, por tanto é inválido."
    
    if sequencia(cleanCpf):
        return "O CPF está em sequência, por tanto é inválido."

    digitoUm = pegarDigitoUm(cleanCpf)
    digitoDois = pegarDigitoDois(cleanCpf)

    novoCpf = f"{cleanCpf[:9]}{digitoUm}{digitoDois}"
    
    if novoCpf == cleanCpf:
        return "CPF Válido"
    
    return "CPF inválido."

print(validar(sys.argv[1]))