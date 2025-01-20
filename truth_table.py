class TruthTable:
    @staticmethod
    def validate_formula(formula: str) -> bool:
        """
        Validates if a formula follows correct RPN syntax.
        Returns True if valid, raises ValueError if invalid.
        
        Example of valid formulas:
        - "AB&"   (A AND B)
        - "A!"    (NOT A)
        - "AB&C|" ((A AND B) OR C)
        """
        stack = []
        
        for i, char in enumerate(formula):
            if char.isalpha():  # Variables
                stack.append(char)
                
            elif char == '!':  # NOT operator
                if not stack:
                    raise ValueError(f"Invalid formula: NOT operator at position {i} has no operand")
                operand = stack.pop()
                stack.append(f"!{operand}")  # Push result back
                
            elif char in {'&', '|', '^', '>', '='}:  # Binary operators
                if len(stack) < 2:
                    raise ValueError(f"Invalid formula: {char} operator at position {i} needs two operands")
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                stack.append(f"({a}{char}{b})")  # Push result back
                
            else:
                raise ValueError(f"Invalid character '{char}' at position {i}")
        
        # At the end, we should have exactly one result
        if len(stack) != 1:
            raise ValueError("Invalid formula: incorrect number of operands")
        
        return True

    @staticmethod
    def evaluate_formula(formula: str, values: dict) -> bool:
        """
        Evaluates an RPN formula with given variable values.
        
        Args:
            formula: The RPN formula to evaluate
            values: Dictionary mapping variables to their boolean values
        """
        stack = []
        
        for char in formula:
            if char.isalpha():  # Variables
                stack.append(values[char])
                
            elif char == '!':  # NOT
                operand = stack.pop()
                stack.append(not operand)
                
            else:  # Binary operators
                b = stack.pop()
                a = stack.pop()
                
                if char == '&':    # AND
                    stack.append(a and b)
                elif char == '|':   # OR
                    stack.append(a or b)
                elif char == '^':   # XOR
                    stack.append(a != b)
                elif char == '>':   # IMPLIES
                    stack.append(not a or b)
                elif char == '=':   # EQUALS
                    stack.append(a == b)
        
        return stack[0]

    @staticmethod
    def print_truth_table(formula: str):
        """
        Prints the truth table for a boolean formula in RPN notation.
        First validates the formula, then generates and evaluates all possible combinations.
        
        Args:
            formula: The RPN formula to evaluate (e.g., "AB&" for A AND B)
        """
        try:
            # First validate the formula
            TruthTable.validate_formula(formula)
            
            # Get unique variables in order of appearance
            variables = []
            for char in formula:
                if char.isalpha() and char not in variables:
                    variables.append(char)
            
            # Print header
            print("| " + " | ".join(variables) + " | = |")
            print("|" + "---|" * (len(variables) + 1))
            
            # Generate and evaluate all possible combinations
            combinations = 2 ** len(variables)
            for i in range(combinations):
                # Create variable assignments for this combination
                values = {}
                row_values = []
                
                for j, var in enumerate(variables):
                    # Extract the j-th bit from i
                    bit = (i >> (len(variables) - 1 - j)) & 1
                    values[var] = bool(bit)
                    row_values.append(str(int(bit)))
                
                # Evaluate formula with these values
                result = TruthTable.evaluate_formula(formula, values)
                
                # Print the row
                print("| " + " | ".join(row_values) + f" | {int(result)} |")
                
        except ValueError as e:
            print(f"Error: {e}")
            return