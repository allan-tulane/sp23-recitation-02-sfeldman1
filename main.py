"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
#import tabulate
import time
###

def simple_work_calc(n, a, b):
  if n <= 1:
    return 1
  else:
    return a*simple_work_calc(n/b, a, b ) + n
    
    
  
    """Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
  
  
  
	# TODO


def test_simple_work():
	
  assert simple_work_calc(10, 2, 2) == 56.0
  assert simple_work_calc(20, 3, 2) == 506.75
  assert simple_work_calc(30, 4, 2) == 1954.0
  assert simple_work_calc(12, 5, 4) == 52.0
  assert simple_work_calc(40, 1, 2) == 79.75
  assert simple_work_calc(100, 2, 10) == 124.0

def work_calc(n, a, b, f):
  if n <= 1:
    return 1
  else:
    return a*work_calc(n/b, a, b, f) + f(n)

  
"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO


def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	pass

def test_work():
  
  assert work_calc(10, 2, 2, lambda n: 1) == 31
  assert work_calc(20, 1, 2, lambda n: n*n) == 533.8125
  assert work_calc(30, 3, 2, lambda n: n) == 638.625
  assert work_calc(12, 5, 3, lambda n: 3) == 218
  assert work_calc(40, 1, 2, lambda n: n) == 79.75
  assert work_calc(100, 2, 10, lambda n: n*n) == 10204.0

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in input_sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2

    res = compare_work(work_fn1, work_fn2)
    print(res)

def test_compare_span():
	"TODO"
