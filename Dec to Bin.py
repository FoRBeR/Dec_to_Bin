import decimal


def binary(num: decimal.Decimal, accuracy, req_int_part=True, req_frac_part=True):
    def nearest_st(x: decimal.Decimal, acc):  # принимает числа с целой частью 0
        st = -1
        while True:
            if st * -1 > acc:
                return acc + 1, False
            if x > 2 ** st:
                return -1 * st, False
            elif x == 2 ** st:
                return -1 * st, True
            else:
                st -= 1

    if not req_int_part and not req_frac_part:  # если оба флага False, то переводятся в True т.к. такого не может быть
        req_int_part = True
        req_frac_part = True
    round_num = str(bin(num.__floor__()))[2:]  # выделение целой части и перевод ее в двоичную систему
    if not req_frac_part:
        return round_num
    num = num - num.__floor__()
    rounded_bin_num = round_num + '.'
    fraction_bin_num = []
    for i in range(accuracy):
        fraction_bin_num.append('0')
    while True:
        nearest_two, flag = nearest_st(num, accuracy)
        if nearest_two > accuracy:  # если позиция близжайшей единицы больше точности, значит она отбрасывается
            break
        fraction_bin_num[nearest_two - 1] = '1'
        if flag:  # флаг True если число перевелось без остатка
            return rounded_bin_num + ''.join(fraction_bin_num)
        num = num - decimal.Decimal(2 ** -nearest_two)
    if req_int_part:
        return rounded_bin_num + ''.join(fraction_bin_num)
    else:
        return '0.' + ''.join(fraction_bin_num)
