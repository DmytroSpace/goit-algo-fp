import random
import matplotlib.pyplot as plt
 
def simulate_dice_rolls(num_rolls):                              # Словник для підрахунку кількості випадків для кожної суми
    sum_counts = {sum_: 0 for sum_ in range(2, 13)}
    
    for _ in range(num_rolls):                                   # Кидаємо два кубики і отримуємо випадкові числа від 1 до 6
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        
        roll_sum = die1 + die2                                   # Обчислюємо суму чисел на кубиках
        
        sum_counts[roll_sum] += 1                                # Рахуємо кількість випадків для цієї суми
    
    probabilities = {sum_: count / num_rolls for sum_, count in sum_counts.items()}
    
    return probabilities

def plot_probabilities(probabilities):                           # Отримуємо списки сум і ймовірностей для графіка
    
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    
    plt.bar(sums, probs, tick_label=sums)                       # Створюємо графік стовпчиків
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')
    
    
    for i, prob in enumerate(probs):                            # Додаємо відсотки випадання на графік
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()

if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        probabilities = simulate_dice_rolls(accuracy)           # Симуляція кидків і обчислення ймовірностей

        print(f"Результати для {accuracy} кидків:")
        for sum_, prob in probabilities.items():
            print(f"Сума {sum_}: ймовірність {prob*100:.2f}%")  # Виводимо ймовірності у відсотках
        
        plot_probabilities(probabilities)                       # Будуємо графік ймовірностей
