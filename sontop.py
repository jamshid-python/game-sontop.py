# Son topish o'yini

import random as r
print("Siz bilan son topish o'yinini o'ynaymiz.")
harakat = 1
son_r = r.randint(1, 10)
top = print("Men 1 dan 10 gacha son o'yladim."
	        "Shu sonni topishga harakat qiling: ")
while True:
	top = int(input(""))
	harakat = harakat + 1
	if top != son_r:
		print("Qaytadan urining")
	if top > son_r:
		top = int(input("Men o'ylagan son kichikroq: "))
	if top < son_r:
		top = int(input("Men o'ylagan son kattaroq: "))
	if son_r == top:
		print(f"Siz {harakat} urinishda topdiningiz")		
		break
print("Biror son o'ylang men topaman")
quyi = 1
chegara = 10
tahminlar_pc = 1
input("Son o'yladingizmi: ")
while True:
	if quyi != chegara:
		tahminlar_pc += 1
		son_pc = r.randint(quyi, chegara)
		javob = input(f"Siz o'ylagan son {son_pc}mi. Katta bo'lsa(1), Kichik bo'lsa(2), to'g'ri bo'lsa T ni bosing:  ")
		if javob == "1":
			quyi = son_pc + 1

		elif javob == "2":
			chegara = son_pc - 1
		else:
			break 
			print("Topdim")
if tahminlar_pc > harakat:
	print(f"Siz {harakat} urinishda topdingiz")
	print(f"Men esa {tahminlar_pc} urinishda topdim ")
	print("Siz yutdingiz")
if tahminlar_pc < harakat:
	print(f"Siz {harakat} urinishda topdingiz")
	print(f"Men esa {tahminlar_pc} urinishda topdim ")
	print("Siz yutdingiz! Tabriklayman")
if harakat == tahminlar_pc:
	print(f"Siz ham men ham (harakat) urinishda topdik")
	print("Durrang") 
