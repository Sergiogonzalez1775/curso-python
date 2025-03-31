

def fibonacci_recursivo(n):
    if n <= 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def main():
    for a in range(20):
        print(fibonacci_recursivo(a))


if __name__ == "__main__":
    main()