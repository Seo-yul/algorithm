def do_sort(students):
    students.reverse()
    sorted_list = sorted(students, key=lambda info: info[1], reverse=True)
    return sorted_list


 
def print_outputs(students):    
    for info in students:
        if info[2] == 'a':
            print('Good A: {}'.format(info[0]))
        elif info[2] == 'b':
            print('Great B: {}'.format(info[0]))
        else:
            print('Best C: {}'.format(info[0]))
 
students = [['Paul', 90, 'a'], ['Michael', 50, 'b'],['Gina', 90, 'c'],['Marie', 70, 'b']]
 
sorted_students = do_sort(students)
print_outputs(sorted_students)
