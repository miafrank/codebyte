# https://www.hackerrank.com/challenges/most-commons/problem
import collections

input_str = 'qwertyuiopasdfghjklzxcvbnm'


def top_three(str_input):
    result = {}
    for s in str_input:
        if s not in result:
            result[s] = 1
        else:
            result[s] += 1

    # sort by key
    counter = collections.Counter({key: result[key] for key in sorted(result.keys())})

    for k, v in counter.most_common(3):
        print(k, v)


top_three(input_str)
