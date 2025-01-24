class AstNode:
    def __init__(self, item):
        self.item = item
        self.left_leaf = None
        self.right_leaf = None

    def parse_formula(self, formula):
        operands = ['!', '&', '|', '^', '>', '=']
        self.item = formula[-1]
        c = formula.pop()
        if c in operands:
            if c != '!':
                self.right_leaf = AstNode('0')
                self.right_leaf.parse_formula(formula)
            self.left_leaf = AstNode('0')
            self.left_leaf.parse_formula(formula)

    def is_in(self, haystack):
        return self.item in haystack

    def negation_normal_form(self):
        if self.left_leaf:
            self.left_leaf.negation_normal_form()
        if self.right_leaf:
            self.right_leaf.negation_normal_form()

        if self.item == '!' and self.left_leaf and self.left_leaf.is_in("&|"):
            right_cpy = self.left_leaf.right_leaf

            if self.left_leaf.item == '|':
                self.item = '&'
            else:
                self.item = '|'

            self.left_leaf.item = '!'
            self.left_leaf.right_leaf = None

            self.right_leaf = AstNode('!')
            self.right_leaf.left_leaf = right_cpy

            self.negation_normal_form()

        if self.item == '=':
            self.item = '&'
            a_cpy = self.left_leaf
            b_cpy = self.right_leaf

            self.left_leaf = AstNode('>')
            self.right_leaf = AstNode('>')

            self.left_leaf.left_leaf = a_cpy
            self.left_leaf.right_leaf = b_cpy

            self.right_leaf.left_leaf = b_cpy
            self.right_leaf.right_leaf = a_cpy

            self.negation_normal_form()

        if self.item == '^':
            self.item = '|'
            a_cpy = self.left_leaf
            b_cpy = self.right_leaf

            self.left_leaf = AstNode('&')
            self.right_leaf = AstNode('&')

            self.left_leaf.right_leaf = AstNode('!')
            self.left_leaf.right_leaf.left_leaf = b_cpy
            self.left_leaf.left_leaf = a_cpy

            self.right_leaf.left_leaf = AstNode('!')
            self.right_leaf.left_leaf.left_leaf = a_cpy
            self.right_leaf.right_leaf = b_cpy

            self.negation_normal_form()

        if self.item == '>':
            left_cpy = self.left_leaf
            self.item = '|'
            self.left_leaf = AstNode('!')
            self.left_leaf.left_leaf = left_cpy
            self.negation_normal_form()

    def stringify(self):
        expr = ""

        if self.left_leaf:
            expr += self.left_leaf.stringify()

        if self.right_leaf:
            expr += self.right_leaf.stringify()

        expr += self.item
        return expr

    def is_conjunctive(self):
        if self.item == '|':
            if (self.right_leaf and self.right_leaf.item == '&' or
                self.left_leaf and self.left_leaf.item == '&') and \
               (self.right_leaf and self.right_leaf.is_in("&|") or
                self.left_leaf and self.left_leaf.is_in("&|")):
                return False
        return True

    def conjunctive_normal_form(self):
        if self.left_leaf:
            self.left_leaf.conjunctive_normal_form()
        if self.right_leaf:
            self.right_leaf.conjunctive_normal_form()

        if not self.is_conjunctive():
            self.item = '&'
            x_cpy = self.left_leaf
            a_cpy = self.right_leaf.left_leaf
            b_cpy = self.right_leaf.right_leaf

            self.left_leaf = AstNode('|')
            self.right_leaf = AstNode('|')

            self.left_leaf.left_leaf = x_cpy
            self.left_leaf.right_leaf = a_cpy

            self.right_leaf.left_leaf = x_cpy
            self.right_leaf.right_leaf = b_cpy

        if self.is_in("&|"):
            if (self.left_leaf and self.left_leaf.item == self.item) and \
               (self.right_leaf and self.right_leaf.is_in("!") or
                self.right_leaf and self.right_leaf.item.isalnum()):
                right_child_cpy = self.right_leaf
                left_child_cpy = self.left_leaf
                self.right_leaf = left_child_cpy
                self.left_leaf = right_child_cpy


def conjunctive_normal_form(formula):
    formula_stack = list(formula)
    root = AstNode('0')
    root.parse_formula(formula_stack)
    root.negation_normal_form()
    root.conjunctive_normal_form()
    return root.stringify()


# Tests
if __name__ == "__main__":
    assert conjunctive_normal_form("AB&!") == "A!B!|"
    assert conjunctive_normal_form("AB|!") == "A!B!&"
    assert conjunctive_normal_form("AB|C&") == "AB|C&"
    assert conjunctive_normal_form("AB|C|D|") == "DCAB|||"
    assert conjunctive_normal_form("AB&C&D&") == "DCAB&&&"
    assert conjunctive_normal_form("AB&!C!|") == "C!A!B!||"
    assert conjunctive_normal_form("AB|!C!&") == "C!A!B!&&"
    assert conjunctive_normal_form("ABDE&|&") == "ABD|BE|&&"
    assert conjunctive_normal_form("A") == "A"
    assert conjunctive_normal_form("A!") == "A!"
    assert conjunctive_normal_form("AB|C&") == "AB|C&"
    assert conjunctive_normal_form("A!B|") == "A!B|"
    assert conjunctive_normal_form("AB!&") == "AB!&"

    print("All tests passed!")