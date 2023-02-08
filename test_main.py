from main import *

def test_simple_work():
	
  assert simple_work_calc(10, 2, 2) == 56.0
  assert simple_work_calc(20, 3, 2) == 506.75
  assert simple_work_calc(30, 4, 2) == 1954.0
  assert simple_work_calc(12, 5, 3) == 52.0
  assert simple_work_calc(40, 1, 2) == 79.95
  assert simple_work_calc(100, 2, 10) == 124.0







def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 31
  assert work_calc(20, 1, 2, lambda n: n*n) == 533.8125
  assert work_calc(30, 3, 2, lambda n: n) == 638.625
  assert work_calc(12, 5, 3, lambda n: 3) == 218
  assert work_calc(40, 1, 2, lambda n: n) == 79.75
  assert work_calc(100, 2, 10, lambda n: n*n) == 10204.0
