import unittest
from outdpik import outdpik as outdp
import pandas as pd
import matplotlib.pyplot as plt

class TestOutdpik(unittest.TestCase):
    
    def test_outliers(self):
        df = pd.DataFrame({'salary':[1,2,3,4,5,1000,-300,4,-1], 'age':[20,22,25,88,1,33,44,55,66], 'weight':[50,60,70,80,90,100,110,120,130]})
        out = outdp()
        
        self.assertEqual(out.outliers(df), {'salary': [5, 6], 'age': [], 'weight': []})

    def test_plot_outliers(self):
        df = pd.DataFrame({'salary':[1,2,3,4,5,1000,-300,4,-1], 'age':[20,22,25,88,1,33,44,55,66], 'weight':[50,60,70,80,90,100,110,120,130]})
        out = outdp()
        plt.close()
        out.plot_outliers(df, 'salary')
        self.assertEqual(plt.gcf().number, 1)

if __name__ == '__main__':
    unittest.main()