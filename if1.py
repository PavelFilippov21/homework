x = int(input("Возраст:"))
def lines(a):
    if a < 7:
        return ("малой")
    if a <= 18:
        return ("Школьник")
    if a <= 24:
        return ("студент")
    return ("Работает")
print(lines(x))