write_type, var_str = input().split(' ')

def camel(w_type, v_str):
    result_str = ''
    if w_type == '2':
        str_list = v_str.split('_')
        for i in range(len(str_list)):
            if i:
                str_list[i] = str_list[i].capitalize()
            result_str += str_list[i]

    elif w_type == '3':
        result_str = v_str[0].lower() + v_str[1:]

    else:
        result_str = v_str

    print(result_str)

def snake(w_type, v_str):
    result_str = ''
    if w_type == '1':
        for i in v_str:
            if i.isupper():
                i='_'+i
            result_str += i.lower()

    elif w_type == '3':
        for idx, i in enumerate(v_str):
            if idx and i.isupper():
                i = '_'+i
            result_str += i.lower()
    else:
        result_str = v_str
    print(result_str)

def pascal(w_type, v_str):
    result_str = ''
    if w_type == '1':
        result_str = v_str[0].upper() + v_str[1:]

    elif w_type == '2':
        str_list = v_str.split('_')
        for i in str_list:
            result_str += i.capitalize()

    else:
        result_str = v_str
    print(result_str)

def run(w_type, v_str):
    camel(w_type, v_str)
    snake(w_type, v_str)
    pascal(w_type, v_str)

run(write_type, var_str)