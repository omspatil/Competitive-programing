import sys

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def reverse_and_add(num):
    iterations = 0
    while not is_palindrome(num):
        num += int(str(num)[::-1])
        iterations += 1
    return iterations, num

def main():
    for line in sys.stdin:
        N = int(line.strip())
        for _ in range(N):
            P = int(input())
            iterations, palindrome = reverse_and_add(P)
            print(f"{iterations} {palindrome}")

if __name__ == "__main__":
    main()
