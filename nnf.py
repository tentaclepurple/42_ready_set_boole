class Node:
    def __init__(self, value, neg=False, left=None, right=None):
        self.value = value    
        self.neg = neg        
        self.left = left      
        self.right = right    
        
    def copy(self):
        new_node = Node(self.value, self.neg)
        if self.left:
            new_node.left = self.left.copy()
        if self.right:
            new_node.right = self.right.copy()
        return new_node
        
    @classmethod
    def parse(cls, formula):
        stack = []
        for char in formula:
            if char.isalpha():
                stack.append(cls(char))
            elif char == '!':
                if not stack:
                    raise ValueError("Invalid negation")
                node = stack.pop()
                node.neg = not node.neg
                stack.append(node)
            elif char in {'&', '|', '>', '=', '^'}:
                if len(stack) < 2:
                    raise ValueError(f"Not enough operands for {char}")
                right = stack.pop()
                left = stack.pop()
                stack.append(cls(char, left=left, right=right))
        
        if len(stack) != 1:
            raise ValueError("Invalid formula structure")
        return stack[0]
    
    def to_string(self):
        if self.value in {'&', '|', '>', '=', '^'}:
            result = f"{self.left.to_string()}{self.right.to_string()}{self.value}"
        else:
            result = self.value
        
        if self.neg:
            result += "!"
        return result

def transform_nnf(node):
    # Manejar primero la negación si existe
    if node.neg:
        if node.value not in {'&', '|', '>', '=', '^'}:  # Es una variable
            return
            
        node.neg = False
        if node.value in {'&', '|'}:
            # Aplicar leyes de De Morgan
            node.left.neg = not node.left.neg
            node.right.neg = not node.right.neg
            node.value = '|' if node.value == '&' else '&'
    
    # Transformar operadores
    if node.value == '>':
        # A > B = !A | B
        node.value = '|'
        node.left.neg = not node.left.neg
    elif node.value == '=':
        # A = B = (A > B) & (B > A) = (!A | B) & (!B | A)
        left_part = Node('|', 
                        left=node.left.copy(),
                        right=node.right.copy())
        left_part.left.neg = not left_part.left.neg
        
        right_part = Node('|',
                         left=node.right.copy(),
                         right=node.left.copy())
        right_part.left.neg = not right_part.left.neg
        
        node.value = '&'
        node.left = left_part
        node.right = right_part
    elif node.value == '^':
        # A ^ B = (A & !B) | (!A & B)
        left_and = Node('&', 
                       left=node.left.copy(),
                       right=node.right.copy())
        left_and.right.neg = True
        
        right_and = Node('&',
                        left=node.left.copy(),
                        right=node.right.copy())
        right_and.left.neg = True
        
        node.value = '|'
        node.left = left_and
        node.right = right_and
    
    # Transformar recursivamente los hijos
    if node.left:
        transform_nnf(node.left)
    if node.right:
        transform_nnf(node.right)

def negation_normal_form(formula: str) -> str:
    try:
        root = Node.parse(formula)
        transform_nnf(root)
        return root.to_string()
    except ValueError as e:
        return str(e)
    

if __name__ == "__main__":
    print(negation_normal_form("ABC^^"))