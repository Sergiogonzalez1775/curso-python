def fibonacci(n):
    a = 0
    b = 1

    for a in range(n):
        c = a + b
        a = b
        b = c
    return b


def main():
    for a in range(20):
        print(fibonacci(a))


if __name__ == "__main__":
    main()