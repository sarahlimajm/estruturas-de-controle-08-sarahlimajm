# Sua solução aqui
#Definição de cada váriaveis 
altura = float(input(" "))
sexo = input(" ")
#Definição das condições para a realização de cada cálculo 
if sexo == 'M':
    peso_ideal = (72.7*altura)-58
elif sexo == 'F':
    peso_ideal =  (62.1*altura)-44.7
print(f"{peso_ideal:.2f}" )
