# # Задача 1
text = 'Test, word1, word2, test. Word2, word3'
words = text.lower().replace(',', '').replace('.', '').split()
counting = {}

for word in words:
    counting[word] = counting.get(word, 0) + 1
print('Задача 1: ', counting)

# Задача 2
text = 'Test, word1, word2, test. Word2, word3'
words = text.lower().replace(',', '').replace('.', '').split()
counting_words = {}
for word in words:
    counting_words[word] = counting_words.get(word, []) + [1]
print('Задача 2: ', counting_words)

# Задача 3
counting_len = {key: len(val) for key, val in counting_words.items()}
print('Задача 3: ', counting_len)

# Задача 4
word_list = []
for word, count in counting.items():
    word_list.extend([word] * count)
str_words = ' '.join(word_list)
print('Задача 4: ', str_words)

# Задача 5
set_words = set(str_words.split())
print('Задача 5: ', set_words)