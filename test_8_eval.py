from powerset import powerset, powerset_itertools
from time import time


test_cases = [
    ([], [[]]),
    
    # Single element
    ([0], [[], [0]]),
    
    # Two elements
    ([0, 1], [[], [0], [1], [0, 1]]),
    
    # Three elements
    ([0, 1, 2], [[], [0], [1], [2], [0, 1], [1, 2], [0, 2], [0, 1, 2]]),

    ]



def test_powerset():

    print("\nTesting Powerset Generator")
    print("=" * 60)
    
    for input_set, expected in test_cases:
        print(f"\nInput set: {input_set}")
        print(f"Expected: {expected}")
        
        result = powerset(input_set)
        print(f"Got:      {result}")
        
        expected_size = 2 ** len(input_set)
        print(f"Number of subsets: {len(result)} (should be 2^{len(input_set)} = {expected_size})")
        
        if sorted(map(sorted, result)) == sorted(map(sorted, expected)):
            print("✓ Test passed")
        else:
            print("✗ Test failed")
        print("-" * 60)


if __name__ == "__main__":
    test_powerset()
