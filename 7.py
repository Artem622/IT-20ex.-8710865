k=0
min=11755
for i in range(5913,11754):
    if i%5==0 and i%11==0 and i%7!=0 and i%10!=0 and i%13!=0 and i%22!=0:
        k+=1
        if i<min:
            min=i
print(k,min)
"""ассматривается множество целых чисел, принадлежащих числовому отрезку
[5913; 11753], которые делятся на 5 и 11 и не делятся на 7, 10, 13, 22.
Найдите количество таких чисел и минимальное из них. В ответе запишите два
целых числа без пробелов и других дополнительных символов: сначала количество,
затем минимальное число."""
