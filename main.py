print("Bem Vindo ao meu primeiro jogo!")

nome = input("Como te chamas?  ")

idade = int(input("Quantos anos tens?  "))

print("Olá", nome, "tens", idade, "anos")

if idade > 7:
    print("Boa! Tens idade para jogar")
    
    wants_to_play = input("Queres começar o jogo? (sim/não)   ").lower()
    if wants_to_play == "sim":
       print("Vamos começar!")
       vidas = 10
       print("Tens", vidas, "vidas")

       left_or_right = input("Primeira escolha...Esquerda ou Direita? (esquerda/direira)  ")

       if left_or_right == "esquerda":
            ans = input("Boa! Agora estás num lago... Nadar ou ir a volta? (nadar/volta)    ")
            
            if ans == "volta":
               print("Tu foste de volta e chegaste ao outro lado do lago")
            elif ans == "nadar":
               print("Tu nadaste mas foste mordido por um peixe e perdeste 5 vidas")
               vidas -= 5
                
            ans = input("Agora estás numa encruzilhada...casa ou rio (casa/rio) ")
            if ans == "casa" :
               print("Tu chegaste a casa mas o dono não gostou... Perdeste 5 vidas")
               vidas -=5
               if vidas <=0:
                  print("GAME OVER")
               else:
                print("Uf... Sobreviveste WIN!!!")
            elif ans == "rio":
              print("Chegaste ao rio mas não tens nada para nadar...GAME OVER")
       else:
         print("Oh não! Caíste num buraco... GAME OVER")

else:
  print("Desculpa, mas não tens idade para jogar")
