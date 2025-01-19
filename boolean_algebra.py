class BooleanAlgebra:

    @staticmethod
    def adder(a: int, b: int) -> int:

        # While there's a carry to propagate
        while b != 0:
            # Sum without considering carry
            no_carry = a ^ b
            
            # Calculate carry
            carry = (a & b) << 1
            
            # Update values for next iteration
            a = no_carry
            b = carry
            
        return a
    
    @staticmethod
    def multiplier(a: int, b: int) -> int:

        result = 0
        
        # Process each bit of b
        while b != 0:
            # If current bit of b is 1, add a to result
            if b & 1:
                result = BooleanAlgebra.adder(result, a)
            
            # Shift a left for next position
            a = a << 1
            # Shift b right to check next bit
            b = b >> 1
            
        return result

    @staticmethod
    def gray_code(n: int) -> int:

        # First, get the number shifted right by one position
        shifted = n >> 1

        # Then XOR the original number with its shifted version
        # This creates a number where each bit is XORed with the bit to its left
        gray = n ^ shifted
        
        return gray
