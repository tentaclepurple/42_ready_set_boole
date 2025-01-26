from dataclasses import dataclass
from typing import List, Optional, Set

class ASTNode:
    def get_postfix(self) -> str:
        pass

@dataclass
class OperandNode(ASTNode):
    variable: str
    
    def get_postfix(self) -> str:
        return self.variable

@dataclass
class UnaryNode(ASTNode):
    operator: str  # '!'
    operand: ASTNode
    
    def get_postfix(self) -> str:
        return f"{self.operand.get_postfix()}{self.operator}"

@dataclass
class BinaryNode(ASTNode):
    operator: str  # '&', '|', '^', '>', '='
    left: ASTNode
    right: ASTNode
    
    def get_postfix(self) -> str:
        return f"{self.left.get_postfix()}{self.right.get_postfix()}{self.operator}"

def parse_expression(tokens: List[str]) -> Optional[ASTNode]:
    stack = []
    binary_ops = {'&', '|', '^', '>', '='}
    
    try:
        for token in tokens:
            if token in binary_ops:
                right = stack.pop()
                left = stack.pop()
                stack.append(BinaryNode(token, left, right))
            elif token == '!':
                operand = stack.pop()
                stack.append(UnaryNode(token, operand))
            else:
                stack.append(OperandNode(token))
                
        if len(stack) != 1:
            raise ValueError("Invalid expression")
            
        return stack[0]
    except:
        return None

def neg_nnf(node: ASTNode) -> ASTNode:
    if isinstance(node, OperandNode):
        return UnaryNode('!', node)
    elif isinstance(node, UnaryNode):
        return node.operand
    elif isinstance(node, BinaryNode):
        if node.operator == '|':
            return BinaryNode('&', neg_nnf(node.left), neg_nnf(node.right))
        elif node.operator == '&':
            return BinaryNode('|', neg_nnf(node.left), neg_nnf(node.right))
        elif node.operator == '>':
            return BinaryNode('|', node.left, neg_nnf(node.right))
        elif node.operator == '=':
            return BinaryNode('|', 
                BinaryNode('&', neg_nnf(node.left), node.right),
                BinaryNode('&', node.left, neg_nnf(node.right)))
        elif node.operator == '^':
            return BinaryNode('=', node.left, node.right)
    raise ValueError("Invalid node type")

def bnf_to_nnf(node: ASTNode) -> ASTNode:
    if isinstance(node, OperandNode):
        return node
    elif isinstance(node, UnaryNode):
        return neg_nnf(bnf_to_nnf(node.operand))
    elif isinstance(node, BinaryNode):
        if node.operator in {'&', '|'}:
            return BinaryNode(node.operator, 
                            bnf_to_nnf(node.left), 
                            bnf_to_nnf(node.right))
        elif node.operator == '>':
            return BinaryNode('|', 
                            neg_nnf(bnf_to_nnf(node.left)), 
                            bnf_to_nnf(node.right))
        elif node.operator == '=':
            return BinaryNode('&',
                            BinaryNode('|', bnf_to_nnf(node.left), neg_nnf(bnf_to_nnf(node.right))),
                            BinaryNode('|', neg_nnf(bnf_to_nnf(node.left)), bnf_to_nnf(node.right)))
        elif node.operator == '^':
            return BinaryNode('|',
                            BinaryNode('&', bnf_to_nnf(node.left), neg_nnf(bnf_to_nnf(node.right))),
                            BinaryNode('&', neg_nnf(bnf_to_nnf(node.left)), bnf_to_nnf(node.right)))
    raise ValueError("Invalid node type")

def transform_operations(node: ASTNode) -> None:
    if isinstance(node, BinaryNode):
        transform_operations(node.left)
        transform_operations(node.right)
        
        if node.operator in {'&', '|'} and isinstance(node.left, BinaryNode) and node.left.operator == node.operator:
            left_node = node.left
            node.left = left_node.left
            node.right = BinaryNode(node.operator, left_node.right, node.right)
            transform_operations(node)

def transform_disjunction_to_conjunction(node: ASTNode) -> None:
    if isinstance(node, BinaryNode):
        transform_disjunction_to_conjunction(node.left)
        transform_disjunction_to_conjunction(node.right)

        if node.operator == '|':
            if isinstance(node.right, BinaryNode) and node.right.operator == '&':
                node.operator = '&'
                old_left = node.left
                node.left = BinaryNode('|', old_left, node.right.left)
                node.right = BinaryNode('|', old_left, node.right.right)

def conjunctive_normal_form(formula: str) -> str:
    tokens = [c for c in formula if c in set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!&|^>=')]
    ast = parse_expression(tokens)
    if not ast:
        return ""
        
    nnf = bnf_to_nnf(ast)
    transform_operations(nnf)
    transform_disjunction_to_conjunction(nnf)
    
    return nnf.get_postfix()

# Tests
if __name__ == "__main__":
    test_cases = [
        "AB&!", # A!B!| 
        "AB|!", # A!B!&
        "AB|C&", # AB|C&
        "AB|C|D|", # ABCD|||
        "AB&C&D&", # ABCD&&&
        "AB&!C!|", # A!B!C!||
        "AB|!C!&", # A!B!C!&&
    ]
    
    for test in test_cases:
        result = conjunctive_normal_form(test)
        print(f"{test} -> {result}")