# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will
# contain 2 elements: the first element will represent a list of comma-separated numbers sorted in
# ascending order, the second element will represent a second list of comma-separated numbers
# (also sorted).

# Your goal is to return a comma-separated string containing the numbers that occur in
# elements of strArr in sorted order. If there is no intersection, return the string false.
import itertools

sample_input = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]

#  split each number in list into individual nums
input_ints = [sample_input[ints].split(', ') for ints in range(len(sample_input))]
# merged = list(itertools.chain(*input_ints))
#
# word_dict = {}
# for word in merged:
#     if word not in word_dict.keys():
#         word_dict[word] = 1
#     else:
#         word_dict[word] += 1
#
#
# def get_intersection(input_dict):
#     return [k for k, v in list(input_dict.items()) if v % 2 == 0]
#
#
# strArr = get_intersection(word_dict)
# print(','.join(strArr))

set_one = set(input_ints[0])
set_two = set(input_ints[1])

# Sort items in list
result = list(map(int, set_one.intersection(set_two)))
result.sort()
print(*result)

