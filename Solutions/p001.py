# multiples of 3 or 5

def solution():
    return str(sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))
    
if __name__ == "__main__":
    print(solution())
