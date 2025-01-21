from powerset import powerset, powerset_itertools
from time import time


test_cases = [
    # Empty set
    ([], [[]]),
    
    # Single element
    ([1], [[], [1]]),
    
    # Two elements
    ([1, 2], [[], [2], [1], [1, 2]]),
    
    # Three elements
    ([1, 2, 3], [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]),

    # Not consecutive elements
    ([5, 10, 15, 8,], [[], [5], [10], [5, 10], [15], [5, 15], [10, 15], [5, 10, 15], [8], [5, 8], [10, 8], [5, 10, 8], [15, 8], [5, 15, 8], [10, 15, 8], [5, 10, 15, 8]]),
    ]

def test_powerset():
    """
    Tests the powerset generation with various input sets.
    Shows the complete process of generating all subsets.
    """
    print("\nTesting Powerset Generator")
    print("=" * 60)
    
    for input_set, expected in test_cases:
        print(f"\nInput set: {input_set}")
        print(f"Expected subsets: {expected}")
        
        result = powerset(input_set)
        print(f"Got:      {result}")
        
        # Verify number of subsets
        expected_size = 2 ** len(input_set)
        print(f"Number of subsets: {len(result)} (should be 2^{len(input_set)} = {expected_size})")
        
        if sorted(map(sorted, result)) == sorted(map(sorted, expected)):
            print("✓ Test passed")
        else:
            print("✗ Test failed")
        print("-" * 60)


def test_powerset_itertools():
    """
    Tests the powerset generation with various input sets.
    Shows the complete process of generating all subsets.
    """
    print("\nTesting Powerset Generator with itertools")
    print("=" * 60)
    
    for input_set, expected in test_cases:
        print(f"\nInput set: {input_set}")
        print(f"Expected subsets: {expected}")
        
        result = powerset_itertools(input_set)
        print(f"Got:      {result}")
        
        # Verify number of subsets
        expected_size = 2 ** len(input_set)
        print(f"Number of subsets: {len(result)} (should be 2^{len(input_set)} = {expected_size})")
        
        if sorted(map(sorted, result)) == sorted(map(sorted, expected)):
            print("✓ Test passed")
        else:
            print("✗ Test failed")
        print("-" * 60)


if __name__ == "__main__":
    init_time = time()
    test_powerset()
    manual_time = time() - init_time

    init_time = time()
    test_powerset_itertools()
    itertools_time = time() - init_time
    
    print(f"\nTime taken with manual powerset: {manual_time:.6f} sec")
    print(f"\nTime taken with itertools powerset: {itertools_time:.6f} sec")