from boolean_evaluation import BooleanAST


def test_boolean_anytree():
    """Test the Boolean AST implementation with anytree"""
    
    test_cases = [
        # Simple AND: 1 AND 0
        "10&",
        
        # Complex formula: 1 AND (0 OR 1)
        "101|&",
        
        # More complex formula: (1 OR 0) AND (1 OR 1)
        "10|11|&"
    ]
    
    print("Testing Boolean Evaluation with anytree:")
    print("-" * 50)
    
    for i, formula in enumerate(test_cases):
        print(f"\nFormula: {formula}")
        print("Tree representation:")
        
        # Build and print the tree
        tree = BooleanAST.build_tree(formula)
        BooleanAST.print_tree(tree)
        
        # Evaluate the tree
        result = BooleanAST.evaluate_node(tree)
        print(f"Result: {result}")


if __name__ == "__main__":
    test_boolean_anytree()