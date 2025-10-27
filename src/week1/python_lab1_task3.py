"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""


def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # Calculate character count
    char_count = len(text)

    # Calculate word count
    words = text.split()
    word_count = len(words)

    # Check for 'Python' (case-insensitive)
    has_python = "python" in text.lower()

    return (char_count, word_count, has_python)


if __name__ == "__main__":
    # Get input from user
    sentence = input("Enter a sentence: ")

    # Analyze the sentence
    length, words, contains_python = analyze_sentence(sentence)

    # Print results
    print(f"\nAnalysis Results:")
    print(f"Character count: {length}")
    print(f"Word count: {words}")
    print(f"Contains 'Python': {contains_python}")
