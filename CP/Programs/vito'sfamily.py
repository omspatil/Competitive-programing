def vito_family_distance(r, streets):
    streets.sort()
    median = streets[r // 2]
    total_distance = sum(abs(median - street) for street in streets)
    return total_distance

def main():
    t = int(input())
    for _ in range(t):
        r, *streets = map(int, input().split())
        print(vito_family_distance(r, streets))

if __name__ == "__main__":
    main()
