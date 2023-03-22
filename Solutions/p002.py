#even fibonacci numbers

def solution(): 
    a, b = 1, 2 # a is current fibo number, b is next fibo number
    total = 0
    while a < 4000000:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return str(total)

if __name__ == "__main__":
    print(solution())