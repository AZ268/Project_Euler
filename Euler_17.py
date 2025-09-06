# Problem 17
# Number Letter Counts
# If the numbers 1 to 5 to are written out in words: one, two, three, four, five, then there are
# 3+3+5+4+4=19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

def words_of_numbers(n):
    one_to_nine = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    if n == 1000:
        return "onethousand"

    words = ""

    hundreds = n // 100
    remainder = n % 100

    if hundreds:
        words += one_to_nine[hundreds] + "hundred"
        if remainder:
            words += "and"

    if remainder >= 20:
        words += tens[remainder // 10]
        words += one_to_nine[remainder % 10]
    elif remainder >= 10:
        words += teens[remainder - 10]
    else:
        words += one_to_nine[remainder]

    return words


total_letters = sum(len(words_of_numbers(i)) for i in range(1, 1001))
print(total_letters)