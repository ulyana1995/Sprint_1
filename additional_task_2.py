def digit_root(num):
    is_finished = False
    num_str = str(num)
    total_amount = 0
    while is_finished != True:
        for i in range(len(num_str)):
            total_amount+= int(num_str[i])
        if total_amount > 9:
            num_str = str(total_amount)
            total_amount = 0
        else:
            is_finished = True
    return total_amount

number = 97569
print(digit_root(number))