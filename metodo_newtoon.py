def get_all_arrays(func_grade):
    array_ret = []
    array = list(range(func_grade+1))
    for i in range(func_grade):
        array_ret.append(split_array(array, i+1))
    return array_ret


def split_array(array, number):
    cont_inf = 0
    cont_sup = number + 1
    arrays = []
    while len(array) >= cont_sup:
        arrays.append(array[cont_inf:cont_sup])
        cont_inf += 1
        cont_sup += 1
    return arrays


def calculate_divided_diff(value, x, y, data_set):
    arr_len = len(value)
    data_saved = data_set.get(str(value))
    if data_saved:
        return data_saved
    if arr_len == 2:
        data = ((y[value[1]]-y[value[0]])/(x[value[1]]-x[value[0]]))
        data_set[str(value)] = data
        return data
    last_values = split_array(value, arr_len-2)
    data = (calculate_divided_diff(last_values[1], x, y, data_set)-calculate_divided_diff(
        last_values[0], x, y, data_set))/(x[value[len(value)-1]]-x[value[0]])
    data_set[str(value)] = data
    return data


def calculate_mul(x, array, cont):
    if(cont == 1):
        return x-array[0]
    return (x-array[cont-1])*calculate_mul(x, array, cont-1)


def divided_diff(array_diffs, x, y, x_to):
    data_set = {}
    used_diff = []
    acum = y[0]
    cont = 1
    for i in array_diffs:
        first = True
        for indexes in i:
            div_diff = calculate_divided_diff(indexes, x, y, data_set)
            if first:
                used_diff.append(div_diff)
                first = False
                acum += calculate_mul(x_to, x, cont)*div_diff
                cont += 1
    return acum


#array = split_array([0, 1, 2, 3], )
# print(array)
array = get_all_arrays(4)
x = [1, 3, 4, 6, 5]
y = [0, 1.098612289, 1.386294, 1.791759, 1.609438]
ret = divided_diff(array, x, y, 7)
print(ret)
#print(calculate_mul(2, x, 3))
