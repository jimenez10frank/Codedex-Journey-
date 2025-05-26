import csv

csv_file_path = 'Bestseller - Sheet1.csv'

best_selling_book = None
max_sales = 0

# Open the input CSV file with proper encoding and read data
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        try:
            current_sales = int(row[4])  # Convert sales to integer
        except ValueError:
            continue  # Skip rows where sales value is not a valid integer

        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row

# Write the bestselling book info to a new CSV file
if best_selling_book:
    output_file_path = 'bestseller_info.csv'
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.writer(output_file)

        # Write header
        csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])

        # Write bestselling book details
        csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])

    print('Bestselling info written to', output_file_path)
else:
    print('No valid book data found.')
