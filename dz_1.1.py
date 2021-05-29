duration = int(input('Время в секундах: '))
day = duration // (60 * 60 * 24)
hour = (duration - day * (60 * 60 * 24)) // (60 * 60)
minutes = (duration - day * (60 * 60 * 24) - hour * (60 * 60)) // 60
seconds = duration - day * (60 * 60 * 24) - hour * (60 * 60) - minutes * 60
print(day, 'дн', hour, 'час', minutes, 'мин', seconds, 'сек')
