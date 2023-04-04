# M05 Programming Assignment - Testing  
SDEV220  
Paul R. Thompson  
_______________________________________________  
  
Below is the terminal output from VSCode for all unittest test*.py files  
_______________________________________________  
PS C:\Users\ray62\Documents\SDEV220\Module5\M05_PgmAssign_Testing\project> python -m unittest discover      
F..F  
======================================================================  
FAIL: test_list_fraction (test.TestSum.test_list_fraction)  
Test that it can sum a list of fractions  
----------------------------------------------------------------------  
Traceback (most recent call last):  
  File "C:\Users\ray62\Documents\SDEV220\Module5\M05_PgmAssign_Testing\project\test.py", line 28, in test_list_fraction  
    self.assertEqual(result, 1)  
AssertionError: Fraction(9, 10) != 1  
  
======================================================================  
FAIL: test_sum_tuple (test_sum_unittest.TestSum.test_sum_tuple)  
----------------------------------------------------------------------  
Traceback (most recent call last):  
  File "C:\Users\ray62\Documents\SDEV220\Module5\M05_PgmAssign_Testing\project\test_sum_unittest.py", line 15, in test_sum_tuple  
    self.assertEqual (sum([1, 2, 2]), 6, "Should be 6")  
AssertionError: 5 != 6 : Should be 6  
  
----------------------------------------------------------------------  
Ran 4 tests in 0.001s  
  
FAILED (failures=2)  
PS C:\Users\ray62\Documents\SDEV220\Module5\M05_PgmAssign_Testing\project>   
  