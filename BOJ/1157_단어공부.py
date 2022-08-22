words = input().upper()
unique_word = list(set(words))

count_words = []

for i in unique_word:
    count = words.count(i)
    count_words.append(count)

if count_words.count(max(count_words)) > 1:
    print('?')
else:
    max_index = count_words.index(max(count_words))
    print(unique_word[max_index])