import random

i = input('請輸入第一個數字: ')
j = input('請輸入第二個數字: ')
i, j = int(i), int(j)
count = 0
r = random.randint(i, j)
while True:
	count = count + 1
	guess = input('請猜一個數字: ')
	guess = int(guess)
	if guess == r:
		print('終於猜對了!總共猜了', count, '次!')
		break
	elif guess > r:
		print('比答案大。總共猜了', count, '次!')
	else:
		print('比答案小。總共猜了', count, '次!')