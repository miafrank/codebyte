# https://www.hackerrank.com/challenges/word-order/problem
# https://docs.python.org/2/library/itertools.html#itertools.permutations

num_words = input()
word_list = [input() for nums in range(1, int(num_words) + 1)]

word_dict = {}
final_count = []
for word in word_list:
    if word not in word_dict.keys():
        word_dict[word] = 1
    else:
        word_dict[word] += 1

final_count = [str(word) for word in list(word_dict.values())]

end = ' '.join(final_count)
print(len(word_dict))
print(end)


