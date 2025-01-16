def adder(a: int, b: int) -> int:
    """
    Adds two natural numbers using only bitwise operations.
    
    Args:
        a: First natural number
        b: Second natural number
    
    Returns:
        The sum of a and b
    
    How it works:
    1. XOR (^) gives us the sum without considering carries
    2. AND (&) with left shift (<<) gives us the carries
    3. We repeat until there are no more carries to process
    
    Example for 3 + 2:
    3 = 11 in binary
    2 = 10 in binary
    
    First iteration:
    XOR:   11 ^ 10 = 01 (sum without carries)
    AND:   11 & 10 = 10 (positions where carries occur)
    Shift: 10 << 1 = 100 (carries for next iteration)
    
    Second iteration:
    XOR:   001 ^ 100 = 101 (5 in decimal, our final result)
    AND:   001 & 100 = 000 (no more carries, we're done)
    """
    while b != 0:
        # Store the carries - each '1' bit in carry represents a position
        # where adding the bits from a and b would generate a carry
        carry = a & b
        
        # XOR gives us the basic sum without carries
        # e.g., 1+1=0, 1+0=1, 0+1=1, 0+0=0
        a = a ^ b
        
        # Shift carries one position left (multiply by 2)
        # as they need to be added to the next bit position
        b = carry << 1
    
    return a

# Main function with test cases
def main():
    # Test cases with expected results
    test_cases = [
        (5, 3),    # Should be 8
        (10, 5),   # Should be 15
        (0, 7),    # Should be 7
        (15, 15),  # Should be 30
    ]
    
    for a, b in test_cases:
        result = adder(a, b)
        print(f"{a} + {b} = {result}")
        # Verification
        assert result == a + b, f"Error: {a} + {b} should be {a + b}, got {result}"

if __name__ == "__main__":
    main()