def delta(a, b, c):
    print(f"Function: {a}x^2 + {b}x + {c}")
    return (b ** 2) - (4 * a * c)

def baskhara(a, b, c):
    d = delta(a, b, c)  # Adding delta to a variable
    if d < 0:
        return None # Preventing the calculation of complex roots

    deltasquareroot = d ** (1/2)
    root1 = (-b + deltasquareroot) / (2 * a)
    root2 = (-b - deltasquareroot) / (2 * a)
    return root1, root2

def main():
    try:
        a = float(input("Type a value for A: "))
        b = float(input("Type a value for B: "))
        c = float(input("Type a value for C: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    result = baskhara(a, b, c)
    if result is None:
        print("Delta is negative, no real roots.")
    else:
        root1, root2 = result
        print(f"First root is {root1:.2f}")
        print(f"Second root is {root2:.2f}")

if __name__ == "__main__":
    main()