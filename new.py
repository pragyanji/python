lst1 = [1,4,6,8,3,9,12,45]
def even_sum(lst):
    summ = 0
    for i in lst:
        if i % 2 == 0:
            summ += i
    return summ
       
print(f'sum of even number:{even_sum(lst1)}')