import random

import preguntas


class Trivial:

    def menu(self):

        while True:
            print('----- Elige un nivel:  -----:')
            print('1. Capitales')
            print('2. Programacion')
            print('3. Animales')
            print('4. Salir')

            try:
                opcion = int(input("Elige un nivel: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if opcion == 1:
                self.juego(1)
            elif opcion == 2:
                self.juego(2)
            elif opcion == 3:
                self.juego(3)
            elif opcion == 4:
                print('Saliendo...')
                break
            else:
                print('Introduce una opcion valida')

    def juego(self, nivel):
        lista_preguntas = preguntas.Preguntas()
        niveles = lista_preguntas.niveles()

        # Seleccionar el nivel correcto
        if nivel == 1:
            question_list = niveles[0]  # Capitales
        elif nivel == 2:
            question_list = niveles[1]  # Programación
        elif nivel == 3:
            question_list = niveles[2]  # Animales
        else:
            print("Nivel no válido.")
            return

        # para que el orden de las preguntas sean aleatorio
        random.shuffle(question_list)
        # puntos
        puntaje = 0

        for pregunta in question_list:
            print(pregunta['pregunta'])
            for opcion in pregunta['opciones']:
                print(opcion)
            respuesta_jugador = input('Elige una respuesta: ').lower().strip()
            if respuesta_jugador == pregunta['respuesta']:
                print('Correcto!\n')
                puntaje += 1
            else:
                print('Incorrecto!\n')

        print(f"Tu puntaje final es: {puntaje}/{len(question_list)}")


prueba = Trivial()
prueba.menu()
