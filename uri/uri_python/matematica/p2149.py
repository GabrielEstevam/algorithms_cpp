phill = [0, 1, 1, 1, 2, 2, 4, 8, 12, 96, 108, 10368, 10476, 108615168, 108625644, 11798392572168192, 11798392680793836]

while True:
	try:
		print(phill[int(input())-1])
	except EOFError:
		break
