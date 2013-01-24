t = int(raw_input())

for i in xrange(t):
	n = int(raw_input())
	sal_in = raw_input()
	sal = [int(x) for x in sal_in.split()]
	print sum(sal)- n* min(sal)