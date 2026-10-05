def count_vowels_consonants(text):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


if __name__ == "__main__":
    text = input("Enter a string: ")
    vowels, consonants = count_vowels_consonants(text)
    print(f"Vowels = {vowels}")
    print(f"Consonants = {consonants}")
