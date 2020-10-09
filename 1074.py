N, r, c = map(int, input().split())
# r : row
# c : column
def z_function(line, x, y):
    result = 0
    if line == 1:
        return result

    line = line // 2
    # (0,0) (0,1) (1,0) (1,1)
    #  0    1     2     3
    for i in range(2):
        for j in range(2):
            if x < line * (i+1) and y < line * (j+1):
                return (i*2+j) * line * line + z_function(line, x-line*i, y-line*j)

print(z_function(2**N, r, c))