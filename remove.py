seconds = [1.23, 1.45, 1.02, 1.11]
elementos_a_eliminar = [1.45, 1.02, 1.11]

for elemento in elementos_a_eliminar:
    seconds.remove(elemento)

print(seconds)