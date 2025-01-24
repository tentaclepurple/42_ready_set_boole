from enum import Enum
from typing import Optional, List
from dataclasses import dataclass

class NodeValue:
    class Type(Enum):
        VALUE = "VALUE"
        VARIABLE = "VARIABLE" 
        OPERATOR = "OPERATOR"

    def __init__(self, type: Type, value):
        self.type = type
        self.value = value

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

class TreeNode:
    def __init__(self, value: Optional[NodeValue] = None):
        self.value = value
        self.left = None  
        self.right = None

    @classmethod
    def new_from(cls, value: NodeValue):
        return cls(value)

    @classmethod
    def new_with_children(cls, value: NodeValue, left: 'TreeNode', right: 'TreeNode'):
        node = cls(value)
        node.left = left
        node.right = right
        return node

def create_tree(expression: str) -> TreeNode:
    stack = []
    for c in expression:
        if c == ' ':
            continue
            
        if c in '01':
            node = TreeNode(NodeValue(NodeValue.Type.VALUE, c == '1'))
        elif c.isalpha():
            node = TreeNode(NodeValue(NodeValue.Type.VARIABLE, c))
        elif c == '!':
            left = stack.pop()
            node = TreeNode(NodeValue(NodeValue.Type.OPERATOR, c))
            node.left = left
        elif c in '&|^>=':
            right = stack.pop()
            left = stack.pop()
            node = TreeNode(NodeValue(NodeValue.Type.OPERATOR, c))
            node.left = left
            node.right = right
        else:
            raise ValueError(f"Invalid character: {c}")
            
        stack.append(node)

    if len(stack) > 1:
        raise ValueError("Too many operands")
    elif len(stack) == 0:
        raise ValueError("Empty formula")
        
    return stack.pop()

def eval_tree(node: TreeNode) -> bool:
    if not node.value:
        raise ValueError("Node has no value")
        
    if node.value.type == NodeValue.Type.VALUE:
        return node.value.value
    elif node.value.type == NodeValue.Type.OPERATOR:
        if node.value.value == '!':
            return not eval_tree(node.left)
            
        left = eval_tree(node.left)
        right = eval_tree(node.right)
        
        if node.value.value == '&':
            return left and right
        elif node.value.value == '|':
            return left or right
        elif node.value.value == '^':
            return left != right
        elif node.value.value == '>':
            return (not left) or right
        elif node.value.value == '=':
            return left == right
            
    raise ValueError(f"Invalid node type: {node.value.type}")

def tree_to_rpn(node: TreeNode) -> str:
    if not node.value:
        raise ValueError("Node has no value")
        
    if node.value.type == NodeValue.Type.VALUE:
        return str(int(node.value.value))
    elif node.value.type == NodeValue.Type.VARIABLE:
        return node.value.value
    elif node.value.type == NodeValue.Type.OPERATOR:
        if node.value.value == '!':
            return f"{tree_to_rpn(node.left)}!"
        return f"{tree_to_rpn(node.left)}{tree_to_rpn(node.right)}{node.value.value}"

def apply_cnf(node: TreeNode) -> TreeNode:
    if not node.value:
        raise ValueError("Node has no value")
        
    if node.value.type != NodeValue.Type.OPERATOR:
        return node
        
    if node.value.value == '|':
        left = apply_cnf(node.left)
        right = apply_cnf(node.right)
        
        if left.value.type == NodeValue.Type.OPERATOR and left.value.value == '&':
            new_left = TreeNode.new_with_children(
                NodeValue(NodeValue.Type.OPERATOR, '|'),
                left.left,
                right
            )
            new_right = TreeNode.new_with_children(
                NodeValue(NodeValue.Type.OPERATOR, '|'),
                left.right,
                right
            )
            return TreeNode.new_with_children(
                NodeValue(NodeValue.Type.OPERATOR, '&'),
                apply_cnf(new_left),
                apply_cnf(new_right)
            )
        elif right.value.type == NodeValue.Type.OPERATOR and right.value.value == '&':
            new_left = TreeNode.new_with_children(
                NodeValue(NodeValue.Type.OPERATOR, '|'),
                left,
                right.left
            )
            new_right = TreeNode.new_with_children(
                NodeValue(NodeValue.Type.OPERATOR, '|'),
                left,
                right.right
            )
            return TreeNode.new_with_children(
                NodeValue(NodeValue.Type.OPERATOR, '&'),
                apply_cnf(new_left),
                apply_cnf(new_right)
            )
            
        return node
        
    new_node = TreeNode(node.value)
    if node.left:
        new_node.left = apply_cnf(node.left)
    if node.right:
        new_node.right = apply_cnf(node.right)
    return new_node

def move_conjunctions_to_end(formula: str) -> str:
    result = ""
    conjunctions = ""
    
    for c in formula:
        if c == '&':
            conjunctions += c
        else:
            result += c
            
    return result + conjunctions

def conjunctive_normal_form(formula: str) -> str:
    tree = create_tree(formula)
    cnf = apply_cnf(tree) 
    rpn = tree_to_rpn(cnf)
    return move_conjunctions_to_end(rpn)

def generate_truth_table(formula: str) -> List[bool]:
    # Implementation needed for tests
    pass

def check_conjunctions(formula: str) -> bool:
    # Implementation needed for tests - checks if formula is in CNF
    pass

# Tests
import unittest


class TestCNF(unittest.TestCase):
    def verify_cnf(self, input_formula, expected):
        result = conjunctive_normal_form(input_formula)
        print(f"\nInput:    {input_formula}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        print(f"Match:    {result == expected}")
        self.assertEqual(result, expected)
        
    def test_empty_string(self):
        self.verify_cnf("", "")
        
    def test_negated_and(self):
        self.verify_cnf("AB&!", "A!B!|")
        
    def test_negated_or(self):
        self.verify_cnf("AB|!", "A!B!&")
        
    def test_deep_and(self):
        self.verify_cnf("AB|C&D&", "AB|CD&&")
        
    def test_many_ors(self):
        self.verify_cnf("AB|C|D|", "AB|C|D|")
        
    def test_many_ands(self):
        self.verify_cnf("AB&C&D&", "ABCD&&&")
        
    def test_complicated(self):
        self.verify_cnf("AB&!C!|", "A!B!|C!|")
        
    def test_last_subject(self):
        self.verify_cnf("AB|!C!&", "A!B!C!&&")

if __name__ == "__main__":
    unittest.main(verbosity=2)