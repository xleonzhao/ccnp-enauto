#!/usr/bin/env python3

def print_2d_array(arr, n):
    for i in range(n):
        print(arr[i])

def main(n):
    min_row, max_row = 0, n - 1
    min_col, max_col = 0, n - 1
    i, j, dir = 0, 0, 0  # 0: right; 1: down; 2: left; 3: up
    spiral = [[0] * n for _ in range(n)]

    for k in range(n * n):
        spiral[i][j] = k
        print("[DEBUG] {}:{} = {}, dir={}".format(i, j, k, dir))
        
        if dir == 0:  # right
            if j < max_col:
                j += 1
            else:
                dir = 1
                min_row += 1
                i += 1
        elif dir == 1:  # down
            if i < max_row:
                i += 1
            else:
                dir = 2
                max_col -= 1
                j -= 1
        elif dir == 2:  # left
            if j > min_col:
                j -= 1
            else:
                dir = 3
                max_row -= 1
                i -= 1
        elif dir == 3:  # up
            if i > min_row:
                i -= 1
            else:
                dir = 0
                min_col += 1
                j += 1

    print_2d_array(spiral, n)
    return spiral

if __name__ == "__main__":
    res = main(8)
