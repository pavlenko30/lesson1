tainted_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in tainted_list:
    print('Привет', position.split()[-1].capitalize())
