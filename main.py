from dal import SqlAlchemyRepository
from bll import ImportService
from presentation import ConsoleUI

if __name__ == "__main__":
    # 1. Створюємо "залізо" (DAL)
    repository = SqlAlchemyRepository()
    
    # 2. Впроваджуємо DAL в логіку (BLL)
    service = ImportService(repository)
    
    # 3. Впроваджуємо логіку в інтерфейс (PL)
    ui = ConsoleUI(service)
    
    # Запуск
    ui.start()