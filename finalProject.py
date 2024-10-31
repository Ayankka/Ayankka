
# Инициализируем словарь для хранения расходов
expenses = {
    'Продукты': 500,
    'Шоппинг': 1200,
    'Для дома': 800,
}


# Функция для добавления расходов
def add_expense():
    category = input("Введите категорию (Продукты, Шоппинг, Для дома): ")
    amount = float(input("650, 1000, 2300"))

    if category in expenses:
        expenses[category] += amount
        print(f'Добавлены расходы: {amount} в категорию {category}')
    else:
        print(f'Категория {category} не найдена.')


# Функция для показа текущих расходов
def show_expenses():
    print("Текущие расходы:")
    for category, amount in expenses.items():
        print(f'{category}: {amount} руб.')


# Основной цикл программы
while True:
    action = input(
        "Введите 'добавить' для добавления расходов, 'показать' для просмотра всех расходов или 'выйти' для выхода: ").lower()

    if action == 'добавить':
        add_expense()
    elif action == 'показать':
        show_expenses()
    elif action == 'выйти':
        print("Выход из программы.")
        break
    else:
        print("Неверная команда. Попробуйте снова.")


def add_expense(amount):
    """Добавить сумму расхода на день."""
    expenses["records"].append(amount)
    print(f"Добавлен расход: {amount}")


def calculate_total_expenses():
    """Рассчитать и вывести общие расходы."""
    total = sum(expenses["records"])
    print(f"Общие расходы: {total}")
    return total

def calculate_average_expense():
    """Рассчитать и вывести средний расход за день."""
    if len(expenses["records"]) > 0:
        average = sum(expenses["records"]) / len(expenses["records"])
        print(f"Средний расход за день: {average}")
        return average
    else:
        print("Данных для расчета среднего расхода нет.")
        return 0


# Список для хранения истории транзакций
transaction_history = []


# Функция для добавления расходов и записи их в историю транзакций
def add_expense():
    category = input("Введите категорию (Продукты, Шоппинг, Для дома): ")
    amount = float(input("Введите сумму расхода: "))

    if category in expenses:
        expenses[category] += amount
        # Добавляем запись в историю: кортеж с категорией и суммой
        transaction_history.append((category, amount))
        print(f'Добавлены расходы: {amount} в категорию {category}')
    else:
        print(f'Категория {category} не найдена.')


# Функция для вывода истории транзакций
def show_history():
    print("История транзакций:")
    if transaction_history:
        for transaction in transaction_history:
            category, amount = transaction
            print(f'Категория: {category}, Сумма: {amount} руб.')
    else:
        print("Транзакций пока нет.")


# Добавляем расходы
add_expense(650)
add_expense(800)
add_expense(1000)


# график расходов
# show_expenses()

# Рассчитывает  общие расходы
calculate_total_expenses()

# Рассчитывает средний расход за день
calculate_average_expense()
