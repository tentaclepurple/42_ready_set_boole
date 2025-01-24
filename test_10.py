from space_filling_curve import ft_map, ft_reverse_map


if __name__ == "__main__":

    try:
        x = 10
        y = 14

        float_value = ft_map(x, y)
        print(f"Coordinates ({x},{y}) mapped to: {float_value}")

        float_value = 5.494803190231323e-08
        x, y = ft_reverse_map(float_value)
        print(f"Float value {float_value} reverse mapped to: ({x},{y})")

    except Exception as e:
        print(f"An error occurred: {e}")