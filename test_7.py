from sat import sat


def test_sat():
    """
    Test the SAT solver with various formulas
    """
    test_cases = [
        # Basic satisfiable cases
        ("AB|", True, "A OR B - satisfiable because we can make A or B true"),
        ("AB&", True, "A AND B - satisfiable when both A and B are true"),
        
        # Basic unsatisfiable cases
        ("AA!&", False, "A AND NOT A - never true because it's a contradiction"),
        ("AA^", False, "A XOR A - never true because a value can't be different from itself"),
        
        # More complex cases
        ("AB|C&", True, "(A OR B) AND C - satisfiable with C=true and either A or B true"),
        ("AB&C!&", True, "(A AND B) AND NOT C - satisfiable with A=B=true and C=false"),
        ("AA!|", True, "A OR NOT A - always true (law of excluded middle)"),
        
        # Cases with implications and equivalences
        ("AB>", True, "A IMPLIES B - satisfiable (false implies anything is true)"),
        ("AB=", True, "A EQUALS B - satisfiable when A and B have same value"),
    ]
    
    print("\nTesting SAT Solver")
    print("=" * 60)
    
    for formula, expected, explanation in test_cases:
        result = sat(formula)
        print(f"\nFormula: {formula}")
        print(f"Expected: {'satisfiable' if expected else 'unsatisfiable'}")
        print(f"Got: {'satisfiable' if result else 'unsatisfiable'}")
        print(f"Explanation: {explanation}")
        assert result == expected, f"Test failed for {formula}"
        print("✓ Test passed")
        print("-" * 60)


if __name__ == "__main__":
    test_sat()
