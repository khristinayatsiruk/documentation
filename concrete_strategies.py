from strategy import OutputStrategy

class ConsoleStrategy(OutputStrategy):
    def send(self, row: dict):
        print(f"DEBUG [Console]: Processing Summons {row.get('Summons Number')}")

class KafkaStrategy(OutputStrategy):
    def send(self, row: dict):
        print(f"SEND [Kafka]: Topic 'parking_data' <- Row {row.get('Summons Number')}")

class RedisStrategy(OutputStrategy):
    def send(self, row: dict):
        print(f"STORE [Redis]: Key 'violation:{row.get('Summons Number')}'")

class FileStrategy(OutputStrategy):
    def send(self, row: dict):
        with open("output_results.txt", "a") as f:
            f.write(f"Summons: {row.get('Summons Number')}\n")
        print(f"DONE [File]: Written to output_results.txt")