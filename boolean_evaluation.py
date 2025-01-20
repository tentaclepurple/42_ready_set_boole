from anytree import Node, RenderTree


class BooleanAST:
    """
    Abstract Syntax Tree for boolean expressions using anytree library.
    """
    
    @staticmethod
    def build_tree(formula: str) -> Node:
        """
        Builds an AST from a RPN formula using anytree
        """
        if not formula:
            raise ValueError("Empty formula")
            
        stack = []
        
        for i, char in enumerate(formula):
            # Create a node with unique name
            current_node = Node(f"{char}_{i}", value=char)
            
            if char in {'&', '|', '^', '>', '=', '!'}:
                # Operators pop values from stack
                if char == '!':
                    # Unary operator
                    if not stack:
                        raise ValueError("Invalid formula: not enough operands")
                    operand = stack.pop()
                    operand.parent = current_node
                else:
                    # Binary operator
                    if len(stack) < 2:
                        raise ValueError("Invalid formula: not enough operands")
                    right = stack.pop()
                    left = stack.pop()
                    right.parent = current_node
                    left.parent = current_node
            
            stack.append(current_node)
        
        if len(stack) != 1:
            raise ValueError("Invalid formula: too many operands")
            
        return stack[0]
    
    @staticmethod
    def evaluate_node(node: Node) -> bool:
        """Evaluates a node in the AST"""
        if not node:
            raise ValueError("Empty node")
            
        # If node is a value
        if node.value in '01':
            return node.value == '1'
            
        # If node is an operator
        if node.value == '!':
            return not BooleanAST.evaluate_node(node.children[0])
        elif node.value == '&':
            return BooleanAST.evaluate_node(node.children[0]) and BooleanAST.evaluate_node(node.children[1])
        elif node.value == '|':
            return BooleanAST.evaluate_node(node.children[0]) or BooleanAST.evaluate_node(node.children[1])
        elif node.value == '^':
            return BooleanAST.evaluate_node(node.children[0]) != BooleanAST.evaluate_node(node.children[1])
        elif node.value == '>':
            return not BooleanAST.evaluate_node(node.children[0]) or BooleanAST.evaluate_node(node.children[1])
        elif node.value == '=':
            return BooleanAST.evaluate_node(node.children[0]) == BooleanAST.evaluate_node(node.children[1])
            
        raise ValueError(f"Invalid operator: {node.value}")
    
    @staticmethod
    def print_tree(root: Node):
        """Prints the tree using anytree's RenderTree"""
        for pre, _, node in RenderTree(root):
            print(f"{pre}{node.value}")
