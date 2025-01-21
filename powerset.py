from itertools import combinations


class PowerSetGenerator:
    """
    Generates the powerset of a given set of integers.
    The powerset P(A) of a set A is the set of all possible subsets of A,
    including the empty set and A itself.
    """
    
    @staticmethod
    def generate_powerset(input_set: list) -> list:
        """
        Generates all possible subsets of the input set.
        Uses binary numbers to represent subset combinations.
        
        For example, for set {1, 2, 3}:
        000 -> {}
        001 -> {3}
        010 -> {2}
        011 -> {2, 3}
        100 -> {1}
        101 -> {1, 3}
        110 -> {1, 2}
        111 -> {1, 2, 3}
        """
        n = len(input_set)
        powerset = []
        
        # Generate 2^n different combinations
        for i in range(2 ** n):
            subset = []
            
            # Check each bit position
            for j in range(n):
                # If bit j is set in i, include element j
                if (i & (1 << j)):
                    subset.append(input_set[j])
            
            powerset.append(subset)
            
        return powerset


def powerset(input_set: list) -> list:
    """
    Wrapper function that generates the powerset of a given set.
    Returns a list of lists, where each inner list is a subset.
    """
    return PowerSetGenerator.generate_powerset(input_set)


def powerset_itertools(input_set):
    """
    Creates a powerset using itertools.combinations
    
    Args:
        input_set: List or set of elements
        
    Returns:
        List of all possible combinations, including empty set and full set
    """
    result = []
    # For each possible length (0 to len(input_set))
    for r in range(len(input_set) + 1):
        # Generate all combinations of that length
        for combo in combinations(input_set, r):
            result.append(list(combo))
    return result