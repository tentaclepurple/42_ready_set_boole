class Node:
    def __init__(self, value, neg=False, left=None, right=None):
        self.value = value    # Operator or variable
        self.neg = neg        # Is this node negated?
        self.left = left      # Left child
        self.right = right    # Right child
        
    def copy(self):
        """Creates a deep copy of the node"""
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
            if char.isalpha():  # Variable
                stack.append(cls(char))
            elif char == '!':  # Negation
                if not stack:
                    raise ValueError("Invalid negation")
                node = stack.pop()
                node.neg = not node.neg
                stack.append(node)
            elif char in {'&', '|', '>', '=', '^'}:  # Binary operators
                if len(stack) < 2:
                    raise ValueError(f"Not enough operands for {char}")
                right = stack.pop()
                left = stack.pop()
                stack.append(cls(char, left=left, right=right))
            else:
                raise ValueError(f"Invalid character: {char}")
        
        if len(stack) != 1:
            raise ValueError("Invalid formula structure")
        return stack[0]
    
    def to_string(self):
        """Converts the AST back to a string"""
        if self.value in {'&', '|', '>', '=', '^'}:
            result = f"{self.left.to_string()}{self.right.to_string()}{self.value}"
        else:
            result = self.value
        
        if self.neg:
            result += "!"
        return result

def transform_nnf(node):
    """Transforms a node and its children to NNF form in-place"""
    if node.value == '>':
        # A > B becomes !A | B
        node.value = '|'
        node.left.neg = not node.left.neg
    
    elif node.value == '=':
        # A = B becomes (!A | B) & (!B | A)
        # Create first part: (!A | B)
        left_impl = Node('|', 
                        left=Node(node.left.value, neg=True),
                        right=node.right.copy())
        
        # Create second part: (!B | A)
        right_impl = Node('|',
                         left=Node(node.right.value, neg=True),
                         right=node.left.copy())
        
        # Join with AND
        node.value = '&'
        node.left = left_impl
        node.right = right_impl
    
    elif node.value == '^':
        # A ^ B becomes (A | B) & (!A | !B)
        left_or = Node('|', left=node.left.copy(), right=node.right.copy())
        right_or = Node('|', 
                       left=Node(node.left.value, neg=True),
                       right=Node(node.right.value, neg=True))
        node.value = '&'
        node.left = left_or
        node.right = right_or

    # Apply De Morgan's laws if node is negated
    if node.neg and node.value in {'&', '|'}:
        node.neg = False
        node.left.neg = not node.left.neg
        node.right.neg = not node.right.neg
        node.value = '|' if node.value == '&' else '&'

    # Transform children recursively
    if node.left:
        transform_nnf(node.left)
    if node.right:
        transform_nnf(node.right)

def negation_normal_form(formula: str) -> str:
    """Converts a formula in RPN to its Negation Normal Form"""
    try:
        root = Node.parse(formula)
        transform_nnf(root)
        return root.to_string()
    except ValueError as e:
        return str(e)