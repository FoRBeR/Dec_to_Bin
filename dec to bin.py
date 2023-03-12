import decimal


def binary(num: decimal.Decimal, accuracy):
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

    round_num = str(bin(num.__floor__()))[2:]  # выделение целой части и перевод ее в двоичную систему
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
    return rounded_bin_num + ''.join(fraction_bin_num)

