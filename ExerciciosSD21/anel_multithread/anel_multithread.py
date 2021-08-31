'''
Exercício:

=> Usando uma linguagem de alto-nível como C/C++/Java, escrever um programa que crie 30 threads
e faça com que uma mensagem circule entre os mesmos.

=> A mensagem é uma string aleatória de pelo menos 80 caracteres.

=> A cada vez que um thread recebe a mensagem ele a imprime, modifica o primeiro caractere minúsculo
para maiúsculo, caso exista, dorme por 1 segundo, e repassa a mensagem.

=> Quando todos os caracteres forem maiúsculos, o processo repassa a mensagem e então termina.

=>Antes de terminar, o processo deve imprimir a mensagem resultante.'''

import threading
import time

numero_th = 30
thread_atual = 0
lista_th = []

string_aleatoria = input("Digite um texto de pelo menos 80 caracteres: ")

if len(string_aleatoria) < 80:
    print("Frase muito curta!")
    exit(-1)


class ClasseThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def maiuscula_ou_minuscula(self):
        global string_aleatoria
        for i in string_aleatoria:
            if i.islower():
                return False
        return True

    def run(self):
        global thread_atual
        global string_aleatoria
        global numero_th

        while 1:
            if self.maiuscula_ou_minuscula():
                break
            if thread_atual == self.threadID:
                for i in range(len(string_aleatoria)):
                    if string_aleatoria[i].islower():
                        string_aleatoria = string_aleatoria[:i] + string_aleatoria[i].upper() + string_aleatoria[i + 1:]  # Troca de minúsculo para maiúsculo
                        print(string_aleatoria)
                        time.sleep(0.5)
                        thread_atual = (thread_atual + 1) % numero_th
                        break

for i in range(numero_th):
    lista_th.append(ClasseThread(i, "Thread number " + str(i), i))
    lista_th[i].start()

while True:
    if lista_th[0].is_alive():
        continue
    else:
        print("Resultado final: " + string_aleatoria)
        break