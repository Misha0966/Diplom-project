"""Дипломная работа.
"""

#Для рассчёта кол-ва муравьёв, потребуются данные  добытые в реаль-ной жизни​
# А именно: форма муравейника, вид муравьёв, и размерности гнезда.​
# Форма муравейника определяется визуально и напоминает сферический фрагмент.
# Вид муравьёв определяется так же на глаз и относится к самому распространённому виду:​
# Чёрный садовый муравей(он же Lasius niger)​
# В ходе замерительных и измерительных мероприятий были полученные следующие данные:​
# Радиус муравейника 0.28 м, высота 0.12 м, а так же замеры каждого муравья, при выборки = 10​
# которые составили: 0.3, 0.3, 0.3, 0.3, 1, 0.3, 0.4, 0.3, 0.4, 0.3.​
# где 1 см- размер матки муравейника, согласно данным Википедии.​

r = 0.26  # радиус муравейника​
h = 0.12  # высота муравейника​
Vn = ((3.14*h)/6)*(3*r**2+h**2)   # объем наземной части муравейника, где r - радиус муравейника, а h - его высота​
Vp = 2 / 3 * Vn  # объем поземной части муравейника​
Vreal = Vn + Vp  # где Vn - объем наземной части, а Vp - объем поземной части​
print("Общий объем муравейника: ", Vreal)

# Опредилим размер выборки​
Na = (0.003 + 0.003 + 0.003 + 0.003 + 0.01 + 0.003 + 0.004 + 0.003 + 0.004 + 0.003) / 10
print("Размер выборки: ", Na)

# Определим объём выборки​

VNa= (Na*(10**(-6)))

print("Объем выборки: ", VNa)

# Определим кол-во муравьёв живущих в муравейнике​
x = (Vreal / VNa)/10

print("Общий объем муравейника: ", Vreal)

# Окрулим до целой части:
rounded_x = round(x)
print("Общее количество муравьев: ", rounded_x)
