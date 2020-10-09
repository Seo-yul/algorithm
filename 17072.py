def intensity (R, G, B):
    result = (2126*R)+(7152*G)+(722*B)
    if 0 <= result < 510000:
        return '#'
    elif 510000 <= result < 1020000:
        return 'o'
    elif 1020000 <= result < 1530000:
        return '+'
    elif 1530000 <= result < 2040000:
        return '-'
    else:
        return '.'

N, M = map(int, input().split(' '))
for line in range(N):
    color_list = list(map(int, input().split(' ')))
    line_text = ''
    for i in range(M):
        R = color_list[(3*i)]
        G = color_list[(3*i)+1]
        B = color_list[(3*i)+2]

        line_text += intensity(R, G, B)
    print(line_text)




