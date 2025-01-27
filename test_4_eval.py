from truth_table import TruthTable


def test_truth_tables():
    
    test_cases = [
        'ABC==',
        'AB>C>',
        'AB>A>A>'
    ]
    
    for formula in test_cases:
        print(f"\nTesting: {formula}")
        print("-" * 40)
        TruthTable.print_truth_table(formula)

if __name__ == "__main__":
    test_truth_tables()