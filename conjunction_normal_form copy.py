class Node:
    """
    Node class representing a boolean formula.
    Can be either a variable (A, B, C...) or an operator (&, |, >, =, ^).
    """
    def __init__(self, value, neg=False, left=None, right=None):
        self.value = value    # Variable or operator
        self.neg = neg       # Whether this node is negated
        self.left = left     # Left child for operators
        self.right = right   # Right child for operators

    def copy(self):
        """Creates a deep copy of current node and its children"""
        new_node = Node(self.value, self.neg)
        if self.left:
            new_node.left = self.left.copy()
        if self.right:
            new_node.right = self.right.copy()
        return new_node

class CNFConverter:
    """
    Converts boolean formulas to Conjunctive Normal Form (CNF).
    CNF requirements:
    1. Negations only appear on variables
    2. Only uses AND(&), OR(|), and NOT(!)
    3. AND operators appear at the end
    """
    @staticmethod
    def parse_formula(formula: str) -> Node:
        """
        Converts a string formula in RPN to a syntax tree.
        Example: "AB&" becomes a tree with & at root and A,B as children
        """
        stack = []
        
        for char in formula:
            if char.isalpha():  # Variables (A-Z)
                stack.append(Node(char))
            elif char == '!':  # NOT operator
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
                stack.append(Node(char, left=left, right=right))
            else:
                raise ValueError(f"Invalid character: {char}")
        
        if len(stack) != 1:
            raise ValueError("Invalid formula structure")
        return stack[0]

    def to_string(self, node: Node) -> str:
        """
        Converts a syntax tree back to RPN string format
        """
        if not node:
            return ""
            
        if node.value in {'&', '|', '>', '=', '^'}:
            result = f"{self.to_string(node.left)}{self.to_string(node.right)}{node.value}"
        else:
            result = node.value
            
        if node.neg:
            result += "!"
            
        return result

    def convert_to_nnf(self, node: Node) -> Node:
        """
        First step: Convert to Negation Normal Form.
        - Eliminates >, =, ^ operators
        - Pushes negations to variables using De Morgan's laws
        """
        if not node:
            return None

        # First handle implications and equivalences
        if node.value == '>':  # A > B becomes !A | B
            node.value = '|'
            node.left.neg = not node.left.neg
        elif node.value == '=':  # A = B becomes (!A | B) & (!B | A)
            left_part = Node('|', left=Node(node.left.value, neg=True),
                                right=node.right.copy())
            right_part = Node('|', left=Node(node.right.value, neg=True),
                                 right=node.left.copy())
            node.value = '&'
            node.left = left_part
            node.right = right_part
        elif node.value == '^':  # A ^ B becomes (A | B) & (!A | !B)
            left_part = Node('|', left=node.left.copy(),
                                right=node.right.copy())
            right_part = Node('|', left=Node(node.left.value, neg=True),
                                 right=Node(node.right.value, neg=True))
            node.value = '&'
            node.left = left_part
            node.right = right_part

        # Then apply De Morgan's laws to push negations down
        if node.neg and node.value in {'&', '|'}:
            node.neg = False
            node.left.neg = not node.left.neg
            node.right.neg = not node.right.neg
            node.value = '|' if node.value == '&' else '&'

        # Process children recursively
        self.convert_to_nnf(node.left)
        self.convert_to_nnf(node.right)
        return node

    def distribute_or(self, node: Node) -> bool:
        """
        Applies the distributive law: A | (B & C) = (A | B) & (A | C)
        Returns True if any changes were made
        """
        if not node:
            return False

        # First distribute in children
        changed = False
        if self.distribute_or(node.left):
            changed = True
        if self.distribute_or(node.right):
            changed = True

        # Then try to distribute at this node
        if node.value == '|':
            if node.right and node.right.value == '&':
                # A | (B & C) = (A | B) & (A | C)
                a = node.left.copy()
                b = node.right.left
                c = node.right.right
                node.value = '&'
                node.left = Node('|', left=node.left, right=b)
                node.right = Node('|', left=a, right=c)
                return True
            elif node.left and node.left.value == '&':
                # (A & B) | C = (A | C) & (B | C)
                a = node.left.left
                b = node.left.right
                c = node.right.copy()
                node.value = '&'
                node.left = Node('|', left=a, right=node.right)
                node.right = Node('|', left=b, right=c)
                return True

        return changed

    def to_cnf(self, formula: str) -> str:
        """
        Main method: converts a formula to CNF.
        1. Parse formula to syntax tree
        2. Convert to NNF
        3. Apply distributive laws
        4. Convert back to string
        """
        try:
            # Parse the input formula
            root = self.parse_formula(formula)
            
            # Convert to NNF
            root = self.convert_to_nnf(root)
            
            # Distribute OR over AND until no changes
            while self.distribute_or(root):
                pass
            
            # Convert back to string
            return self.to_string(root)
            
        except ValueError as e:
            return str(e)

def conjunctive_normal_form(formula: str) -> str:
    """
    Wrapper function that creates converter and processes formula
    """
    converter = CNFConverter()
    return converter.to_cnf(formula)