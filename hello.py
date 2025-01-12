class TreeNode:
    def __init__(self, value):  
        self.value = value
        self.children = []

def build_tree():
    nodes = {}
    
    while True:
        try:
            n_n = int(input("Enter the number of nodes (positive integer): "))
            if n_n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print("Enter the node value and the child nodes, if no children then enter ' - ' : ")
    for _ in range(n_n):
        value = input(" ").strip()
        value = value.split()

        if value[0] not in nodes:
            nodes[value[0]] = TreeNode(value[0]) 
        if value[1] == '-':
            continue
       
        for c_v in value[1:]:
            if c_v not in nodes:
                nodes[c_v] = TreeNode(c_v)
            nodes[value[0]].children.append(nodes[c_v]) 
    
    return nodes[next(iter(nodes))], nodes

def bfs(root, search_value):
    traversal = []
    queue = [(root, [root.value])]  
    i = 0  
    
    while i < len(queue):
        node, path = queue[i]
        i += 1

        traversal.append(node.value)

        if node.value == search_value:
            return path, traversal
        
        for child in node.children:
            queue.append((child, path + [child.value]))
    
    return None, traversal  

def generate_arr(root, nodes, arr=None):
    if arr is None:
        arr = [root.value]
    
    queue = [root]
    while queue:
        current = queue.pop(0)
        if not current.children:
            arr.extend(['-', '-'])
        else:
            child_values = [child.value for child in current.children]
            arr.extend(child_values + ['-'] * (2 - len(child_values)))  # Ensure two placeholders
            queue.extend(current.children)
    
    return arr

def tree_printer(arr, num_lvl):
    current_level = 0
    index = 0  
    
    while current_level <= num_lvl:
        nodes_at_level = 2 ** current_level
        leading_trailing_spaces = 2 ** (num_lvl - current_level)
        line = ' ' * leading_trailing_spaces

        for _ in range(nodes_at_level):
            if index < len(arr):
                line += str(arr[index]) + ' ' * leading_trailing_spaces * 2
                index += 1
            else:
                line += '- ' * leading_trailing_spaces * 2
        
        print(line.strip())
        current_level += 1

def find_depth(root):
    if root is None:
        return -1

    if not root.children:
        return 0
    child_depths = [find_depth(child) for child in root.children]
    
    return 1 + max(child_depths)

def main():
    root, nodes = build_tree()
    if not root:
        return
    arr = generate_arr(root, nodes)
    
    search_value = input("Enter the value to search for: ")
    path, traversal = bfs(root, search_value)
    
    if path:
        print(f"Path to {search_value} = {' -> '.join(path)}")
    else:
        print(f"Value '{search_value}' not found in the tree.")
    
    print(f"Traversal Path = {' -> '.join(traversal)}")

    tree_depth = find_depth(root)
    print("\nTree Structure:")
    tree_printer(arr, tree_depth)

if __name__ == "__main__":
    main()
