def ten_to_q(number, q):
    '''Переводит из 10-ой СС в Q-ую СС(на вход получаем значение 'int')'''
    osts = []
    while number > 0:
        number_2  = (number // q) * q
        ost = number - number_2
        number = number_2 // 2
        osts.append(ost)
    return osts


def revers_number(list):
    '''Получает строчноне значение списка переворачивает его и приводит к строчной записи'''
    sistem_number = []
    for i in list[::-1]:
        sistem_number.append(i)
    sistem_number_2 = [str(i) for i in sistem_number]
    result = ''.join(sistem_number_2)
    return result


def revers_g_and_v_cherez_spisok(number_user, g, v):
    rezerv = number_user
    digits = []
    count = 0
    while rezerv > 0:
        x = rezerv % 10
        digits.append(x)
        count += 1
        rezerv = rezerv // 10
    a = digits[v]
    digits[v] = digits[g]
    digits[g] = digits[v]
    digits = [str(i) for i in digits]
    new_number = ''.join(digits)
    return new_number

def revers_0_and_2_cherez_delenie(number):
    '''Меняет числа 0-ой и 2-ой позиции через деление числа.'''
    count = 0
    rezerv = number
    while number > 0:
        count += 1
        number = number // 10
    a = rezerv // (10 ** (count-1))
    b = rezerv // (10 ** (count-2))
    b = b % (10 ** (count-1))
    c = rezerv % (10 ** (count-1))
    c = c // (10 ** (count-2))
    d = rezerv % (10 ** (count-3))
    new_number = c * (10 ** (count-1))
    new_number = new_number + (b * (10 ** (count-2))) + (a * (10 ** (count-3))) + d
    return new_number


def revers_g_and_v(user_list, v, g):
    '''Меняет местами G-ое число и V-ое через списочное выражение.'''
    new_list =[]
    for i in user_list:
        a = str(i)
        q = list(a)
        number_v = q[v]
        number_g = q[g]
        q[g] = number_v
        q[v] = number_g
        q = ''.join(q)
        new_list.append(q)
    return new_list

z = [1243, 13434, 5432, 3543, 453434, 5346]
binary_number = [revers_number(ten_to_q(i,2)) for i in z]
print(revers_g_and_v(z, 1, 3))
print(revers_g_and_v_cherez_spisok(154545, 1, 4))