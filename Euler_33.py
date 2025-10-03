# Problem 33
# Digit Cancelling Fractions

# Function to find the greatest common divisor (for reducing the fraction)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# To store the product of all curious fractions
top = 1
bottom = 1

# Try all 2-digit numerators and denominators
for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):  # fraction must be < 1
        # Convert to strings to check digits
        n_str = str(numerator)
        d_str = str(denominator)

        # Check for common digit (except zero)
        for digit in n_str:
            if digit != '0' and digit in d_str:
                # Remove the common digit
                new_n = n_str.replace(digit, '', 1)
                new_d = d_str.replace(digit, '', 1)

                # Make sure we still have digits left
                if new_n != '' and new_d != '0' and new_d != '':
                    # Convert to integers
                    new_n = int(new_n)
                    new_d = int(new_d)

                    # Check if the "fake" simplification is correct
                    if numerator * new_d == denominator * new_n:
                        top *= numerator
                        bottom *= denominator

# Reduce the final product
common = gcd(top, bottom)
print(bottom // common)