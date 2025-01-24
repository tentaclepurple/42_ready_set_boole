def ft_map(x: int, y: int) -> float:
    """
    Maps a 2D point to a value in [0,1] using a Z-order curve approach.
    
    Args:
        x: x coordinate (0 to 65535)
        y: y coordinate (0 to 65535)
        
    Returns:
        A float between 0 and 1 representing the point
    """
    if not (0 <= x < 65536 and 0 <= y < 65536):
        raise ValueError("Coordinates must be between 0 and 2^16-1")
    
    # Interleave bits of x and y
    result = 0
    for i in range(16):
        result |= ((x & (1 << i)) << i) | ((y & (1 << i)) << (i + 1))
    
    # Normalize to [0,1]
    return result / (2**32)


def ft_reverse_map(n: float) -> tuple[int, int]:
    """
    Converts a value in [0,1] back to its original 2D coordinates.
    This is the inverse function of coordinates_to_float.
    
    Args:
        n: A float between 0 and 1 representing encoded coordinates
        
    Returns:
        tuple[int, int]: The original (x,y) coordinates
    """

    if not (0 <= n <= 1):
        raise ValueError("Input must be between 0 and 1")
        
    # Multiply by 2^32 to denormalize
    value = int(n * (2**32))
    
    # Extract x and y bits
    x = 0
    y = 0
    
    # Even bits are for x, odd bits are for y
    for i in range(16):
        # Extract bit for x (0,2,4,... positions)
        x |= ((value >> (i * 2)) & 1) << i
        
        # Extract bit for y (1,3,5,... positions)
        y |= ((value >> (i * 2 + 1)) & 1) << i
    
    return (x, y)