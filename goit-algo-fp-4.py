import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color                                                          # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())                                                 # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)                   # Використовуємо id та зберігаємо значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}          # Створюємо словник міток для відображення значень вузлів на графі

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None
    root = Node(heap[index])                                                        # Створюємо вузол для поточного елемента
    
    left_index = 2 * index + 1                                                      # Визначаємо індекси для лівого та правого нащадків у списку
    right_index = 2 * index + 2
    
    root.left = build_heap_tree(heap, left_index)                                   # Рекурсивно створюємо ліве та праве піддерево
    root.right = build_heap_tree(heap, right_index)
    return root


if __name__ == '__main__':
    heap_list = [1, 3, 5, 7, 9, 11, 13, 15, 4]                                      # Перетворюємо список на бінарну купу
    heapq.heapify(heap_list)
    print(heap_list)
    
    heap_tree_root = build_heap_tree(heap_list)                                     # Побудова дерева з купи

    draw_tree(heap_tree_root)                                                       # Візуалізація дерева бінарної купи
