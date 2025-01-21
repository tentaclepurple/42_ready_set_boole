class SATSolver:
    """
    Determines if a boolean formula in RPN is satisfiable.
    A formula is satisfiable if there exists at least one assignment
    of boolean values to its variables that makes it evaluate to True.
    """
    def __init__(self):
        self.binary_ops = {'&', '|', '^', '>', '='}
        
    def get_variables(self, formula: str) -> list:
        """
        Extracts all unique variables from the formula in order of appearance
        """
        return [c for c in formula if c.isalpha()]
        
    def evaluate(self, formula: str, values: dict) -> bool:
        """
        Evaluates a formula with the given variable assignments
        """
        stack = []
        
        for char in formula:
            if char.isalpha():  # Variable
                stack.append(values[char])
            elif char == '!':  # NOT
                operand = stack.pop()
                stack.append(not operand)
            elif char in self.binary_ops:  # Binary operator
                b = stack.pop()
                a = stack.pop()
                
                if char == '&':
                    stack.append(a and b)
                elif char == '|':
                    stack.append(a or b)
                elif char == '^':
                    stack.append(a != b)
                elif char == '>':
                    stack.append(not a or b)
                elif char == '=':
                    stack.append(a == b)
        
        return stack[0]
        
    def is_satisfiable(self, formula: str) -> bool:
        """
        Determines if the formula is satisfiable by trying all possible
        combinations of True/False for each variable.
        """
        try:
            # Get unique variables
            variables = list(dict.fromkeys(self.get_variables(formula)))
            num_vars = len(variables)
            
            # Try all possible combinations
            for i in range(2 ** num_vars):
                # Create variable assignments from binary representation of i
                values = {}
                for j, var in enumerate(variables):
                    # Extract bit j from i
                    bit = (i >> (num_vars - 1 - j)) & 1
                    values[var] = bool(bit)
                
                # If we find a satisfying assignment, return True
                if self.evaluate(formula, values):
                    return True
            
            # If no assignment worked, return False
            return False
            
        except Exception as e:
            print(f"Error processing formula: {e}")
            return False


def sat(formula: str) -> bool:
    """
    Wrapper function to check if a formula is satisfiable.
    """
    solver = SATSolver()
    return solver.is_satisfiable(formula)