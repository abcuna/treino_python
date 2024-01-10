import random

tabuleiro_player_2 = [[2, 2, 2, 2, 2, 2],
                      [2, 2, 2, 2, 2, 2]]

tabuleiro_player_1 = [[2, 2, 2, 2, 2, 2],
                      [2, 2, 2, 2, 2, 2]]

coordenadas_P2 = {"A1": (0,0), "A2": (0,1), "A3": (0,2), "A4": (0,3), "A5": (0,4), "A6": (0,5),
                  "B1": (1,0), "B2": (1,1), "B3": (1,2), "B4": (1,3), "B5": (1,4), "B6": (1,5)}

coordenadas_P1 = {"C1": (0,0), "C2": (0,1), "C3": (0,2), "C4": (0,3), "C5": (0,4), "C6": (0,5),
                  "D1": (1,0), "D2": (1,1), "D3": (1,2), "D4": (1,3), "D5": (1,4), "D6": (1,5)}

pontos_player_2:int = 0
pontos_player_1:int = 0

total_pedras_p1, total_pedras_p2 = sum(map(sum,tabuleiro_player_1)), sum(map(sum,tabuleiro_player_2))

quem_joga = 1
vencedor = None

def ver_tabuleiro():
    p2_letras = ["   ", "1", "2", "3", "4", "5", "6","   "]
    p1_letras = ["   ", "1", "2", "3", "4", "5", "6","   "]
    index_letra = ["A", "B", "C", "D"]
    
    for p2_letra in p2_letras:
        print(p2_letra, end=" ")
    print("\n   ------------  ")
    for index, linha in enumerate(tabuleiro_player_2):
        print(index_letra[index], end=" | ")
        for index_col, coluna in enumerate(linha):
            print(coluna, end=" ")
            if index_col == 5:
                print(f"| {index_letra[index]}", end="")
        print("")
    print("   ------------ ")
    for index, linha in enumerate(tabuleiro_player_1):
        print(index_letra[index+2], end=" | ")
        for index_col, coluna in enumerate(linha):
            print(coluna, end=" ")
            if index_col == 5:
                print(f"| {index_letra[index+2]}", end="")
        print("")
    print("   ------------ ")
    for p1_letra in p1_letras:
        print(p1_letra, end=" ")
    print(f"\n\nP1 = {pontos_player_1}    P2 = {pontos_player_2}\nPedras Capuradas")


def obter_coordenadas(coordenada:str, tabuleiro:dict):
    if coordenada in tabuleiro:
        return tabuleiro.get(coordenada)
    else:
        return "Posição desconhecida."

def mover_peca(x: int, y: int, tabuleiro:list):
  casas_a_percorrer = tabuleiro[x][y] # define o numero de casas que irá percorrer
  casas_percorridas = 0 # helper
  global pontos_player_1, pontos_player_2 # número actual de pontos dos jogadores.


  while casas_a_percorrer > casas_percorridas:
        for _ in range(casas_a_percorrer + 1): # +1 para adicionar mais um movimento, pois inicia a contagem a partir da remoção da pedra.
          valor = tabuleiro[x][y] # helper
          
          # Verifica a posição e e diz ao programa que posição é a proxima a mover

          if x == 0 and y == 0:
            next_x = 1
            next_y = 0
          elif x == 1 and y == 0:
            next_x = 1
            next_y = 1
          elif x == 1 and y == 1:
            next_x = 1
            next_y = 2
          elif x == 1 and y == 2:
            next_x = 1
            next_y = 3
          elif x == 1 and y == 3:
            next_x = 1
            next_y = 4
          elif x == 1 and y == 4:
            next_x = 1
            next_y = 5
          elif x == 1 and y == 5:
            next_x = 0
            next_y = 5        
          elif x == 0 and y == 5:
            next_x = 0
            next_y = 4
          elif x == 0 and y == 4:
            next_x = 0
            next_y = 3
          elif x == 0 and y == 3:
            next_x = 0
            next_y = 2
          elif x == 0 and y == 2:
            next_x = 0
            next_y = 1
          elif x == 0 and y == 1:
            next_x = 0
            next_y = 0
          
          # Movimento da primeira casa, que remove as pedras da casa e inicia a distribuição na proxima casa no sentido anti-horário.
          if casas_percorridas == 0:
            casas_percorridas += 1
            tabuleiro[x][y] = 0
            print(f"\n{casas_percorridas}. pos(x={x}, y={y}), {valor} -> {tabuleiro[x][y]}")
          else:
              # Caso não seja a primeira casa continua a distribuição no sentido anti-horário.
              casas_percorridas += 1
              tabuleiro[x][y] += 1
              print(f"{casas_percorridas}. pos(x={x}, y={y}), {valor} -> {tabuleiro[x][y]}") # Imprime o relatório da posição actual, pedras existentes anteriorimente e novo número de pedras.
              if (casas_percorridas-1 == casas_a_percorrer): # Verifica se está no ultimo movimento
                    if tabuleiro[x][y] > 1: # se a casa onde foi feito o ultimo movimento número de peças for maior que 1
                        print(f"\nPeças a mover: {tabuleiro[x][y]}") # Informa o número de peças que irá mover
                        mover_peca(x, y, tabuleiro) # Aplica novamente a função usando os parametros da posição actual.
                    
                    elif tabuleiro[x][y] == 1: # CAPTURA DE PEÇA
                        if tabuleiro == tabuleiro_player_1 and x == 0: # verifica se está na posição interna
                            if tabuleiro_player_2[x+1][y] > 0: # verifica se o numero de pedras do adversário na linha imediatamente a seguir do jogador 1 tem ou não peças
                                pedras_externas = 0 # helper
                                pedras_internas = tabuleiro_player_2[x+1][y] # helper
                                
                                tabuleiro_player_2[x+1][y] = 0 # recolhe as pedras internas do adversário
                                pontos_player_1 = pontos_player_1 + pedras_internas # converte o número de pedras removidas do jogador 2 em pontos
                                
                                if tabuleiro_player_2[x][y] > 0: # verfica se a coluna externa tem ou não pedras
                                  pedras_externas = tabuleiro_player_2[x][y] # helper
                                  tabuleiro_player_2[x][y] = 0 # recolhe as pedras externas
                                  pontos_player_1 = pontos_player_1 + pedras_externas # converte o número de pedras removidas do jogador 2 em pontos
                            
                                print(f"\nCapuradas {pedras_internas + pedras_externas} peças do Jogador 1") # informa aos jogadores quantas peças foram removidas
                        
                        elif tabuleiro == tabuleiro_player_2 and x == 1:
                            if tabuleiro_player_1[x-1][y] > 0:
                                pedras_externas = 0
                                pedras_internas = tabuleiro_player_1[x-1][y]

                                tabuleiro_player_1[x-1][y] = 0
                                pontos_player_2 = pontos_player_2 + pedras_internas

                                if tabuleiro_player_1[x][y] > 0:
                                   pedras_externas = tabuleiro_player_1[x][y]
                                   tabuleiro_player_1[x][y] = 0
                                   pontos_player_2 = pontos_player_2 + pedras_internas
                                
                                print(f"\nCapuradas {pedras_internas + pedras_externas} peças do Jogador 1")

          x = next_x
          y = next_y    


