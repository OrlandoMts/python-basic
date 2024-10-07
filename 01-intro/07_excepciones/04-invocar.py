def division(n=0):
    if n == 0:
        raise ZeroDivisionError("Cannot divide by 0", f"{n}")

    return 5/n


try:
    division()
except ZeroDivisionError as e:
    print(e)
