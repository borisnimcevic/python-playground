#! pyton3

import time

def calcProd():
	product =1
	for i in range(1,10000):
		product = product * i
	return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculat.' % (endTime - startTime))
