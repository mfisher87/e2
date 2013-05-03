#! /usr/bin/env python3.3

totalSum = 0
def fibonacci(nbr,prevNbr):
	"Recursive function generates numbers in a fibonacci sequence"
	global totalSum

	print(nbr,end="")

	# If nbr divisible by 2, add nbr to totalSum
	if nbr%2 == 0:
		totalSum += nbr
		print("\teven")
	else: print()

	# If next number < 4M, recurse with new parameter values
	if nbr+prevNbr < 4000000:
		fibonacci(nbr+prevNbr,nbr)
	else: return [nbr]
	
fibonacci(1,0)
print("=======================================")
print("Sum of even fibonacci numbers:",totalSum)
