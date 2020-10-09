T = int(input())


def divide_action(list_pra, list_len) -> (list, tuple):
    tmp_list = [0]*list_len
    for i in range(list_len):
        tmp_list[i] += list_pra[i] // 2
        if i == list_len-1:
            tmp_list[0] += list_pra[i] // 2
        else:
            tmp_list[i+1] += list_pra[i] // 2
    return tmp_list


def check_even(list_pra, list_len) -> list:
    tmp_list = list_pra
    for i in range(list_len):
        if tmp_list[i] % 2 == 1:
            tmp_list[i] += 1
    return tmp_list


def is_same_candy(list_pra) -> bool:
    set_pra = set(list_pra)
    if len(set_pra) == 1:
        return True
    else:
        return False


for _ in range(T):
    child_count = int(input())
    candy_count_list = list(map(int, input().split(' ')))
    flag_bool = False
    result = 0

    while not flag_bool:
        check_rote = False
        candy_count_list = check_even(candy_count_list, child_count)
        if not result:
            flag_bool = is_same_candy(candy_count_list)
            if flag_bool:
                break
        candy_count_list = divide_action(candy_count_list, child_count)
        candy_count_list = check_even(candy_count_list, child_count)
        flag_bool = is_same_candy(candy_count_list)
        result += 1

    print(result)