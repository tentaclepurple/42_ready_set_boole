from conjunction_normal_form import conjunctive_normal_form


def output_test(formula: str, result: str, expected: str):
    print(f"Testing: {formula}")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    print("✓ PASS" if result == expected else "✗ FAIL")
    print("-" * 60)



""" 
("AB&!") // A!B!|
("AB|!") // A!B!&
("AB|C&")) // AB|C&
("AB|C|D|") // ABCD|||
("AB&C&D&") // ABCD&&&
("AB&!C!|") // A!B!C!||
("AB|!C!&")// A!B!C!&&

"""

def test_cnf():

    # Basic negations

    # "AB&!" -> "A!B!|"
    # Simple De Morgan: NOT(A AND B) -> (NOT A) OR (NOT B)")
    output_test("AB&!", conjunctive_normal_form("AB&!"), "A!B!|")

    # "AB|!" -> "A!B!&"
    # Simple De Morgan: NOT(A OR B) -> (NOT A) AND (NOT B)
    output_test("AB|!", conjunctive_normal_form("AB|!"), "A!B!&")

    # Simple conjunctions and disjunctions

    # "AB|C&" -> "AB|C&"
    # Already in CNF: (A OR B) AND C
    output_test("AB|C&", conjunctive_normal_form("AB|C&"), "AB|C&")

    # "AB|C|D|" -> "ABCD|||"
    # Single OR clause: A OR B OR C OR D
    output_test("AB|C|D|", conjunctive_normal_form("AB|C|D|"), "ABCD|||")

    # "AB&C&D&" -> "ABCD&&&"
    # Single AND of literals: A AND B AND C AND D
    output_test("AB&C&D&", conjunctive_normal_form("AB&C&D&"), "ABCD&&&")

    # "AB|!C!&" -> "A!B!C!||"
    # NOT(A AND B) OR NOT(C)
    output_test("AB&!C!|", conjunctive_normal_form("AB&!C!|"), "A!B!C!||")

    # "AB&!C!&" -> "A!B!C!&&"
    output_test("AB|!C!&", conjunctive_normal_form("AB|!C!&"), "A!B!C!&&")



if __name__ == "__main__":
    test_cnf()
