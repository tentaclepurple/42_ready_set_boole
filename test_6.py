from conjunction_normal_form import conjunctive_normal_form


def test_cnf():
    """
    Tests the CNF converter with various test cases from the exercise requirements
    Each test case includes: input formula, expected output, and explanation
    """
    test_cases = [
        # Basic negations
        ("AB&!", "A!B!|", "Simple De Morgan: NOT(A AND B) -> (NOT A) OR (NOT B)"),
        ("AB|!", "A!B!&", "Simple De Morgan: NOT(A OR B) -> (NOT A) AND (NOT B)"),
        
        # Simple conjunctions and disjunctions
        ("AB|C&", "AB|C&", "Already in CNF: (A OR B) AND C"),
        ("AB|C|D|", "ABCD|||", "Single OR clause: A OR B OR C OR D"),
        ("AB&C&D&", "ABCD&&&", "Single AND of literals: A AND B AND C AND D"),
        
        # Complex cases with distribution
        ("AB&!C!|", "A!B!C!||", "NOT(A AND B) OR NOT(C)"),
        ("AB|!C!&", "A!B!C!&&", "NOT(A OR B) AND NOT(C)"),
        
        # Main example from exercise
        ("ABCD&|&", "ABC|BD|&&", "A AND (B OR (C AND D)) -> A AND (B OR C) AND (B OR D)"),
        
        # Complex operators
        ("AB>", "A!B|", "A IMPLIES B -> NOT A OR B"),
        ("AB=", "A!B|B!A|&", "A EQUALS B -> (NOT A OR B) AND (NOT B OR A)"),
        ("AB^", "AB|A!B!|&", "A XOR B -> (A OR B) AND (NOT A OR NOT B)"),
    ]
    
    print("\nTesting CNF Converter")
    print("=" * 60)
    
    for formula, expected, explanation in test_cases:
        result = conjunctive_normal_form(formula)
        print(f"\nTesting: {formula}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        print(f"Description: {explanation}")
        
        if result == expected:
            print("✓ PASS")
        else:
            print(f"✗ FAIL")
        print("-" * 60)


if __name__ == "__main__":
    test_cnf()
