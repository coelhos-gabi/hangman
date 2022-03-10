# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

categorias = ['animais', 'objetos', 'frutas']

# Classe
class Hangman:

    def __init__(self, word):
        self.word = word.upper()
        self.letras_erradas = []
        self.letras_certas = []
        self.palavra_secreta = []

    def check_chute(self, chute):
        index = 0
        contador = 0
        
        for letra in self.word:
            if chute == letra:
                self.palavra_secreta[index] = chute
                self.letras_certas.append(letra)
            else:
                contador += 1
            index += 1
        
        if contador == len(self.word):
            self.letras_erradas.append(chute)
            del(board[0])


    # Método para verificar se o jogo terminou
    def hangman_over(self):
        
        if self.hangman_won():
            return True
        
        elif len(board) == 1:
            return True
        
        else:
            return False

    # Método para verificar se o jogador venceu

    def hangman_won(self):
        contador = 0
        acertou = False

        for elemento in self.letras_certas:
            if elemento in self.palavra_secreta:
                contador += 1
        
        if contador == len(self.palavra_secreta):
            acertou = True
        
        return acertou

    # Método para não mostrar a letra no board

    def hide_word(self):
        
        for letra in self.word:
            self.palavra_secreta.append("-")
        for elemento in self.palavra_secreta:
            print(elemento, end='')

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        
        print(board[0])
        print('Palavra secreta:')
        
        for letra in self.palavra_secreta:
            print(letra,end='')
        
        print('\n')
        
        print('Letras certas:')
        
        for letra in sorted(set(self.letras_certas)):
            print(letra, end='')
        
        print('\n')
        
        print('Letras erradas:')
        
        for letra in sorted(set(self.letras_erradas)):
            print(letra, end='')
        
        print('\n')


# Método para ler uma palavra de forma aleatória do banco de palavras

def rand_word(escolha):
    
    with open(categorias[escolha-1]+".txt", "rt") as file:
        bank = file.readlines()

    return bank[random.randint(0, len(bank))].strip()


# Método Main - Execução do Programa

def main():

    # Objeto
    
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')
    print('\n\nQUAL CATEGORIA DESEJA JOGAR?')

    escolha = int(input('1 - ANIMAIS\n2 - OBJETOS\n3 - FRUTAS\nCATEGORIA: '))
    
    game = Hangman(rand_word(escolha))
    
    print(board[0])
    print('Palavra secreta: ')
    
    game.hide_word()
    
    print('\n')

    while True:
        chute = input('Tente uma letra: ').upper().strip()
        game.check_chute(chute)
        game.print_game_status()
        acertou = game.hangman_won()
        acabou = game.hangman_over()
        if acertou:
            print('Você ganhou o jogo!')
            break
        if acabou:
            print('Fim de jogo!')
            break
    
    print(f'A palavra era: {game.word.upper()}\n')

# Executa o programa
if __name__ == "__main__":
    main()
