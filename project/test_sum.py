"""
    M05 Programming Assignment - Testing
	SDEV220
	Paul R Thompson
    test_sum.py
"""

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print ("Everything passed")
