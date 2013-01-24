[n,m] = [int(x) for x in raw_input().split()]

country_name = {}
for i in xrange(n):
	[name,country] = raw_input().split()
	country_name[name] = country

country_count = {}
name_count = {}
for key, value in country_name.items():
	country_count[value] = 0;
	name_count[key] = 0;

for i in xrange(m):
	name = raw_input()
	name_count[name] += 1
	country_count[country_name[name]] += 1

max_c=max(country_count,key=country_count.get)
max_n=max(name_count,key=name_count.get)
max_list_c = {key:value for key, value in country_count.items() if value == country_count[max_c]}
max_list_n = {key:value for key, value in name_count.items() if value == name_count[max_n]}

print min(max_list_c.iterkeys())
print min(max_list_n.iterkeys())