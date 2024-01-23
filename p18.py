import utils

""" 
This requires a 'clever' solution involving dynamic programming: 
1. modify the existing array by replace the values with the 
    evaluated local maxima 
2. continuing this process will eventually create the maximum value 
    at the first row of the triangle  



trivial example 
3
7 4
2 4 6
8 5 9 3

           [0][0]
       [1][0], [1][1]
   [2][0], [2][1], [2][2]
[3][0], [3][1], [3][2], [3][3]

[2][0] -> {[3][0], [3][1]} 
[2][1] -> {[3][1], [3][2]} 
...
[1][0] -> {[2][0], [2][1]} 
...
[r][c] -> {[r+1][c], [r+1][c+1]}

"""

triangle_grid_text = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle_grid_arr = utils.parse_grid(triangle_grid_text)


def max_path_sum(triangle_grid_arr):
    rows = len(triangle_grid_arr)
    for r in range(rows - 1, -1, -1):
        cols = len(triangle_grid_arr[r])
        for c in range(cols):
            if r < rows - 1:
                """ start calculating the max val the second last row """
                tmp_max = triangle_grid_arr[r][c] + max(triangle_grid_arr[r + 1][c], triangle_grid_arr[r + 1][c + 1])
                triangle_grid_arr[r][c] = tmp_max
    return triangle_grid_arr[0][0]

# print(max_path_sum(triangle_grid_arr)) 1074
