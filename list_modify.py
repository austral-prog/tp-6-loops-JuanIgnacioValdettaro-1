# Replace the "ANSWER HERE" for your answer

def put(value, lst):
    """
    Coloca value en el primer lugar vacio ("") que encuentre en lst
    y retorna el indice donde lo coloco.
    Si no hay ningun lugar vacio, retorna -1.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "", "Green"]
        put("Blue", colors) -> 1
        # colors ahora es ["Red", "Blue", "Green"]
    """
    f=-1
    i=0
    while i < len(lst) and f == -1:
        if lst[i] == "":
           lst[i] = value
           f = i
        i+=1
    return f

    return "ANSWER HERE"  # Remove this line and implement


def remove(value, lst):
    """
    Busca todas las ocurrencias de value en lst, las reemplaza por ""
    y retorna la cantidad de eliminaciones realizadas.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "Green", "Red", "Blue"]
        remove("Red", colors) -> 2
        # colors ahora es ["", "Green", "", "Blue"]
    """
    v=0
    i=0
    while i < len(lst):
        if lst[i] == value:
           lst[i]=""
           v+=1
        i+=1
    return v  # "ANSWER HERE"  # Remove this line and implement
