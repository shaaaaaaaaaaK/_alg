def perm(n): # 由於n==temp，所以全部只有兩個變數temp,p
	p = [] 
	return permNext(n, p) 

def permNext(n, p):# n == temp
	i = len(p)
	if i == len(n): 
		print(p)  
		return
	for x in n: 
		if not x in p: 
			p.append(x)    
			permNext(n, p) 
			p.pop()    
while(1):
	print('要找出字串全部的排列組合，請輸入：1')    
	print('要找出數字全部的排列組合，請輸入：2')    
	print('要退出，請輸入其他')    

	x=int(input())
	if x == 1:
		temp=str(input("輸入："))
		perm(temp)
	elif x == 2:
		a=[]
		t=int(input("輸入："))
		for i in range(t):
			a.append(i+1)
		perm(a)
	else:
		break