def obter_posicoes_validas(tabuleiro:list):
  global coordenadas_P1, coordenadas_P2
  
  if tabuleiro == tabuleiro_player_1:
     coordenadas = coordenadas_P1
  else:
     coordenadas = coordenadas_P2

  key_list = list(coordenadas.keys())
  val_list = list(coordenadas.values())

  posicoes_validas = [[],[]] # Array 2D que no primeiro index sao colocados elementos == 1, e no segundo index apenas elementos maiores que 1.
  
  for x_index, x in enumerate(tabuleiro):
    for y_index, y in enumerate(x):
      if tabuleiro[x_index][y_index] == 1:
        valor = (x_index,y_index)
        
        if valor in val_list:
          posicao = val_list.index(valor)
          posicoes_validas[0].append(key_list[posicao])

      elif tabuleiro[x_index][y_index] > 1: #verfiica se o elemento é maior que 1
        valor = (x_index,y_index) # obtem as coordenadas
        
        if valor in val_list: # verifica se as coordenadas está presente nos valores das coordenas do dicionario
          posicao = val_list.index(valor) # obtem a posição da coordenada no dicionario
          posicoes_validas[1].append(key_list[posicao]) # adiciona na lista posicoes_validas[1] a chave do elemento
  
  if len(posicoes_validas[1]) >= 1:
    return posicoes_validas[1]
  else:
    return posicoes_validas[0]
    

def jogar(tabuleiro_jogador):
    while True:
        if tabuleiro_jogador == tabuleiro_player_1:
            texto = input("Digite a coordenada: ").capitalize()
            coordenada = coordenadas_P1         
        elif tabuleiro_jogador == tabuleiro_player_2:
            texto = random.choice(obter_posicoes_validas(tabuleiro_player_2))
            coordenada = coordenadas_P2
            print(f"Jogador 2 escolheu: {texto}")
            
        coordenada = obter_coordenadas(texto, coordenada)
        if coordenada != "Posição desconhecida.":
            x, y = coordenada[0], coordenada[1]
            if tabuleiro_jogador[x][y] > 0:
                if texto in obter_posicoes_validas(tabuleiro_jogador):
                  mover_peca(coordenada[0], coordenada[1], tabuleiro_jogador)
                  print()
                  ver_tabuleiro()
                  break
                else:
                   print("Existem casas com mais de uma pedra. Tente novamente.")
            else:
                print("Nenhuma peça nesta posição. Tente novamente.")
        else:
            print("Coordenada desconhecida. Tente novamente.")

def main():
    global quem_joga, vencedor, pontos_player_1, pontos_player_2
    ver_tabuleiro()
    while vencedor is None:
        if quem_joga == 1:
            print("\nJogador 1")
            jogar(tabuleiro_player_1)
            if pontos_player_1 > total_pedras_p2 - 1:
                vencedor = pontos_player_1
                print("\n   GAME OVER  \nJOGADOR 1 VENCEU\n")
            else:
                quem_joga = 2
        else:
            print("\nJogador 2")
            jogar(tabuleiro_player_2)
            if pontos_player_2 > total_pedras_p1 - 1:
                vencedor = pontos_player_2
                print("\n   GAME OVER  \nJOGADOR 2 VENCEU\n")
            else:
                quem_joga = 1

if __name__ == "__main__":
   main()