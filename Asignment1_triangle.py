def print_lower_triangle(n):
    print("\nLower Triangular Pattern:")
    for i in range(1, n + 1):
        print("* " * i)

def print_upper_triangle(n):
    print("\nUpper Triangular Pattern:")
    for i in range(n, 0, -1):
        print("* " * i)

def print_pyramid(n):
    print("\nPyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


def print_all_patterns():
    try:
        rows = int(input("Enter the number of rows: "))
        if rows <= 0:
            print("Please enter a positive integer.")
            return

        print_lower_triangle(rows)
        print_upper_triangle(rows)
        print_pyramid(rows)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


print_all_patterns()
