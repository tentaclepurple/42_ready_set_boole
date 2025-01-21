def adder_rec(a, b):

    if not b:
        return a
    
    no_carry = a ^ b
    carry = (a & b) << 1
    a = no_carry
    b = carry

    return adder_rec(a, b)
      


if __name__ == "__main__":
      print(adder_rec(2, 3))