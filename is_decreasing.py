def is_decreasing(num_list):
    length = len(num_list)
    if length == 1:
        return True
    elif num_list[0] > num_list[1]:
        temp = num_list[1]
        num_list[1] = num_list[0]
        num_list[0] = temp
        num_list.pop(1)
        return is_decreasing(num_list)

    else:
        return False


list1 = [10, 5, 3, 10]

print(is_decreasing(list1))