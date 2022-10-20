def large(arr):
    max_ = arr[0]
    for a in arr:
        if a > max_:
            max_ = a
    return max_
def small(ary):
    min_ = ary[0]
    for b in ary:
        if b < min_:
         min_ = b
    return min_

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(large(new_lst) - small(new_lst))


