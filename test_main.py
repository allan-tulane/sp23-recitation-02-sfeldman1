from main import *

def test_simple_work():
	
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(12, 5, 3) == 57
  assert simple_work_calc(40, 1, 2) == 78
  assert simple_work_calc(100, 2, 10) == 124







def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(12, 5, 3, lambda n: 3) == 43
  assert work_calc(40, 1, 2, lambda n: n) == 78
  assert work_calc(100, 2, 10, lambda n: n*n) == 10204
