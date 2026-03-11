nombre_jugador = input("Escribe tu nombre!: ")
respuestas = 0
pregunta1="paris"
pregunta2="bruselas"
pregunta3="marte"
pregunta4="lobo"

print("=================================")
print("                                 ")
print("                                 ")
print(f"   ¡BIENVENIDO, {nombre_jugador}!   ")
print("                                 ")
print("                                 ")
print("=================================")
print("                                 ")
print("Prepárate para jugar y divertirte.")
print("                                 ")
print("=================================")

def validacion_respuestas(respuesta_ingresada, respuesta_establecido, respuesta_valor):
    if respuesta_ingresada == respuesta_establecido:
        print("Correcto")
        respuesta_valor = respuesta_valor + 1
    else:
        print("Incorrecto")

print("1ra Pregunta...")
print("¿Capital de Francia?")
Respuesta_1 = input("Ingrese su respuesta".lower)
validacion_respuestas(Respuesta_1, pregunta1, respuestas)
print("2da Pregunta...")
print("¿Capital de Bélgica?")
Respuesta_2 = input("Ingrese su respuesta".lower)
validacion_respuestas(Respuesta_2, pregunta2, respuestas)
print("3ra Pregunta...")
print("¿Planeta Rojo?")
Respuesta_3 = input("Ingrese su respuesta".lower)
validacion_respuestas(Respuesta_3, pregunta3, respuestas)
print("4ta Pregunta...")
print("¿Animal que aulla?")
Respuesta_4 = input("Ingrese su respuesta".lower)
validacion_respuestas(Respuesta_4, pregunta4, respuestas)

if respuestas == 5:
    print('Felicidades, EXCELENTE')
elif respuestas == 4:
    print('Felicidades, muy bueno')
elif respuestas == 3:
    print('Felicidades, pasaste')
elif respuestas == 2:
    print('mal')
elif respuestas == 1:
    print('horrible')
else:
    print('PESIMO')