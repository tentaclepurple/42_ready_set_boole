from boolean_algebra import BooleanAlgebra

def test_adder():
    """
    Simple function to test the adder method of BooleanAlgebra class.
    Prints 'OK' if test passes, or the error if it fails.
    """
    # List of test cases: (a, b, expected_result)
    test_cases = [
        (0, 0, 0),
        (0, 2, 2),
        (5, 3, 8),
        (10, 5, 15),
        (100, 50, 150),
        (1, 1, 2),
        (7, 8, 15),
        (15, 15, 30),
    ]
    
    for a, b, expected in test_cases:
        result = BooleanAlgebra.adder(a, b)
        if result != expected:
            print(f"Error: adder({a}, {b}) = {result}, expected {expected}")
            return
    print("All adder tests OK!")

def test_multiplier():

    test_cases = [
        (0, 0, 0),
        (2, 0, 0),
        (5, 3, 15),
        (10, 5, 50),
        (2, 8, 16),
        (7, 7, 49),
        (15, 3, 45),
        (1, 100, 100),
    ]
    
    for a, b, expected in test_cases:
        result = BooleanAlgebra.multiplier(a, b)
        if result != expected:
            print(f"Error: multiplier({a}, {b}) = {result}, expected {expected}")
            return
    
    print("All multiplier tests OK!")

def test_gray_code():
    """
    Tests the gray_code conversion function with various inputs
    """
    # List of test cases: (input, expected_gray_code)
    test_cases = [
        (0, 0),   # 0 -> 0
        (1, 1),   # 1 -> 1
        (2, 3),   # 2 -> 3
        (3, 2),   # 3 -> 2
        (4, 6),   # 4 -> 6
        (5, 7),   # 5 -> 7
        (6, 5),   # 6 -> 5
        (7, 4),   # 7 -> 4
        (8, 12),  # 8 -> 12
    ]
    
    for input_num, expected in test_cases:
        result = BooleanAlgebra.gray_code(input_num)
        if result != expected:
            print(f"Error: gray_code({input_num}) = {result}, expected {expected}")
            print(f"Input binary: {bin(input_num)[2:].zfill(4)}")
            print(f"Result binary: {bin(result)[2:].zfill(4)}")
            print(f"Expected binary: {bin(expected)[2:].zfill(4)}")
            return
    
    print("All Gray code tests OK!")


if __name__ == "__main__":
    test_adder()
    test_multiplier()
    test_gray_code()