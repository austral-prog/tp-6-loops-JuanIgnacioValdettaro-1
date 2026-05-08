# Replace the "ANSWER HERE" for your answer

def collatz_steps(n):
    """
    Retorna la cantidad de pasos necesarios para llegar a 1
    siguiendo la conjetura de Collatz:
      - Si n es par: n = n // 2
      - Si n es impar: n = 3 * n + 1

    n debe ser >= 1. Si n es 1, retorna 0 (ya esta en 1).

    Ejemplo: collatz_steps(6) -> 8
      6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (8 pasos)
    """
    i= n
    step=0
    while i != 1:
        if i % 2 == 0:
            i=i//2
        elif i % 2 == 1:
            i=3*i+1
        step=step+1
    return step # Remove this line and implement


def collatz_sequence(n):
    """
    Retorna la secuencia completa de Collatz como una lista,
    comenzando desde n y terminando en 1.

    n debe ser >= 1. Si n es 1, retorna [1].

    Ejemplo: collatz_sequence(6) -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    r=[n]
    while n!=1:
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = 3 * n + 1
        r.append(n)
    return r # Remove this line and implement
