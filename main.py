from etl import read_csv, process_data, calculate_sales

file_name = 'vendas.csv'
raw_data = read_csv(file_name)
structured_data = process_data(raw_data)
result = calculate_sales(structured_data)
for category, item in result.items():
    print(f'Category {category}: $ {item}')