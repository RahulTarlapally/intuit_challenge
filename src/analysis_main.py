from csv_reader import read_csv
from sales_analyzer import SalesAnalyzer
from config import CONFIG

def main():
    data = read_csv(CONFIG['csv_path'])
    analyzer = SalesAnalyzer(data)

    print(f'total sales : {analyzer.total_sales()}')
    print(f'sales by category : {analyzer.total_sales_by_category()}')
    print(f'avg transaction : {analyzer.avg_sales_per_transaction()}')
    print(f'top 5 sales: {analyzer.top_n_sales()}')

if __name__ == "__main__":
    main()

