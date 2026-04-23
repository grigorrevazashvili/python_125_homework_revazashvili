#Homework 5.6

def translate(sentence, dictionary):
    words= sentence.split()
    translated_words = []

    for word in words:
        lower_word = word.lower()
        if lower_word in dictionary:
            translated_words.append(dictionary[lower_word])
        else:
            translated_words.append(word)
    return " ".join(translated_words)

translations = {
    "hello": "hola",
    "world": "mundo",
    "good": "bueno",
    "morning": "mañana",
    "cat": "gato",
    "dog": "perro",
    "house": "casa",
    "friend": "amigo"

}

sentence = "hello friend good morning"
result = translate(sentence, translations)

print(result)

