from fraction import hsum

def main():
    while True:
        print("\nMake selection:\n")
        print("1. Problem 1 (Fractions)")
        print("2. Problem 2 (Primality)")
        print("3. Problem 5 (RSA)")
        print("4. Quit\n")

        choice = input("Enter option: ")

        #handle hsum call
        if choice == "1":
            n = int(input("Enter a value for 'n': "))
            m = int(input("Enter a value for 'm': "))
            result = hsum(n, m)
            print(f"\nResult:\nThe {m}-digit of H({n}) is {result}")
        elif choice == "2":
            print("Problem 2 not implemented yet")
        elif choice == "3":
            print("Problem 5 not implemented yet")
        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()