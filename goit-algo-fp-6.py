items = {                                               # Заповнюємо словник зі стравами з їхньою вартістю та калорійністю.
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):                   # Реалізуємо логіку жадібного алгоритму
    total_calories = 0                                 # Сумарна кількість калорій, яку отримали з вибраних страв
    remaining_budget = budget                          # Бюджет, що залишився після вибору страв
    chosen_items = []                                  # Список обраних страв

                                                       # Сортуємо страви за спаданням співвідношення калорії/вартість
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    for item, details in sorted_items:
        if remaining_budget >= details['cost']:        # Якщо залишок бюджету дозволяє купити страву:
            chosen_items.append(item)                  # додаємо страву до списку вибраних
            total_calories += details['calories']      # Також додаємо калорії цієї страви до загальної кількості
            remaining_budget -= details['cost']        # Логічно, що зменшуємо залишок бюджету
                                                       # Повертаємо загальні калорії, залишок бюджету та обрані страви
    return total_calories, remaining_budget, chosen_items  


def dynamic_programming(items, budget):                # Реалізуємо логіку алгоритму динамічного програмування
    item_names = list(items.keys())                    # Отримуємо список назв страв
    n = len(item_names)                                # Кількість страв

                            # Створюємо DP-таблицю, де dp_table[i][temp_budget] — максимальні калорії для i страв з бюджетом temp_budget
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    
    for i in range(1, n + 1):                          # Заповнюємо DP-таблицю
        item_name = item_names[i - 1]                  # Назва поточної страви
        item_cost = items[item_name]['cost']           # Вартість поточної страви
        item_calories = items[item_name]['calories']   # Калорійність поточної страви

        for temp_budget in range(budget + 1):
            if item_cost <= temp_budget:
                                                       # Якщо бюджет дозволяє, обираємо максимальне значення між:
                                                       # - залишком калорій без цієї страви
                                                       # - калоріями з цією стравою
                dp_table[i][temp_budget] = max(dp_table[i - 1][temp_budget], dp_table[i - 1][temp_budget - item_cost] + item_calories)
            else:                                      # Якщо бюджет не дозволяє, повертаємося до попереднього результату без цієї страви
                dp_table[i][temp_budget] = dp_table[i - 1][temp_budget]

    chosen_items = []                                  # Список для обраних страв
    temp_budget = budget                               # Тимчасовий бюджет для поточних розрахунків
    for i in range(n, 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            item_name = item_names[i - 1]              # Назва обраної страви
            chosen_items.append(item_name)             # Додаємо страву до списку вибраних
            temp_budget -= items[item_name]['cost']    # Зменшуємо залишок бюджету
                           # Повертаємо максимальні калорії усіх обраних страв, залишок бюджету і відповідно обрані страви
    return dp_table[n][budget], temp_budget, chosen_items  


if __name__ == '__main__':
    budget = 5                                        # Встановлюємо бюджет для роботи алгоритмів

    min_cost = min(item['cost'] for item in items.values())
    if budget < min_cost:
        print("Можливо сьогодні хтось із друзів пригостить ;)")
    else:
        greedy_result = greedy_algorithm(items, budget)   
        dp_result = dynamic_programming(items, budget)   

        print(f"Greedy Algorithm при бюджеті {budget} обрав:")
        print(f"  Обрані страви: {', '.join(greedy_result[2])}")
        print(f"  Загальна кількість калорій: {greedy_result[0]}")
        print(f"  Залишок бюджету: {greedy_result[1]}\n")  
         
        print(f"Dynamic Programming Algorithm при бюджеті {budget} обрав:")
        print(f"  Обрані страви: {', '.join(dp_result[2])}")
        print(f"  Загальна кількість калорій: {dp_result[0]}")
        print(f"  Залишок бюджету: {dp_result[1]}") 
        print("Смачного !") 