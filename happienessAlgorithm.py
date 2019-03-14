# First implementation: Simple if/else statements

def happieness():
    user_input = raw_input(40 * "-" + " Eres feliz?" + " Imprime 'si' or 'no'. Para terminar el programa imprime q " + 40 * "-" + "\n")
    response = user_input.lower()

    if response == "yes" or response == "si":
        print(40* "-" + " continue con lo que estes haciendo " + 40 * "-" )
        happieness()

    elif response == "no":
        user_input_pregunta_2 = raw_input(40 * "-" + " Quieres ser lo?" + " Imprime 'si' or 'no' " + 45 * "-" + "\n")
        response2 = user_input_pregunta_2.lower()

        if response2 == "yes" or user_input_pregunta_2 == "si":
            print(40*"-" + " Cambia tu vida! " + 40*"-")
            happieness()

        elif response2 == "no":
            print(40*"-" + " continue con lo que estes haciendo " + 40*"-")
            happieness()

        elif response2 == "como puedo cambiar mi vida?":
            print(40 * "-" + " lastimosamente el programa no es tan avanzado de analyzar tu vida. Pero no tengas miedo y haz lo que amas! " + 40 * "-")
            happieness()

        elif response2 == "q":
            print(40*"-" + " Espero que vas a encontrar felizidad! Hasta pronto " + 40*"-")

        else:
            print(40*"-" + " El input no es valido. Intenta otra vez: " + 40*"-")
            happieness()

    elif response == "q":
            print(40*"-" + " Espero que vas a encontrar felizidad! Hasta pronto " + 40*"-")

    else:
             print(40*"-" + " El input no es valido. Intenta otra vez: " + 40*"-")
             happieness()


happieness()





