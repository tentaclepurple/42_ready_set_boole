from conjunction_normal_form import conjunctive_normal_form
from truth_table import TruthTable

test_cases = [
    'ABC||!',
    'ABC&|',
    'ABC&|!',
    'ABC^^',
    'ABC>>',
]

def test_cnf():
    for formula in test_cases:
        print()
        print(formula)
        TruthTable.print_truth_table(formula)
        result = conjunctive_normal_form(formula)
        print(result)
        TruthTable.print_truth_table(result)
        print()


if __name__ == "__main__":
    test_cnf()
