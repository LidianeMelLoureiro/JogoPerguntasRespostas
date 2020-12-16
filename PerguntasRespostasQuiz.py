#Projeto desenvolvido por Lidiane Mel Loureiro em 2020
#Jogo de Perguntas e Respostas

pontos = 0  #Declaração da variável
print("Bem vindo ao jogo de perguntas e respostas! Vamos começar!") #Boas vindas aos jogadores

print("\n Pergunta 1: Olhe para suas mãos. Há 10 dedos. Quantos dedos há em 10 mãos?") #Exibindo a pergunta 1
resposta1 = input("R: " ) #Resposta do usuário
if resposta1 == "50" :  # (linha 9 a 13) Verificação e correção da resposta sobre a pergunta 1
    print("Resposta Certa! Vamos para a próxima pergunta!")
    pontos = pontos + 2
else :
    print("Resposta Errada!")
    
print("\n Pergunta 2: Meu avô tem 4 filhos. Cada filho tem 4 filhos. Quantos primos eu tenho?") #Exibindo a pergunta 2
resposta2 = input("R: " )
if resposta2 == "12" : # (linha 17 a 21) Verificação e correção da resposta sobre a pergunta 2
    print("Resposta Certa! Vamos para a próxima pergunta!")
    pontos = pontos + 2
else :
    print("Resposta Errada!")

print("\n Pergunta 3: Alguns meses têm 30 dias. Outros têm 31. Quantos meses tem 28 dias?") #Exibindo a pergunta 3
resposta3 = input("R: " )
if resposta3 == "12" :  # (linha 25 a 29) Verificação e correção da resposta sobre a pergunta 3
    print("Resposta Certa! Vamos para a próxima pergunta!")
    pontos = pontos + 2
else :
    print("Resposta Errada!")

print("\n Pergunta 4: Em um evento tem 6 velas acesas. 3 velas se apagam. Quantos velas sobram?") #Exibindo a pergunta 4
resposta4 = input("R: " )
if resposta4 == "6" :  # (linha 33 a 37) Verificação e correção da resposta sobre a pergunta 4
    print("Resposta Certa! Vamos para a próxima pergunta!")
    pontos = pontos + 2
else :
    print("Resposta Errada!")

print("\n Pergunta 5: Quantos pares de olhos a maioria das aranhas têm?") #Exibindo a pergunta 5
resposta = input("R: " )
if resposta == "4" :  # (linha 41 a 45) Verificação e correção da resposta sobre a pergunta 5
    print("Resposta Certa! Vamos para a próxima pergunta!")
    pontos = pontos + 2
else :
    print("Resposta Errada!")

# Resultado final e desempenho do jogador:
if (pontos > 7):
    print("Parabéns! Você fez" ,pontos, "pontos!")
elif ((pontos > 5) and (pontos < 7)):
    print("Quase lá! Mais atenção nas perguntas!")
    print("Pontuação Total: " ,pontos)
elif (pontos < 5):
    print("Poxa, poderia ter se esforçado mais...")
    print("Pontuação Total: " ,pontos)

 print("Pontuação Máxima: 10")