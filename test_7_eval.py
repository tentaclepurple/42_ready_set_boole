from sat import sat


def test_sat():
    """
    Test the SAT solver with various formulas
    """
    test_cases = [
        ('ABC||', True),
        ('AB&A!B!&&', False),
        ('ABCDE&&&&', True),
        ('AAA^^', True),
        ('ABCDE^^^^', True)
    ]
    
    print("=" * 60)
    
    for formula, expected in test_cases:
        result = sat(formula)
        print(f"\nFormula: {formula}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")

        print("-" * 60)


if __name__ == "__main__":
    test_sat()
