def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Sintaxis Básica y Operaciones Simples")
        print("2. Condicionales y Bucles")
        print("3. Listas y Diccionarios")
        print("4. Calculadora Básica")
        print("5. Juego de Adivinanza")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Hola, bienvenido a la actividad de Python básico.")
            num1 = 10
            num2 = 20.5
            mensaje = "Suma total: "
            suma = num1 + num2
            print(mensaje + str(suma))
            nombre = input("¿Cómo te llamas? ")
            edad = input("¿Cuántos años tienes? ")
            print("Hola, " + nombre + ", tienes " + edad + " años.")

        elif opcion == "2":
            numero = int(input("Ingresa un número: "))
            if numero % 2 == 0:
                print("El número es par.")
            else:
                print("El número es impar.")
            numeros = [1, 2, 3, 4, 5]
            print("Cuadrados de los números:")
            for n in numeros:
                print(f"{n}^2 = {n**2}")
            while True:
                palabra = input("Escribe 'salir' para terminar: ")
                if palabra.lower() == 'salir':
                    print("¡Hasta luego!")
                    break

        elif opcion == "3":
            estudiantes = ["Ana", "Luis", "Pedro", "Carla"]
            print("Lista de estudiantes:")
            for estudiante in estudiantes:
                print(estudiante)
            contactos = {"Ana": "ana@gmail.com", "Luis": "luis@gmail.com"}
            print("Contactos:")
            for nombre, correo in contactos.items():
                print(f"Nombre: {nombre}, Correo: {correo}")
            nuevo_estudiante = input("Ingresa un nuevo estudiante: ")
            estudiantes.append(nuevo_estudiante)
            print("Lista actualizada de estudiantes:", estudiantes)
            nuevo_nombre = input("Ingresa un nombre para actualizar su correo: ")
            nuevo_correo = input("Ingresa el correo: ")
            contactos[nuevo_nombre] = nuevo_correo
            print("Contactos actualizados:", contactos)

        elif opcion == "4":
            def calculadora():
                print("Calculadora básica")
                while True:
                    print("Opciones: suma, resta, multiplicacion, division, salir")
                    operacion = input("Elige una operación: ").lower()
                    if operacion == "salir":
                        print("¡Hasta luego!")
                        break
                    num1 = float(input("Ingresa el primer número: "))
                    num2 = float(input("Ingresa el segundo número: "))
                    if operacion == "suma":
                        print(f"Resultado: {num1 + num2}")
                    elif operacion == "resta":
                        print(f"Resultado: {num1 - num2}")
                    elif operacion == "multiplicacion":
                        print(f"Resultado: {num1 * num2}")
                    elif operacion == "division":
                        if num2 != 0:
                            print(f"Resultado: {num1 / num2}")
                        else:
                            print("Error: división entre cero.")
                    else:
                        print("Operación no válida.")
            calculadora()

        elif opcion == "5":
            import random
            numero_secreto = random.randint(1, 100)
            print("Adivina el número secreto entre 1 y 100")
            while True:
                intento = int(input("Tu intento: "))
                if intento < numero_secreto:
                    print("El número secreto es mayor.")
                elif intento > numero_secreto:
                    print("El número secreto es menor.")
                else:
                    print("¡Felicidades! Adivinaste el número.")
                    break

        elif opcion == "6":
            print("Este programa fue realizado por Roberto Guillot.")
            print("¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu()
