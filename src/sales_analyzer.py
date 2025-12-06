'''
performs aggregation, grouping, and filtering operations on CSV data
'''

from functools import reduce

class SalesAnalyzer:
    def __init__(self, data):
        self.data = data 

    def total_sales(self):
        return reduce(lambda acc, row: acc+float(row['total_price']), self.data, 0)

    def total_sales_by_category(self):
        g = {}
        for row in self.data:
            cat = row['category']
            price = float(row['total_price'])
            g[cat] = g.get(cat, 0) + price 
        return g 

    def avg_sales_per_transaction(self):
        total = self.total_sales()
        count = len(self.data)
        return total / count if count else 0 

    def filter_by_min_price(self, min_price):
        return list(filter(lambda r: float(r['total_price']) >= min_price, self.data))

    def top_n_sales(self, n=5):
        return sorted(self.data, key=lambda r: float(r['total_price']), reverse=True)[:n]
