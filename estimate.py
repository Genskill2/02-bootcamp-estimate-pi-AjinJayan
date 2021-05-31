import math
import unittest
import random

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
    
def wallis(n_iter):
    product_series=1
    for i in range(1,n_iter+1):
        product_series *= 4*i*i/(4*i*i-1)  
    return 2*product_series    


def monte_carlo(n):
    dart_inside=0
    total_dart=n
    for i in range(0,n):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        distance=(x**2+y**2)**0.5
        if distance <= 1:
          dart_inside+=1
    return 4*dart_inside/total_dart

    
if __name__ == "__main__":
    unittest.main()
