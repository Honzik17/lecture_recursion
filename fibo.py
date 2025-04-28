def recursive_nth_fibo(poradi):
    if poradi == 0:
        return 0
    elif poradi == 1:
        return 1
    else:
        return recursive_nth_fibo(poradi - 1) + recursive_nth_fibo(poradi - 2)

def main():
    cislo = input("Napiš kolik chceš čísel bro ")
    emoji = [0, 1]
    for i in range(2, int(cislo)+1):
        emoji.append(recursive_nth_fibo(i))
    print(emoji)
    pass


if __name__ == "__main__":
    main()
