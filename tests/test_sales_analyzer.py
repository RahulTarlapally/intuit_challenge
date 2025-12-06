import sys
import os 

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT_DIR)
SRC_DIR = os.path.join(ROOT_DIR, 'src')
sys.path.insert(0, SRC_DIR)

from sales_analyzer import SalesAnalyzer


def sample_data():
    return [
        {'category': 'A', 'total_price':'10'},
        {'category': 'A', 'total_price':'20'},
        {'category': 'B', 'total_price': '5'}
    ]


def test_total_sales():
    ana = SalesAnalyzer(sample_data())
    assert ana.total_sales() == 35

def test_category_grouping():
    ana = SalesAnalyzer(sample_data())
    assert ana.total_sales_by_category() == {'A':30.0, "B":5.0}

def test_avg_sale():
    ana = SalesAnalyzer(sample_data())
    assert ana.avg_sales_per_transaction() == 35/3

def test_filter_min_price():
    ana = SalesAnalyzer(sample_data())
    res = ana.filter_by_min_price(15)
    assert len(res) == 1
    assert res[0]['total_price'] == '20'

if __name__ == "__main__":
    test_total_sales()
    test_category_grouping()
    test_avg_sale()
    test_filter_min_price()
    print('Yahoo! ALL Tests Passed')

