a = ['Ace Of Base - All That She Wants', 'No Doubt - Dont Speak', 'Bad Boys Blue - Youre A Woman', 'E-type - Angels Crying', 'Haddaway - What is love']
print('Введите плей-лист папы:')
for i in range(len(a)):
    print(a[i])
print('Введите плей-лист мамы:')
reversed_a = a[::-1]
for i in range(len(reversed_a)):
    print(reversed_a[i])
