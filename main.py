from fraction import hsum
from primality import primality3, generate_random_prime

def main():
    while True:
        print("\nMake selection:\n")
        print("1. Problem 1 (Fractions)")
        print("2. Problem 2 (Primality Test)")
        print("3. Problem 3 (Generate Prime)")
        print("4. Quit")

        choice = input("Enter option: ")

        # handle hsum call
        if choice == "1":
            n = int(input("Enter a value for 'n': "))
            m = int(input("Enter a value for 'm': "))
            result = hsum(n, m)
            print(f"Result: The {m}-digit of H({n}) is {result}")

        elif choice == "2":
            n = int(input("Enter number to test: "))
            k = int(input("Enter confidence parameter k: "))
            result = primality3(n, k)
            print("Prime?" , result)

        elif choice == "3":
            nbits = int(input("Enter bit length for prime: "))
            k = int(input("Enter confidence parameter k: "))
            p = generate_random_prime(nbits, k)
            print("Random prime:", p)

        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
