def find_words(grid, words):
    dirs = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    word_positions = {word: [] for word in words}
    
    for word in words:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].lower() == word[0].lower():
                    for dx, dy in dirs:
                        cur, nx, ny = 1, i + dx, j + dy
                        while 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and cur < len(word) and grid[nx][ny].lower() == word[cur].lower():
                            cur += 1
                            nx, ny = nx + dx, ny + dy
                        if cur == len(word):
                            word_positions[word].append((i + 1, j + 1))
                            break
                    if word_positions[word]:
                        break
    return word_positions

def main():
    t = int(input())
    for _ in range(t):
        input()  # Consume the empty line
        m, n = map(int, input().split())
        grid = [input() for _ in range(m)]
        k = int(input())
        words = [input() for _ in range(k)]

        word_positions = find_words(grid, words)

        for word in words:
            x, y = word_positions[word][0]
            print(x, y)
        
        if _ < t - 1:
            print()

if __name__ == "__main__":
    main()
