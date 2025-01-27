from nnf import negation_normal_form
from truth_table import TruthTable


def test_nnf():
    """
    Test cases for Negation Normal Form conversion
    """
    test_cases = [
        'ABC||!',
        'ABC&|!',
    ]
    


    print("\nTesting NNF Converter")
    print("=" * 60)
    
    for formula in test_cases:
        result = negation_normal_form(formula)
        print(f"\ninput:      {formula}")
        TruthTable.print_truth_table(formula)
        print(f"nnf:        {result}")
        TruthTable.print_truth_table(result)


if __name__ == "__main__":
    test_nnf()