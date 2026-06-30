# Escreva um programa que receba a temperatura atual em graus Celsius (°C) e exiba uma mensagem alertando o usuário sobre as condições climáticas e cuidados a tomar

temp = float(input("Digite a temperatura atual: "))

if temp < 15:
    print("Clima frio. Risco de hipotermia se exposto por muito tempo. Agasalhe-se!")
elif temp >= 15 and temp <= 25:
    print("Clima agradável. Temperatura ideal para atividades ao ar livre.")
elif temp >= 25.1 and temp <= 35:
    print("Clima quente. Lembre-se de beber água e passar protetor solar.")
else:
    print("Alerta de calor extremo! Evite exposição ao sol e hidrate-se constantemente.")
