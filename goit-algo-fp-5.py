import uuid  
import networkx as nx 
import matplotlib.pyplot as plt 
import heapq  

class Node:   
    def __init__(self, key, color="skyblue"):                   # Ініціалізуємо вузол з ключем, кольором та унікальним ідентифікатором
        self.left = None   
        self.right = None  
        self.val = key  
        self.color = color                                      # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())                             # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):             # Функція для додавання ребер до графа, що представляє дерево
    if node is not None:                                         
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:                                           # Якщо лівий нащадок існує, додаємо ребро між вузлом та його лівим нащадком                              
            graph.add_edge(node.id, node.left.id)                
            l = x - 1 / 2 ** layer                              
            pos[node.left.id] = (l, y - 1)                       
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)   
        if node.right:                                          # Якщо правий нащадок існує, додаємо ребро між вузлом та його правим нащадком
            graph.add_edge(node.id, node.right.id) 
            r = x + 1 / 2 ** layer  
            pos[node.right.id] = (r, y - 1)  
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)   
    return graph                                                # Повертаємо граф із доданими вузлами та ребрами

def draw_tree(tree_root, colors):                               # Функція для візуалізації дерева
    tree = nx.DiGraph()                                         # Створюємо спрямований граф
    pos = {tree_root.id: (0, 0)}                                # Початкова позиція кореневого вузла
    tree = add_edges(tree, tree_root, pos)                      # Додаємо всі ребра та вузли до графа

    node_colors = [colors.get(node, 'skyblue') for node in tree.nodes()]   
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}   

    plt.figure(figsize=(8, 5))   
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)  
    plt.show()                                                  # Відображаємо граф на екрані

def build_heap_tree(heap, index=0):                             # Функція для побудови дерева з купи
    if index >= len(heap):                                      # Якщо індекс перевищує розмір купи, повертаємо None
        return None   
    root = Node(heap[index])                                    # Створюємо вузол для поточного елемента
    
    left_index = 2 * index + 1                                  # Визначаємо індекси для лівого та правого нащадків у списку
    right_index = 2 * index + 2   
    
    root.left = build_heap_tree(heap, left_index)               # Рекурсивно створюємо ліве та праве піддерево
    root.right = build_heap_tree(heap, right_index)  
    return root   

def generate_red_color(step, total_steps):                      # Функція для генерації кольору з червоної гами
    base_color = [255, 204, 204]                                # Світло-червоний колір
    darken_factor = step / total_steps                          # Крок до темнішого кольору
    new_color = [int(c * (1 - 0.4 * darken_factor)) for c in base_color]  # Новий колір із урахуванням затемнення
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'     # Повертаємо колір у форматі HEX

def generate_blue_color(step, total_steps):                     # Аналогічна функція для генерації кольору з блакитної гами
    base_color = [204, 229, 255]   
    darken_factor = step / total_steps   
    new_color = [int(c * (1 - 0.4 * darken_factor)) for c in base_color]  
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}' 

def dfs_visualize(root, total_steps):                           # Функція для візуалізації обходу дерева в глибину (DFS)
    visited = set()   
    stack = [root]                                              # Стек для обходу дерева
    colors = {}                                                 # Словник для збереження кольорів вузлів
    step = 0   

    while stack:                                                # Виконуємо поки стек не порожній
        node = stack.pop()                                      # Виймаємо останній елемент із стека
        if node and node.id not in visited:                     # Якщо вузол існує і ще не відвіданий
            visited.add(node.id)                                # Додаємо вузол до множини відвіданих
            colors[node.id] = generate_red_color(step, total_steps)  # Призначаємо вузлу колір із червоної гами
            step += 1   
            if node.right:  
                stack.append(node.right)   
            if node.left:   
                stack.append(node.left)   

    return colors                                               # Повертаємо словник із кольорами вузлів

def bfs_visualize(root, total_steps):                           # Функція для візуалізації обходу дерева в ширину (BFS)
    visited, queue = set(), [root]   
    colors = {}                                                 # Словник для збереження кольорів вузлів
    step = 0   

    while queue:                                                # Аналогічно виконуємо поки черга не порожня
        node = queue.pop(0)   
        if node and node.id not in visited:  
            visited.add(node.id)  
            colors[node.id] = generate_blue_color(step, total_steps)  # Призначаємо вузлу колір із блакитної гами
            step += 1   
            if node.left:   
                queue.append(node.left)   
            if node.right:  
                queue.append(node.right)  

    return colors                                               # Повертаємо словник із кольорами вузлів

def count_nodes(node):                                          # Функція для підрахунку кількості вузлів у дереві
    if node is None:   
        return 0  
    return 1 + count_nodes(node.left) + count_nodes(node.right) # Повертаємо кількість вузлів у дереві

if __name__ == '__main__':   
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]              # Наш список елементів для купи
    heapq.heapify(heap_list)                                    # Перетворюємо список на min-heap
    heap_tree_root = build_heap_tree(heap_list)                 # Створюємо дерево з купи

    total_steps = count_nodes(heap_tree_root)  

                                                                # DFS візуалізація з червоною гамою
    dfs_colors = dfs_visualize(heap_tree_root, total_steps)     # Отримуємо кольори для вузлів за допомогою обходу в глибину
    draw_tree(heap_tree_root, dfs_colors)                       # Візуалізуємо дерево з використанням кольорів із червоної гами

                                                                # BFS візуалізація з блакитною гамою
    bfs_colors = bfs_visualize(heap_tree_root, total_steps)     # Отримуємо кольори для вузлів за допомогою обходу в ширину
    draw_tree(heap_tree_root, bfs_colors)                       # Візуалізуємо дерево з використанням кольорів із блакитної гами
