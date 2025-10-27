"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""


def count_characters(text):
    """Count non-space characters in a string."""
    return len([char for char in text if not char.isspace()])


def count_words(text):
    """Count number of words in a string."""
    return len(text.split())


def extract_numbers(text):
    """Return list of integers found in text."""
    numbers = []
    for word in text.split():
        try:
            numbers.append(int(word))
        except ValueError:
            continue
    return numbers


def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)

    # Calculate sum and average of numbers if any exist
    num_sum = sum(numbers) if numbers else 0
    num_avg = num_sum / len(numbers) if numbers else 0

    return {
        "characters": char_count,
        "words": word_count,
        "numbers": numbers,
        "sum": num_sum,
        "average": num_avg,
    }


if __name__ == "__main__":
    # Get input from user
    print("Enter a text to analyze (can include numbers):")
    user_text = input()

    # Analyze the text
    results = analyze_text(user_text)

    # Print formatted results
    print("\nAnalysis Results:")
    print(f"Non-space characters: {results['characters']}")
    print(f"Word count: {results['words']}")
    print(f"Numbers found: {results['numbers']}")
    print(f"Sum of numbers: {results['sum']}")
    print(
        f"Average of numbers: {results['average']:.2f}"
        if results["numbers"]
        else "Average of numbers: N/A"
    )
