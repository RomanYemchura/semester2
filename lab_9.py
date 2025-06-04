from collections import defaultdict

def read_file():
    with open("ijones_in.txt", "r") as f:
        width, height = map(int, f.readline().split())
        grid = [list(f.readline().strip()) for col in range(height)]
    return width, height, grid

def solve(width, height, grid):
    paths = [[0] * width for row in range(height)]
    letter_positions = defaultdict(list)

    for col in range(height):
        for row in range(width):
            letter = grid[col][row]
            letter_positions[letter].append((col, row))

    for col in range(height):
        paths[col][0] = 1

    for row in range(width):
        jump_sums = defaultdict(int)

        for col in range(height):
            letter = grid[col][row]
            jump_sums[letter] += paths[col][row]

        for col in range(height):
            if row + 1 < width:
                paths[col][row + 1] += paths[col][row]

        for letter in jump_sums:
            for y, x in letter_positions[letter]:
                if x > row:
                    paths[y][x] += jump_sums[letter]

    result = sum(paths[col][width - 1] for col in range(height))
    return result

def write_result(result):
    with open("ijones_out.txt", "w") as f:
        f.write(str(result) + "\n")

def main():
    width, height, grid = read_file()
    result = solve(width, height, grid)
    write_result(result)

if __name__ == "__main__":
    main()
