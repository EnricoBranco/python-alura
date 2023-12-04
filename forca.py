import random
def jogar():
 
    imprime_mensagem()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    acertou = False
    enforcou = False
    erros = 0
    
    while not acertou and not enforcou:
        
        chute = chute_usuario()
        
        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            
        else:    
            erros +=1
        
        marca_erro(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        
    if acertou:
        ganhou(palavra_secreta)
    else:
        perdeu(palavra_secreta)

def imprime_mensagem():
    print("--------------------------")
    print("Bem vindo ao jogo da forca")
    print("--------------------------")
    
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavra_secreta = []
    
    for linha in arquivo:
        linha = linha.strip().upper()
        palavra_secreta.append(linha)
        
    arquivo.close
    
    numero_aleatorio = random.randrange(0,len(palavra_secreta))
    palavra_secreta = palavra_secreta[numero_aleatorio]
    
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for i in palavra]

def chute_usuario():
    chute = input("Escolha uma letra: ")
    chute = chute.upper().strip()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    for i in range(len(palavra_secreta)):
                if chute == palavra_secreta[i]:
                    letras_acertadas[i] = chute
    print(letras_acertadas)

def marca_erro(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
def ganhou(palavra_secreta):
    print("----------------------")
    print("Parabéns, você ganhou!")
    print("----------------------")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def perdeu(palavra_secreta):
    print("-------------------------")
    print("Puxa, você foi enforcado!")
    print("-------------------------")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________        ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\   ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/    ")
    print(" |   XXX       XXX   |     ")
    print(" |                   |     ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |       ")
    print("   | I I I I I I I |       ")
    print("   |  I I I I I I  |       ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
jogar()



