from dataclasses import dataclass
from typing import Optional
from enum import Enum
import unittest

class OperatorType(Enum):
    OPERAND = "OPERAND"
    NOT = "NOT"
    AND = "AND"
    OR = "OR"

@dataclass
class Operator:
    type: OperatorType
    value: Optional[str] = None
    left: Optional['Operator'] = None
    right: Optional['Operator'] = None

    @staticmethod
    def from_formula(formula: str) -> Optional['Operator']:
        if not formula:
            return None
            
        stack = []
        for char in formula:
            if char.isalpha():
                stack.append(Operator(OperatorType.OPERAND, char))
            elif char == '!':
                if not stack:
                    return None
                operand = stack.pop()
                stack.append(Operator(OperatorType.NOT, left=operand))
            elif char in '&|':
                if len(stack) < 2:
                    return None
                right = stack.pop()
                left = stack.pop()
                op_type = OperatorType.AND if char == '&' else OperatorType.OR
                stack.append(Operator(op_type, left=left, right=right))
                
        return stack[0] if len(stack) == 1 else None

    def to_negation_normal_form(self) -> 'Operator':
        if self.type == OperatorType.OPERAND:
            return self
        elif self.type == OperatorType.NOT:
            if self.left.type == OperatorType.OPERAND:
                return self
            elif self.left.type == OperatorType.NOT:
                return self.left.left.to_negation_normal_form()
            elif self.left.type == OperatorType.AND:
                return Operator(
                    OperatorType.OR,
                    left=Operator(OperatorType.NOT, left=self.left.left).to_negation_normal_form(),
                    right=Operator(OperatorType.NOT, left=self.left.right).to_negation_normal_form()
                )
            elif self.left.type == OperatorType.OR:
                return Operator(
                    OperatorType.AND,
                    left=Operator(OperatorType.NOT, left=self.left.left).to_negation_normal_form(),
                    right=Operator(OperatorType.NOT, left=self.left.right).to_negation_normal_form()
                )
        elif self.type in (OperatorType.AND, OperatorType.OR):
            return Operator(
                self.type,
                left=self.left.to_negation_normal_form(),
                right=self.right.to_negation_normal_form()
            )
        return self

    def to_conjunctive_normal_form(self) -> 'Operator':
        if self.type == OperatorType.OPERAND:
            return self
        elif self.type == OperatorType.NOT:
            return Operator(OperatorType.NOT, left=self.left.to_conjunctive_normal_form())
        elif self.type == OperatorType.AND:
            return Operator(
                OperatorType.AND,
                left=self.left.to_conjunctive_normal_form(),
                right=self.right.to_conjunctive_normal_form()
            )
        elif self.type == OperatorType.OR:
            a = self.left.to_conjunctive_normal_form()
            b = self.right.to_conjunctive_normal_form()
            
            if a.type == OperatorType.AND:
                return Operator(
                    OperatorType.AND,
                    left=Operator(OperatorType.OR, left=a.left, right=b).to_conjunctive_normal_form(),
                    right=Operator(OperatorType.OR, left=a.right, right=b).to_conjunctive_normal_form()
                )
            elif b.type == OperatorType.AND:
                return Operator(
                    OperatorType.AND,
                    left=Operator(OperatorType.OR, left=a, right=b.left).to_conjunctive_normal_form(),
                    right=Operator(OperatorType.OR, left=a, right=b.right).to_conjunctive_normal_form()
                )
            return Operator(OperatorType.OR, left=a, right=b)
        
        raise ValueError(f"Operator {self.type} not allowed. Expression must be in NNF")

    def __str__(self) -> str:
        if self.type == OperatorType.OPERAND:
            return self.value
        elif self.type == OperatorType.NOT:
            return f"{self.left}!"
        else:
            op = "&" if self.type == OperatorType.AND else "|"
            return f"{self.left}{self.right}{op}"

def conjunctive_normal_form(formula: str) -> str:
    operator = Operator.from_formula(formula)
    if operator is None:
        return ""
        
    result = str(operator.to_negation_normal_form().to_conjunctive_normal_form())
    n = result.count("&")
    result = "".join(c for c in result if c != "&")
    return result + "&" * n

class TestCNF(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(conjunctive_normal_form(""), "")
        
    def test_negated_and(self):
        self.assertEqual(conjunctive_normal_form("AB&!"), "A!B!|")
        
    def test_negated_or(self):
        self.assertEqual(conjunctive_normal_form("AB|!"), "A!B!&")
        
    def test_deep_and(self):
        self.assertEqual(conjunctive_normal_form("AB|C&D&"), "AB|CD&&")
        
    def test_many_ors(self):
        self.assertEqual(conjunctive_normal_form("AB|C|D|"), "AB|C|D|")
        
    def test_many_ands(self):
        self.assertEqual(conjunctive_normal_form("AB&C&D&"), "ABCD&&&")
        
    def test_complicated(self):
        self.assertEqual(conjunctive_normal_form("AB&!C!|"), "A!B!|C!|")
        
    def test_last_subject(self):
        self.assertEqual(conjunctive_normal_form("AB|!C!&"), "A!B!C!&&")

if __name__ == "__main__":
    unittest.main()