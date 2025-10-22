# Problem 42
# Coded Triangle Numbers

# --- The word list from p042_words.txt ---
WORDS_TEXT = (
    '"A","ABILITY","ABLE","ABOUT","ABOVE","ABSENCE","ABSOLUTELY","ACADEMIC",'
    '"ACCEPT","ACCESS","ACCIDENT","ACCOMPANY","ACCORDING","ACCOUNT","ACHIEVE",'
    '"ACID","ACROSS","ACT","ACTION","ACTIVE","ACTIVITY","ACTUAL","ACTUALLY",'
    '"ADD","ADDITION","ADDITIONAL","ADDRESS","ADMINISTRATION","ADMIT","ADOPT",'
    '"ADULT","ADVANCE","ADVANTAGE","ADVICE","ADVISE","AFFAIR","AFFECT","AFFORD",'
    '"AFRAID","AFTER","AFTERNOON","AGAIN","AGAINST","AGE","AGENCY","AGENT",'
    '"AGO","AGREE","AGREEMENT","AHEAD","AID","AIM","AIR","AIRCRAFT","ALL","ALLOW"'
    ')'
)

# --- Parse the words into a list ---
def parse_words(text):
    words = []
    word = ''
    inside_quotes = False
    for char in text:
        if char == '"':
            if inside_quotes:
                words.append(word)
                word = ''
            inside_quotes = not inside_quotes
        elif inside_quotes:
            word += char
    return words

# --- Get alphabetical value of a word ---
def word_value(word):
    total = 0
    for char in word:
        # ord('A') is 65, so A=1, B=2, ..., Z=26
        value = ord(char) - 64
        total += value
    return total

# --- Generate triangle numbers up to a limit ---
def generate_triangle_numbers(limit):
    numbers = []
    n = 1
    while True:
        t = n * (n + 1) // 2
        if t > limit:
            break
        numbers.append(t)
        n += 1
    return numbers

# --- Count how many words are triangle words ---
def count_triangle_words():
    words = parse_words(WORDS_TEXT)

    # Find the max word value possible to know how many triangle numbers we need
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    max_possible_value = max_len * 26  # Max value if all letters were 'Z'

    triangle_numbers = generate_triangle_numbers(max_possible_value)

    # Use dictionary for fast lookup (instead of set)
    triangle_lookup = {}
    for t in triangle_numbers:
        triangle_lookup[t] = True

    count = 0
    for word in words:
        val = word_value(word)
        if val in triangle_lookup:
            count += 1

    return count

# --- Run the solution ---
print("Number of triangle words:", count_triangle_words())
