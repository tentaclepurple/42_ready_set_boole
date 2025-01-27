from boolean_evaluation import BooleanAST


def test_boolean_anytree():
    """Test the Boolean AST implementation with anytree"""
    
    test_cases = [
        '11&0|',
        '10&1|',
        '11&1|',
        '11&1|1^',
        '01&1|1=',
        '01&1&1&',
        '0111&&&',
    ]
    
    print("Testing Boolean Evaluation with anytree:")
    print("-" * 50)
    
    for i, formula in enumerate(test_cases):
        print(f"\nFormula: {formula}")
        
        # Build and print the tree
        tree = BooleanAST.build_tree(formula)
        
        # Evaluate the tree
        result = BooleanAST.evaluate_node(tree)
        print(f"Result: {result}")


if __name__ == "__main__":
    test_boolean_anytree()