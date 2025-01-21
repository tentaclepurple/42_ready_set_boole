from set_evaluation import eval_set


def test_set_evaluation():
    """
    Comprehensive tests for set evaluation covering all operators.
    Each test case includes detailed explanation of the expected behavior.
    """
    test_cases = [
        # Base cases from the original exercise
        {
            "formula": "AB&",
            "sets": [[0, 1, 2], [0, 3, 4]],
            "expected": [0],
            "explanation": "A ∩ B: Only elements present in both sets"
        },
        {
            "formula": "AB|",
            "sets": [[0, 1, 2], [3, 4, 5]],
            "expected": [0, 1, 2, 3, 4, 5],
            "explanation": "A ∪ B: All elements from both sets combined"
        },
        {
            "formula": "A!",
            "sets": [[1, 2]],
            "expected": [],
            "explanation": "¬A: All elements in universe not in A"
        },
        
        # Testing equivalence with equal sets
        {
            "formula": "AB=",
            "sets": [[1, 2], [1, 2]],
            "expected": [1, 2],
            "explanation": "A ↔ B: When sets are equal, result is the set itself"
        },
        
        # Testing equivalence with overlapping sets
        {
            "formula": "AB=",
            "sets": [[1, 2], [2, 3]],
            "expected": [2],
            "explanation": "A ↔ B: Elements that are either in both sets or in neither"
        },
        
        # Testing equivalence with disjoint sets
        {
            "formula": "AB=",
            "sets": [[1, 2], [3, 4]],
            "expected": [],
            "explanation": "A ↔ B: Empty when sets have no elements in common and cover universe"
        },
        
        # Complex operations
        {
            "formula": "AB|C&",
            "sets": [[0, 1], [2, 3], [1, 2]],
            "expected": [1, 2],
            "explanation": "(A ∪ B) ∩ C: Union then intersection"
        },
        
        # Testing XOR
        {
            "formula": "AB^",
            "sets": [[1, 2, 3], [2, 3, 4]],
            "expected": [1, 4],
            "explanation": "A ⊕ B: Elements in either set but not in both"
        }
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
        print(f"Explanation: {test['explanation']}")
        
        result = eval_set(formula, sets)
        print(f"Result: {result}")
        
        if sorted(result) == sorted(expected):
            print("✓ Test passed")
        else:
            print("✗ Test failed")
            print(f"Difference: expected {expected}, got {result}")
            
        print("-" * 60)

if __name__ == "__main__":
    test_set_evaluation()