def binary_search(ls, n):
	i = 0
	items = ls.copy()
	while (True):
		print(items)
		if len(items) < 3:
			if n not in items:
				return None
			if items[0] == n:
				return i
			return i+1
		s = len(items)//2
		if items[0] <= n < items[s]:
			items = items[0:s]
		else:
			items = items[s::]
			i += s

a = [
	([1,2,3,4,5], 3),
	([1,2,3,4,5,6,7,8,9], 2),
	([2,4,6,8,10,12,14,16,18,20], 13),
	([0,2,4,6,8,10,12,14,16,18,20], 16),
	([-10,1,34,76,91,102,129,160,198,233,245,271,293,309,316,376,394,407,409,414,452,466,479], 407),
	([-10,1,34,76,91,102,129,160,198,233,245,271,293,309,316,376,394,407,409,414,452,466,479], 408),
	([-10,1,34,76,91,102,129,160,198,233,245,271,293,309,316,376,394,407,409,414,452,466,479], 245),
	([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8], 5)
	]
for i in a:
	print("\nindex of " + str(i[1]) + " is: " + str(binary_search(i[0], i[1])) + "\n\n----------------------\n")
input()