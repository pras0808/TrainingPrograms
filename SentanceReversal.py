def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

s = input("Enter sentence: ")
print(reverse_words(s))
