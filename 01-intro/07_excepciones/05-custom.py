class ErrorCustom(Exception):
    "Esta clase es para representar errores"

    # def __init__(self, *args: object) -> None:
    #     super().__init__(*args)

    def __init__(self, msg, code) -> None:
        self.msg = msg
        self.code = code

    def __str__(self) -> str:
        return f"{self.msg} - codigo de error: ({self.code})"


def division(n=0):
    if n == 0:
        raise ErrorCustom("Cannot divide by 0", 805)

    return 5/n


try:
    division()
except ErrorCustom as e:
    print(e)
