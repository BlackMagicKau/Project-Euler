# Smallest Multiple

def solution():
    n = 20
    i = 1
    while True:
        if all(i % j == 0 for j in range(1, n + 1)):
            return str(i)
        i = i + 1

if __name__ == "__main__":
    print(solution())