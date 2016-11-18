def tri2(x):	# Triangle number formula, iterative,
	x= x*(x+1)/2	# As seen on the book Things to Make and do in the fourth dimension
	return x		# by Matt Parker

def primefactors(x): 	# This is a code for factor checking
	factorlist=[]		# On small numbers such as this it's
	loop=2				# Just about enough
	while loop<=x:
		if x%loop==0: x/=loop
			factorlist.append(loop)
		else:
			loop+=1
	return factorlist

def factors(s):			# The above code doesn't print the
	xx=primefactors(s)	# non prime factors, so this one
	facindex=[]			# adds them back in and returns the
	for x in xx:		# number of factors the number has
		z=xx.count(x)
		if [x,z] not in facindex:
            facindex.append([x,z])
    numfac=1
	for [p,q] in facindex:
		numfac*=(q+1)
	return numfac

for i in range(1, 15000): 				# End result is 76576500,
	if (factors(int(tri2(i)))>=500):	# Quite a satisfying number.
		print(int(tri2(i)))				# as we are checking the first
										# 15000 it also prints 103672800
										# Also satisfying.
