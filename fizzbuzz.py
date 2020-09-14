# 1
# 2
def main():
    for i in range(1, 101):
        if i == 42:
            print("Answer to the Ultimate Question of Life, the Universe, and Everything")
        else:
            if i % 3 == 0:
                print("Fizz", end="")
            if i % 5 == 0:
                print("Buzz", end="")
            if i % 3 != 0 and i % 5 != 0:
                print(i, end="")
            print()


if __name__ == '__main__':
    main()
