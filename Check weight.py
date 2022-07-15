while True:
     ves=int(input('Введите свой вес, кг: '))
     rost=int(input('Введите свой рост, см: '))
     r=int((rost - 115)*1.15)
     raz = int()
     if r == ves:
          print('У тебя идеальное соотношение роста и веса, поздравляю!')
     elif r > ves:
          raz = r-ves
          print ('Тебе нужно набрать ', raz,'кг.')
     elif r < ves:
          raz = ves-r
          print ('Тебе нужно скинуть ', raz,'кг.')    



