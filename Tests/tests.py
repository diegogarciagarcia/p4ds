for i in range(0,10):
    if i % 2 == 0:
        print(i)
    elif i % 3 ==0:
        print(str(i)+" es divisible por 3")
    else:
        print(i+10)

def my_abs1(val):
    if val < 0:
        return 0-val
    return val

def my_abs(val):
	if val < 0:
		print(0-val) #parentheses for print required in Python 3
	else:
		print(val)

def swap(val1, val2):
	tmp = val1
	val1 = val2
	val2 = tmp

x = 6
y = 3
swap(x, y)
print(x,", ",y)
