# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
def power2n(n):
    pass
    # power2n(n-1)+power2n(n-1)

# 方法2b：用遞迴
def power2n(n):
    pass
    # 2*power2n(n-1)

# 方法 3：用遞迴+查表
pow = [None]*10000
pow[1]=1
pow[0]=0
def power2n_x(n):
    # pass
    if n<0: raise
    if not pow[n] is None : return pow[n]  
    pow[n]=power2n_x(n-1)+power2n_x(n-1)
    return pow[n]

    
print(power2n_x(25))