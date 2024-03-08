#### Q1 ####

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma = soma + k

print("Q1:")
print(f"O valor da soma é: {soma}")


#### Q2 ####
def fibonacci(n):
    seq = [0, 1]

    while seq[-1] < n:
        seq.append(seq[-1] + seq[-2])

    return n in seq


n = int(input("Digite o número que deseja verificar: "))

if fibonacci(n):
    print(f"{n} está na sequência de Fibonacci")
else:
    print(f"{n} não esta na sequência de Fibonacci")

#### Q3 ####
# A) Números impares: 9 /ou/ Números primos: 11
# B) O dobro do anterior ou 2^n+1: 128
# C) O quadrado de cada número inteiro: 49
# D) O quadrado dos números pares: 100
# E) Fibonacci: 13
# F) Não consegui idenficiar

#### Q4 ####
# Eu posso acender uma lampada e ir até uma das salas, se esta lampada estiver
# acesa, então já tenho minha resposta na minha próxima jogada, pois ainda tenho uma ida
# e é só acender outro interruptor e ir até alguma das salas restantes, independente se
# a lâmpada vai estar acesa ou não, você já tem a sua resposta
# mas caso a lâmapda da sala da primeira ida não esteja acesa, volte, desligue o interruptor
# ligado anteriormente, ligue outro e vá para outra sala, se a lampada está ligada, então você
# já tem a sua resposta, parecida com a solução anterior, mas se ela estiver apagada
# você pode tentar chegar a lampada e verificar se ela ou o ar em volta dela está quente,
# caso esteja, então ela é a primeira lampada que você ligou no primeiro interruptor, assim você
# tem a resposta igual a solução anterior

#### Q5 ####
# Problema simples de lógica de programação, é apenas usar um -1 no for, para percorrer de traz para frente
# Lembrando de limitar a parada em -1, para que seja percorrido até o indice 0
string = input("Digite a string que você quer inverter: ")
string2 = ""

for i in range(len(string) - 1, -1, -1):
    string2 += string[i]

print(f"String invertida: {string2}")
