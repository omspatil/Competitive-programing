def count_adjacent_mines(field, row, col, n, m):
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < n and 0 <= c < m and field[r][c] == '*':
            count += 1
    return count

def process_field(field, n, m):
    result = []
    for i in range(n):
        row = ""
        for j in range(m):
            if field[i][j] == '*':
                row += '*'
            else:
                count = count_adjacent_mines(field, i, j, n, m)
                row += str(count)
        result.append(row)
    return result

def main():
    field_number = 1
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        if field_number > 1:
            print()  # Empty line between field outputs
        
        field = [input() for _ in range(n)]
        
        result = process_field(field, n, m)
        
        print("Field #{}:".format(field_number))
        for row in result:
            print(row)
        field_number += 1

if __name__ == "__main__":
    main()
