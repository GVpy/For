participantes_total = 0
maior_participantes = 0

for dia in range (1,6):
   participantes_por_dia = int(input(f"Coloque o número de participantes do dia {dia}:")) 

   participantes_total += participantes_por_dia

   if participantes_por_dia > maior_participantes:
    maior_participantes = participantes_por_dia

media_participantes = participantes_total / 5

print (f"Participantes totais: {participantes_total}\nMédia de participantes: {media_participantes:.2f}\nMaior número de participantes em um único dia {maior_participantes}")