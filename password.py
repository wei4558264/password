# 設定密碼測試程式
password = 'a123456'
ans = input('請輸入密碼:')
x = 0
while x < 3:
	if ans == 'a123456':
		print('恭喜你!密碼正確!')
		break
	else:
		x = x+1
		if x < 3:
			print('密碼錯誤!')
			print('你還有 ', 3-x, '次的機會')
			ans = input('請輸入密碼:')
		else:
			print('很抱歉!你必須離開')
   