import csv
import random
import sys

def generate(filename="data.csv", count=1000):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'price', 'category'])
        for i in range(count):
            writer.writerow([f"Product_{i}", round(random.uniform(10, 500), 2), "General"])
    print(f"Файл {filename} на {count} рядків створено.")

if __name__ == "__main__":
    rows = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    generate(count=rows)