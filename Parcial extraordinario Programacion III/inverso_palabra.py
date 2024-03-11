def reverse_words(words: list) -> list:
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return reversed_words

sentence = ["Hola", "Mundo"]
reversed_sent = reverse_words(sentence)
print(reversed_sent)