formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('One', 'Two', 'Three', 'Four'))
print(formatter.format(True, False, False, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	" One may say\n",
	"What one never does\n",
	"But if everyone does in fact can\n",
	"Potato"))