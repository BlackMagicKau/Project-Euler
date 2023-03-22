# 10001st prime

def solution():
    n = 10001
    primes = [2]
    i = 3
    while len(primes) < n:
        if all(i % j != 0 for j in primes):
            primes.append(i)
        i = i + 2
    return str(primes[-1])

if __name__ == "__main__":
    print(solution())
