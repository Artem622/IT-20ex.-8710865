x=0
for i in range(245690,245757):
    x+=1
    k=0
    A=[]
    for a in range(2,i//2+1):
        if i%a==0:
            k+=1
            if k>1:
                break
    if k==0:
        A.append(i)
        print(x,*A)

"""Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
отрезку [245 690; 245 756] простые числа. Выведите на экран все найденные
простые числа в порядке возрастания, слева от каждого числа выведите его
порядковый номер в последовательности. Каждая пара чисел должна быть выведена
в отдельной строке.
"""

