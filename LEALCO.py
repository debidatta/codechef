t = int(raw_input())

def findp(n,k,m,r):
	p = [0] * n
	
	for j in xrange(n):
		c = []
		c = r[j:min(n,j+k)]
		c_m = max(c)
		
		
		if c.count(c_m) >= m:
			for z in range(k):
				p[min(j+z,n-1)] += 1
	return p

operated=[]
for i in xrange(t):
	n,k,m = [int(x) for x in raw_input().split()]
	r = [int(x) for x in raw_input().split()]

	operated = []
	while not m==1 and not len(operated)==n:
		p_now = findp(n,k,m,r)
		max_chk = max(p_now)
		if max_chk==0:
			break
		p_now_sum = sum(p_now)
		p_next = [0] * n
				
		for h in xrange(n):
			if h in operated:
				p_next[h] = p_now_sum
			else:
				r[h] += 1
				p_next[h] = sum(findp(n,k,m,r))
				r[h] -= 1
		p_next_min = min(p_next)
		elist = [i for i,val in enumerate(p_next) if val==p_next_min and val < p_now_sum]
		for q in xrange(len(elist)):
			if not max_chk == 0 :
				r[elist[q]] += 1;
				operated.append(elist[q])
				break
			else:
				continue

	if m == 1 or not max_chk == 0:
		print -1
	elif max(p_now) == 0:
		print len(operated)