#產生一個隨機數字1~100(不要印出來)
#讓使用這重複輸入數字去猜
#猜對的話 印出"終於猜對"
#猜錯的話 要告訴他 比答案大/小

import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
   count = count + 1
   num = input('請猜數字: ')
   num = int(num)
   if num == r :
   	print('你猜中了!')
   	print('這是猜的第',count,'次')
   	break
   elif num > r:
   	print('比答案大')
   elif num < r:
   	print('比答案小')
   print('這是猜的第',count,'次')