import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]
csv_file_path = 'packing_list.csv'
try:
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            print(row)
except FileNotFoundError:
  print('Packing list file not found. Creating a new one.')
  with open('packing_list.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(data)