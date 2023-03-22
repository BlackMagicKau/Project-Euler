# Largest palindrome product

def solution():
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if product > largest and str(product) == str(product)[::-1]:
                largest = product
    return str(largest)


if __name__ == "__main__":
    print(solution())