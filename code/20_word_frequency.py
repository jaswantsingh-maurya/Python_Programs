def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(word_frequency(sentence))
