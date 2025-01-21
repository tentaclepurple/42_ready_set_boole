class SetEvaluator:
    """
    Evaluates set operations using boolean formula notation.
    Maps logical operations to set operations:
    AND (&) -> intersection (∩)
    OR (|) -> union (∪)
    NOT (!) -> complement
    XOR (^) -> symmetric difference
    """
    def __init__(self):
        self.binary_ops = {'&', '|', '^', '>', '='}
    
    def get_universe(self, sets: list) -> set:
        """Gets the universe set (union of all input sets)"""
        universe = set()
        for s in sets:
            universe.update(s)
        return universe

    def complement(self, set_a: set, universe: set) -> set:
        """Returns the complement of set_a with respect to the universe"""
        return universe - set_a

    def evaluate_sets(self, formula: str, sets: list) -> set:
        """
        Evaluates a formula in RPN using set operations.
        Each operator is converted to its set theory equivalent.
        """
        try:
            # Create universe and mapping of variables to sets
            universe = self.get_universe(sets)
            set_map = {chr(65+i): set(s) for i, s in enumerate(sets)}
            stack = []
            
            for char in formula:
                if char.isalpha():
                    if char not in set_map:
                        raise ValueError(f"No set provided for {char}")
                    stack.append(set_map[char])
                
                elif char == '!':
                    if not stack:
                        raise ValueError("Invalid complement operation")
                    set_a = stack.pop()
                    stack.append(self.complement(set_a, universe))
                
                elif char in self.binary_ops:
                    if len(stack) < 2:
                        raise ValueError(f"Not enough operands for {char}")
                    set_b = stack.pop()
                    set_a = stack.pop()
                    
                    if char == '&':    # Intersection
                        result = set_a & set_b
                    elif char == '|':   # Union
                        result = set_a | set_b
                    elif char == '^':   # Symmetric difference
                        result = (set_a | set_b) - (set_a & set_b)
                    elif char == '>':   # Implication: A → B = ¬A ∪ B
                        result = self.complement(set_a, universe) | set_b
                    elif char == '=':   # Equivalence: A ↔ B = (A ∩ B) ∪ (¬A ∩ ¬B)
                        comp_a = self.complement(set_a, universe)
                        comp_b = self.complement(set_b, universe)
                        result = (set_a & set_b) | (comp_a & comp_b)
                    
                    stack.append(result)
            
            if len(stack) != 1:
                raise ValueError("Invalid formula structure")
                
            return stack[0]
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return set()

def eval_set(formula: str, sets: list) -> list:
    """Wrapper function that evaluates the formula and returns sorted result"""
    evaluator = SetEvaluator()
    result = evaluator.evaluate_sets(formula, sets)
    return sorted(list(result))