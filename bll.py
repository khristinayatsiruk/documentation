from models import ProductEntity

class ImportService:
    def __init__(self, repository): # Тут repository має тип IRepository
        self.repository = repository

    def import_from_file(self, file_path):
        # 1. Читаємо через DAL
        data = self.repository.get_data_from_csv(file_path)
        
        # 2. Перетворюємо в об'єкти (моделі)
        entities = [ProductEntity(**item) for item in data]
        
        # 3. Зберігаємо через DAL
        self.repository.save_products(entities)
        print(f"BLL: Оброблено та збережено {len(entities)} записів.")