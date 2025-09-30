from fraction import hsum
from primality import primality3, generate_random_prime
from rsa import generate_rsa_keys, rsa_encrypt_decrypt_test

def main():
    while True:
        print("\nMake selection:\n")
        print("1. Problem 1 (Fractions)")
        print("2. Problem 2 (Primality Test)")
        print("3. Problem 5 (RSA Encrypt/Decrypt)")
        print("4. Quit")

        choice = input("Enter option: ")

        # handle hsum call
        if choice == "1":
            n = int(input("Enter n (sum 1/1 + 1/2 + ... + 1/n): "))
            m = int(input("Enter m (which decimal digit to find): "))
            result = hsum(n, m)
            print(f"Result: The {m}-digit of H({n}) is {result}")

        elif choice == "2":
            n = int(input("Enter number to test for primality: "))
            k = int(input("Enter confidence parameter k (higher = more accurate): "))
            result = primality3(n, k)
            print("Prime?" , result)

        elif choice == "3":
            M = int(input("Enter message M (integer, must be < N): "))
            n = int(input("Enter bit length for RSA primes (e.g. 8): "))
            k = int(input("Enter confidence parameter k (higher = more accurate): "))
            p, q, N, E, D = generate_rsa_keys(n, k)
            print(f"\nGenerated keys: p={p}, q={q}, N={N}, E={E}, D={D}")
            print()
            if M >= N:
                print(f"Error: Message M must be less than N ({N}).")
            else:
                rsa_encrypt_decrypt_test(M, N, E, D)

        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
