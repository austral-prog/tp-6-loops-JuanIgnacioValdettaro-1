# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    r=[]
    for f in matrix:
        for val in f:
            r.append(val)

    return r # Remove this line and implement


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    r=[]
    for f in matrix:
        total=0
        for val in f:
            total+=val
        r.append(total)
    return r  # Remove this line and implement


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    result = []
    if len(matrix) > 0:
        for col in range(len(matrix[0])):
            total = 0
            for row in range(len(matrix)):
                total += matrix[row][col]
            result.append(total)
    return result # Remove this line and implement
