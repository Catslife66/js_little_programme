import random


letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]
punctuations = ['.', '?', '!']

max_letter_length = 8
min_letter_length = 1
max_word_length = 15
min_word_length = 2
max_sentence_length = 5
min_sentence_length = 2


def make_sentence():
    words = []
    single_word = ''
    sentence = []
    single_sentence = ''
    sentence_length = random.randint(min_word_length, max_word_length)
    for i in range(sentence_length):
        word = random.choices(letters, k=random.randint(min_letter_length, max_letter_length))
        words.append(word)
    for w in words:
        single_word = ''.join(w)
        sentence.append(single_word)

    if len(sentence) > 10:
        sentence[len(sentence)//2] += ','
    for i in sentence:
        single_sentence += i + ' '

    single_sentence = single_sentence.capitalize()
    single_sentence = single_sentence.rstrip()
    single_sentence += random.choice(punctuations)
    return single_sentence

def generate_random_text():
    paragraph = ''
    paragraph_length = random.randint(min_sentence_length, max_sentence_length)
    for i in range(paragraph_length):
        sentence = make_sentence()
        paragraph += sentence + ' '
    paragraph = paragraph.rstrip()
    print(paragraph)

generate_random_text()