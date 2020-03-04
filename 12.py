import random
r = random.randint(1,100)
while True:
	a = input('请输入')
	a = int(a)
	if a == r:
		print('对了')
		break
	elif a > r:
		print('大了')
	elif a < r:
		print('小了')
