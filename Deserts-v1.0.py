


#Работает со списком
while True:
	truf = {'темный шоколад': 150,'сливки': 70, 'ягодное или фруктовое пюре': 50, 'ликер': 1}
	zefir = {'малиновое пюре': 180, 'сахар А': 130, 'сахар Б': 180, 'белок': 35, 'вода': 100, 'агар-агар': 7, 'сироп гоюкозы': 70}
	
	print('Меню рецептов:')
	print('1.Зефир\n2.Трюфели\n')
	print('Введите порядковый номер рецепта или название. Выйти - для выхода из приложения. ')

	def rasch():
		it = []
		bl = input('Что будем готовить:\n')
		kol = int(input('Количество к изготовлению:\n'))
		if bl == 'зефир' or bl == '1':
			for i in zefir:
				zefir[i] = it.append(round(zefir[i] / 25 * kol, 2))
		elif bl == 'трюфели' or bl == '2':
			for i in truf:
				truf[i] = it.append(round(truf[i] / 15 * kol, 2))
			return (it)	
					
	x = rasch()
	print('________________________________________________________\n')
	print('Количество ингридиентов:\n')


	if len(x) == 7:
		q = x.pop(0)
		w = x.pop(0)
		e = x.pop(0)
		r = x.pop(0)
		t = x.pop(0)
		y = x.pop(0)
		u = x.pop(0)


		print('Малиновое пюре: ', q, 'гр')
		print('Сахар А: ', w, 'гр')
		print('Сахар Б: ', e, 'гр')
		print('Белок: ', r, 'гр')
		print('Вода: ', t, 'гр')
		print('Агар-агар: ', y, 'гр')
		print('Сироп глюкозы: ', u, 'гр')
		print('________________________________________________________\n')
	elif len(x) == 4:
		q = x.pop(0)
		w = x.pop(0)
		e = x.pop(0)
		r = x.pop(0)

		print('Темный шоколад (от 70%): ', q, 'гр')
		print('Сливки (от 30%): ', w, 'гр')
		print('Ягодное или фруктовое пюре: ', e, 'гр')
		print('Ликер (амаретто/бейлиз/куантро): ', r, 'ст.л.')
		print('Какао для обваливания')
		print('________________________________________________________\n')


		#Fix bugs


	#Время для добавления ссылки на сайт и редактирования кода, вперед!









#L:KJ:HBkjv;jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
#vxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
	#xvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxv
	#vxxxxxxxxxxxxxxxxxxxxxxx
	#vxxxxxxxxxxxxxxxxxxxxx#