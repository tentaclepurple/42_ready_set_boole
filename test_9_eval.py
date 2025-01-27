from set_evaluation import eval_set

def test_set_evaluation():

    test_cases = [
        # Base cases from the original exercise
        {
            "formula": 'ABC||',
            "sets": [[], [], []],
            "expected": [],
        },
        {
            "formula": "ABC||",
            "sets": [[0], [1], [2]],
            "expected": [0, 1, 2],
        },
        {
            "formula": "ABC||",
            "sets": [[0], [0], [0]],
            "expected": [0],
        },
        {
            "formula": "ABC&&",
            "sets": [[0], [0], []],
            "expected": [],
        },
        {
            "formula": "ABC&&",
            "sets": [[0], [0], [0]],
            "expected": [0],
        },
        {
            "formula": "ABC^^",
            "sets": [[0], [0], [0]],
            "expected": [0],
        },
        {
            "formula": "ABC>>",
            "sets": [[0], [0], [0]],
            "expected": [0],
        },
    ]
    
    print("\nTesting Set Evaluation")
    print("=" * 60)
    
    for test in test_cases:
        formula = test["formula"]
        sets = test["sets"]
        expected = test["expected"]
        
        print(f"\nFormula: {formula}")
        print(f"Input sets: {sets}")
        print(f"Expected: {expected}")
        
        result = eval_set(formula, sets)
        print(f"Result:   {result}")
        
        if sorted(result) == sorted(expected):
            print("✓ Test passed")
        else:
            print("✗ Test failed")
            print(f"Difference: expected {expected}, got {result}")
            
        print("-" * 60)

if __name__ == "__main__":
    test_set_evaluation()