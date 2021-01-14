# fibonacci 0 1 1 2 3 5 8 13


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    numero = int(input("Introduce numero: "))

    for x in range(numero):
        print(fibonacci(x), end=" ")



if __name__ == '__main__':
    main()
