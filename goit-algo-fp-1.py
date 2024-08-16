class Node:                                              # Ініціалізуємо вузол з переданими даними та посиланням на наступний вузол
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:                                        # Ініціалізуємо зв'язаний список з початковим вузлом
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):                 # Вставляємо новий вузол на початок списку
        new_node = Node(data)                            # Створюємо новий вузол
        new_node.next = self.head                        # Встановлюємо наступний вузол на поточну голову
        self.head = new_node                             # Оновлюємо голову на новий вузол

    def insert_at_end(self, data):                       # Вставляємо новий вузол у кінець списку
        new_node = Node(data)   
        if self.head is None:                            # Якщо список порожній, робимо новий вузол головою
            self.head = new_node
        else:                                            # Інакше проходимо до кінця списку і додаємо вузол
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node                          # Встановлюємо новий вузол як останній елемент

    def reverse(self):                                   # Реверсуємо зв'язаний список, змінюючи посилання між вузлами
        prev = None                                       
        current = self.head                              # Починаємо з голови списку
        while current:                                   # Проходимо через кожен вузол і змінюємо його посилання на попередній вузол
            next_node = current.next                     # Зберігаємо наступний вузол
            current.next = prev                          # Змінюємо посилання на попередній вузол
            prev = current                               # Рухаємо попередній вузол вперед
            current = next_node                          # Рухаємо поточний вузол вперед
        self.head = prev                                 # Встановлюємо нову голову списку

    def merge_sort(self, head):                          # Алгоритм сортування злиттям для зв'язаного списку                
        if head is None or head.next is None:            # Якщо список порожній або має один елемент, повертаємо його як відсортований
            return head

        middle = self.get_middle(head)                   # Знаходимо середній вузол списку
        next_to_middle = middle.next                     # Визначаємо наступний вузол після середнього
        middle.next = None                                

        left = self.merge_sort(head)                     # Рекурсивно сортуємо ліву частину
        right = self.merge_sort(next_to_middle)          # Аналогічно праву частину

        sorted_list = self.sorted_merge(left, right)     # З'єднуємо відсортовані половини
        return sorted_list

    def get_middle(self, head):                          # Знаходимо середній вузол списку для розділення
        if head is None:
            return head

        slow = head                                      # Pointer (вказівник), що рухається повільно (по одному кроку)
        fast = head                                      # Швидкий pointer рухається по два кроки

        while fast.next and fast.next.next:              # Рухаємо повільний pointer на один вузол, а швидкий на два
            slow = slow.next
            fast = fast.next.next

        return slow                                      # Повертаємо середній вузол

    def sorted_merge(self, a, b):                        # Об'єднуємо два відсортованих списки в один
        
        result = None

        if a is None:
            return b                                     # Якщо перший список порожній, повертаємо другий
        if b is None:
            return a                                     # Якщо другий список порожній, повертаємо перший

        if a.data <= b.data:
                                                         # Якщо дані у першому списку менші або рівні, додаємо його елемент до результату
            result = a
            result.next = self.sorted_merge(a.next, b)   # Рекурсивно об'єднуємо залишки списків
        else:                                            # Інакше додаємо елемент з другого списку до результату
            result = b
            result.next = self.sorted_merge(a, b.next)   # Рекурсивно об'єднуємо залишки списків

        return result                                    # Повертаємо результат об'єднання

    def merge_sorted_lists(self, list1, list2):          # Об'єднуємо два відсортованих списки
        sorted_list1 = self.merge_sort(list1.head)       # Сортуємо перший список
        sorted_list2 = self.merge_sort(list2.head)       # Сортуємо другий список
                                                         # Викликаємо функцію для злиття відсортованих списків
        merged_head = self.sorted_merge(sorted_list1, sorted_list2)
        
        merged_list = LinkedList()                       # Повертаємо новий зв'язаний список з головою merged_head
        merged_list.head = merged_head
        return merged_list

    def print_list(self):                                # Друкуємо всі елементи списку
        current = self.head                              # Починаємо з голови списку
        while current:                                   # Проходимо по списку і виводимо кожен елемент
            print(current.data, "-->", end="")
            current = current.next
        print('None')                                    # Вказуємо на кінець списку


if __name__ == '__main__':
    first_list = LinkedList()

                                                         # Додаємо елементи до першого списку
    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    print("Зв'язний список:")
    first_list.print_list()

    first_list.reverse()                                 # Реверсуємо список
    print("Зв'язний список після реверсування :")
    first_list.print_list()
                                                         # Сортуємо список
    first_list.head = first_list.merge_sort(first_list.head)
    print("Зв'язний список відсортовано:")
    first_list.print_list()

    second_list = LinkedList()                           # Додаємо елементи до другого списку
    second_list.insert_at_beginning(39)
    second_list.insert_at_beginning(40)
    second_list.insert_at_beginning(55)
    second_list.insert_at_beginning(49)

                                                         # Об'єднуємо два відсортованих списки
    merged_list = LinkedList().merge_sorted_lists(first_list, second_list)
    print("Зв'язний список відсортовано та замерджено:")
    merged_list.print_list()