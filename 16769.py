pod_key = [0, 0, 0]
pod_val = [0, 0, 0]

for i in range(3):
    pod_key[i],  pod_val[i] = map(int, input().split(' '))

check_max0 = 0
check_max1 = 0
check_max2 = 0

for i in range(1, 101):

    if i%3 == 1:
        if pod_key[0] == pod_val[0]:
            check_max0 += 1

        milk = pod_val[1] + pod_val[0]

        if milk > pod_key[1]:
            pod_val[0] = milk - pod_key[1]
            pod_val[1] = pod_key[1]

        else:
            pod_val[0] = 0
            pod_val[1] = milk

    elif i%3 == 2:
        if check_max0 == check_max1 == 5:
            break
        if check_max0 == check_max2 == 5:
            break
        if check_max1 == check_max2 == 5:
            break

        if pod_val[1] == pod_key[1]:
            check_max1 += 1

        milk = pod_val[2] + pod_val[1]
        if milk > pod_key[2]:
            pod_val[1] = milk - pod_key[2]
            pod_val[2] = pod_key[2]

        else:
            pod_val[1] = 0
            pod_val[2] = milk

    else:
        if pod_val[2] == pod_key[2]:
            check_max2 += 1

        milk = pod_val[0] + pod_val[2]
        if milk > pod_key[0]:
            pod_val[2] = milk - pod_key[0]
            pod_val[0] = pod_key[0]

        else:
            pod_val[2] = 0
            pod_val[0] = milk

for i in pod_val:
    print(i)