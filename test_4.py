from truth_table import TruthTable


def test_truth_tables():
    
    test_cases = [
        ("AB&", "A AND B"),
        ("AB|", "A OR B"),
        ("AB=", "A EQUALS B"),
        ("AB>", "A IMPLIES B"),
        ("A!", "NOT A"),
        ("ABC||", "A OR B OR C"),
        ("AB&C|", "(A AND B) OR C"),
        ("AB&", "A NOT B"),
    ]
    
    for formula, description in test_cases:
        print(f"\nTesting: {formula} ({description})")
        print("-" * 40)
        TruthTable.print_truth_table(formula)

if __name__ == "__main__":
    test_truth_tables()