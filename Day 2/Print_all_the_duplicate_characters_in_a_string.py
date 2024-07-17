from collections import Counter

def print_duplicate_characters(s):
    # Count occurrences of each character
    char_counts = Counter(s)
    
    # Filter and sort characters that appear more than once
    duplicates = sorted([(char, count) for char, count in char_counts.items() if count > 1])
    
    # Print the results
    if duplicates:
        for char, count in duplicates:
            print(f"{char}, count = {count}")
    else:
        print("No duplicate characters found.")

# Example usage
S = "geeksforgeeks"
print_duplicate_characters(S)
