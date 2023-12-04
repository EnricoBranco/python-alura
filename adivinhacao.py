import random

print("--------------------------------")
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
print("--------------------------------")


numero_aleatorio = random.randrange(1,100)
tentativa = 0

while tentativa < 10:
    
    chute = int(input("Digite um número entre 1 e 100: "))
    
    if chute == numero_aleatorio:
        tentativa += 1
        break
    
    elif chute > numero_aleatorio and chute < 100:
        tentativa += 1 
        print(f"Seu chute foi muito alto, tentativa ({tentativa} / 10)")
        
    elif chute < numero_aleatorio and chute > 0:
        tentativa += 1 
        print(f"Seu chute foi muito baixo, tentativa ({tentativa} / 10)")
    
    else:
        print("Valor inválido, tente novamente!")
    
if chute == numero_aleatorio:
    print("Fim de jogo")
    print(f"Você venceu com {tentativa} tentativas!")
    
else:
    print("Fim de jogo")
    print("Você perdeu!")
    

        
        
    
    
    
