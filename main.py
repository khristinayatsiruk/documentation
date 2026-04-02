import csv
import json
import os
from concrete_strategies import ConsoleStrategy, KafkaStrategy, RedisStrategy, FileStrategy

def get_strategy():
    # Читаємо JSON конфіг
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    strategy_type = config.get('strategy', 'console').lower()
    
    strategies = {
        "console": ConsoleStrategy(),
        "kafka": KafkaStrategy(),
        "redis": RedisStrategy(),
        "file": FileStrategy()
    }
    
    return strategies.get(strategy_type, ConsoleStrategy())

def process_data(file_path, strategy):
    if not os.path.exists(file_path):
        print(f"Помилка: Файл {file_path} не знайдено!")
        return

    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            strategy.send(row)

if __name__ == "__main__":
    current_strategy = get_strategy()
    process_data('data.csv', current_strategy)
    print("\nОбробка завершена успішно.")