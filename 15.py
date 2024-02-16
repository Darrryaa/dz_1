#15
print('Введите расстояние в сантиметрах')
sm=float(input())
dum=sm/2.54
fut=dum/12
yard=fut/3
mil=yard/1760
print(dum, 'дюймов')
print(fut, 'футов')
print(yard, 'ярдов')
print(mil, 'мили')