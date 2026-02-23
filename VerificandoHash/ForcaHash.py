import hashlib
import random
import string
import time


def brute_force_test(charset, repetitions=10):
    tempos = []

    for _ in range(repetitions):

        # Aqui vai escolher uma letra
        seed = random.choice(charset)

        # Vai gerar o hash
        test_hash = hashlib.md5(seed.encode()).hexdigest()

        inicio = time.time()

        # Percorre todas as possibilidades
        for char in charset:
            current_hash = hashlib.md5(char.encode()).hexdigest()

            if current_hash == test_hash:
                break

        fim = time.time()

        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)

    media = sum(tempos) / len(tempos)
    return media

# Testes

print("===== TESTE 1: Apenas letras minúsculas =====")
charset1 = string.ascii_lowercase
media1 = brute_force_test(charset1)
print("Total de símbolos:", len(charset1))
print("Tempo médio:", media1, "segundos\n")


print("===== TESTE 2: Minúsculas + Maiúsculas =====")
charset2 = string.ascii_letters
media2 = brute_force_test(charset2)
print("Total de símbolos:", len(charset2))
print("Tempo médio:", media2, "segundos\n")


print("===== TESTE 3: Minúsculas + Maiúsculas + Números =====")
charset3 = string.ascii_letters + string.digits
media3 = brute_force_test(charset3)
print("Total de símbolos:", len(charset3))
print("Tempo médio:", media3, "segundos\n")


print("===== TESTE 4: Todos caracteres imprimíveis =====")
charset4 = string.printable
media4 = brute_force_test(charset4)
print("Total de símbolos:", len(charset4))
print("Tempo médio:", media4, "segundos\n")