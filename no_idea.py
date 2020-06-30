# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.
# https://www.hackerrank.com/challenges/no-idea/problem
n_m = [3, 2]
array_n = [1, 5, 3]
A = [3, 1]
B = [5, 7]


def no_idea(arr, arr_a, arr_b):
    print(len(arr))
    arr_no_duplicates = list(set(arr))
    print(len(arr_no_duplicates))
    happiness_level_A = 0
    happiness_level_B = 0
    for num_a in arr_a:
        if num_a in arr_no_duplicates:
            happiness_level_A += 1
        else:
            happiness_level_A += 0

    for num_b in arr_b:
        if num_b in arr_no_duplicates:
            happiness_level_B -= 1
        else:
            happiness_level_B += 0
    print(happiness_level_A)
    print(happiness_level_B)
    return happiness_level_A + (happiness_level_B)


n_m_list = [int(''.join(item).strip()) for item in input().split()]
array_ints = [int(''.join(item).strip()) for item in input().split()]
A_list = [int(''.join(item).strip()) for item in input().split()]
B_list = [int(''.join(item).strip()) for item in input().split()]

print(no_idea(array_ints, A_list, B_list))
# todo does not work with larger sets -- figure out why
