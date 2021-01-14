# factorial

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)




def main():

    numero = int(input("Introduce numero: "))

    print("El factorial del ", numero, "es :", factorial(numero))



if __name__ == '__main__':
    main()