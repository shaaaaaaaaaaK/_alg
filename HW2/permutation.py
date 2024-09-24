def perm(n):
	p = [] 
	return permNext(n, p) 

def permNext(n, p):
	i = len(p)
	if i == len(temp): 
		print(p)  
		return
	for x in n: 
		if not x in p: 
			p.append(x)    
			permNext(n, p) 
			p.pop()        

temp=['a','b','c']
perm(temp)