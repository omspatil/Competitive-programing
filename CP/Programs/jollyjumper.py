def is_jolly(sequence):
    n = len(sequence)
    if n == 1:
        return True
    
    diff_set = set()
    for i in range(1, n):
        diff = abs(sequence[i] - sequence[i-1])
        if diff == 0 or diff >= n or diff in diff_set:
            return False
        diff_set.add(diff)
    return True

def main():
    while True:
        try:
            line = input().split()
            n = int(line[0])
            sequence = list(map(int, line[1:]))
            if is_jolly(sequence):
                print("Jolly")
            else:
                print("Not jolly")
        except EOFError:
            break

if __name__ == "__main__":
    main()
