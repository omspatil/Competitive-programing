import math

def fibonacci(n):
    f = [1, 2]
    while f[-1] <= n:
        f.append(f[-1] + f[-2])
    return f

def main():
    f = fibonacci(10**100)
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        count = sum(1 for x in f if a <= x <= b)
        print(count)

if __name__ == "__main__":
    main()
