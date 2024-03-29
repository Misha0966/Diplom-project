begin
	# Находим объем наземной части муравейника
	r= 0.26
	h= 0.12
	Vn = ((π * h)/6)*(3*r^2+h^2)
	println("объём наземной части муравейника", Vn)
	
	# Находим объем подземной части муравейника
	Vp = 2/3 * Vn
	println("объём подземной части муравейника", Vp)
	
	# Находим общий объем всего муравейника
	Vreal = Vn + Vp
	println("общий объём всего муравейника", Vreal)
	
	# Находим размер выборки
	Na = sum([0.003, 0.003, 0.003, 0.003, 0.01, 0.003, 0.004, 0.003, 0.004, 0.003]) / 10
	println("размер выборки", Na)
	
	# Находим объем выборки
	Vna = Na * 10^-6
	println("объём выборки", Vna)
	
	# Находим число муравьёв, которые живут в данном муравейнике
	X = (Vreal / Vna) / 10

	# Округляем результат до целой части
    X_rounded = round(X)
	println("число муравьёв, которые живут в данном муравейнике:", X_rounded)
end
