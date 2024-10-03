from collections import deque

# FIFO First In, First Out
fila = deque([1, 2, 3, 4])
fila.append(5)
fila.append(6)
print(fila)
fila.popleft()
print(fila)
if not fila:
    print("fila vacia")
