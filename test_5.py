from negation_normal_form import negation_normal_form


def test_nnf():
    """
    Test cases for Negation Normal Form conversion
    """
    test_cases = [
        # De Morgan's laws
        ("AB&!", "A!B!|", "NOT(A AND B) -> (NOT A) OR (NOT B)"),
        ("AB|!", "A!B!&", "NOT(A OR B) -> (NOT A) AND (NOT B)"),
        
        # Material conditions (implications)
        ("AB>", "A!B|", "A IMPLIES B -> NOT A OR B"),
        
        # Equivalence
        ("AB=", "A!B|B!A|&", "A EQUALS B -> (NOT A OR B) AND (NOT B OR A)"),
        
        # Double negation
        ("A!!", "A", "NOT NOT A -> A"),
        
        # Complex formulas
        ("AB|C&!", "A!B!&C!|", "NOT((A OR B) AND C) -> (NOT A AND NOT B) OR NOT C"),
    ]
    
    print("\nTesting NNF Converter")
    print("=" * 60)
    
    for formula, expected, explanation in test_cases:
        result = negation_normal_form(formula)
        print(f"\nInput:      {formula}")
        print(f"Expected:   {expected}")
        print(f"Got:        {result}")
        print(f"Explanation: {explanation}")
        assert result == expected, f"Test failed for {formula}"
        print("✓ Test passed")

if __name__ == "__main__":
    test_nnf()