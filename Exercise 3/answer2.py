sentences = input("Enter a sentence: ")


sentences = sentences.lower()

for char in '.,!?:;':
    sentences = sentences.replace(char, ' ')

words = sentences.split()


word_freq = {}


for word in words:

    if word in word_freq:
        word_freq[word] += 1

    else:
        word_freq[word] = 1


for word, count in word_freq.items():
    print(f"{word}: {count}")
