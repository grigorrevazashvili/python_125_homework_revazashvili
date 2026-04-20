#Homework 4 Task 4

def count_words(sentence):
    words = sentence.split()
    word_count = len(words)
    char_count = len(sentence.replace (" ", ""))
    longest_word = max(words, key=len)
    return word_count, char_count, longest_word

sentence = "the quick brown fox jumps over the lazy dog"

word_count, char_count, longest_word = count_words(sentence)

print("Number of words:", word_count)
print("Number of characters (excluding spaces):",char_count)
print("Longest word:", longest_word)
