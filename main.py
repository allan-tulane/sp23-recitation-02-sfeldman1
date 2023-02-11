"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
  if n <= 1:
    return 1
  else:
    return a*simple_work_calc(n/b, a, b ) + n
    

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
 

def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 31
  assert work_calc(20, 1, 2, lambda n: n*n) == 533.8125
  assert work_calc(30, 3, 2, lambda n: n) == 638.625
  assert work_calc(12, 5, 3, lambda n: 3) == 218
  assert work_calc(40, 1, 2, lambda n: n) == 79.75
  assert work_calc(100, 2, 10, lambda n: n*n) == 10204.0

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  result = []
  for n in sizes:
		# compute W(n) using current a, b, f
    result.append((n, work_fn1(n), work_fn2(n)))
  "result = n.array(result)"
  return result

def test_compare_work():
  def work_fn1(n):
    return work_calc(n, 4, 2, lambda n:math.pow(n, 1.0))
  def work_fn2(n):
    return work_calc(n, 4,2, lambda n:math.pow(n, 10.0))
  res = compare_work(work_fn1, work_fn2)
  print(res)

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))
	


def span_calc(n, a, b, f):
  if n <= 1:
    return 1
  else:
    return span_calc(n/b, a, b, f) + f(n)
	

def compare_span(span_fn1, span_fn2,sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  result = []
  for n in sizes:
		# compute W(n) using current a, b, f
    result.append((n, span_fn1(n), span_fn2(n)))
  
  return result
  
def test_compare_span():
  def span_fn1(n):
    return span_calc(n, 4, 2, lambda n:math.pow(n, 1.0))
  def span_fn2(n):
    return span_calc(n, 4,2, lambda n:math.pow(n, 10.0))
  res = compare_span(span_fn1, span_fn2)
  print(res)


print(span_calc(100000000, 4 ,2, lambda n:1))
print(span_calc(100000000, 4, 2, lambda n:n))
print(span_calc(100000000, 4, 2, lambda n: math.log(n)))



print(work_calc(100000000, 4, 2, lambda n: 1))
print(work_calc(100000000, 4, 2, lambda n: n))
print(work_calc(100000000, 4, 2, lambda n: math.log(n)))