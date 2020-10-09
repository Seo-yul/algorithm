def do_sort(students):
    students.reverse()
    sorted_students = sorted(students, key=lambda info: info[1], reverse=True)
    return sorted_students


def get_list(func):
    def decorated(students):
        sorted_students = do_sort(students)
        return func(sorted_students)

    return decorated


@get_list
def print_output(each_student):
    output = []
    for i in each_student:
        if i[2] == 'a':
            output.append('Good A: {}'.format(i[0]))
        elif i[2] == 'b':
            output.append('Great B: {}'.format(i[0]))
        else:
            output.append('Best C: {}'.format(i[0]))
    return output


students = [['Paul', 90, 'a'], ['Michael', 50, 'b'], ['Gina', 90, 'c'], ['Marie', 70, 'b']]
print(*print_output(students), sep='\n')