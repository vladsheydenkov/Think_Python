x = input()


def print_(q):
	print(x * q)


def do_twice(f, n, q):
	if n:
		f(q)
		f(q)
		do_twice(f, n-1, q-1)


do_twice(print_, 7, 9)
