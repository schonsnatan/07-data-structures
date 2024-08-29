import csv 

def read_csv(file: str) -> list[dict]:
    with open(file, mode='r',encoding='utf-8') as file:
        dict_reader = csv.DictReader(file)
        return list(dict_reader)
    
def process_data(salesList: list[dict]) -> dict:
    categories = {}
    for row in salesList:
        category = row['Categoria']
        if category not in categories:
            categories[category] = []
        categories[category].append(row)
    return categories

def calculate_sales(dataProcessed: dict) -> dict:
    sales = {}
    for category, items in dataProcessed.items():
        total_vendas = 0
        for item in items:
            total_vendas += int(item['Quantidade']) * int(item['Venda'])
        sales[category] = total_vendas
    return sales