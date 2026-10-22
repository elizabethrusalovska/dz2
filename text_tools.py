def count_words(text):
    """Рахує слова в тексті."""
    words = text.split()
    return len(words)


def count_vowels(text):
    """Рахує українські голосні літери."""
    vowels = "аеєиіїоуюя"
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1

    return count