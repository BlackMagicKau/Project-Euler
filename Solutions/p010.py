# Summation of Primes

def solution():
    primes = [2]
    for i in range(3, 2000000, 2):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return sum(primes)
    

if __name__ == "__main__":
    print(solution())
