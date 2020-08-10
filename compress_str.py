# https://www.hackerrank.com/challenges/compress-the-string/problem
# sample input: 1222311
# sample output: (1, 1) (3, 2) (1, 3) (2, 1)
# where (count_n, n)


def compressed_str(input_str):
    # Create list of individual numbers
    str_list = list(input_str)
    count = 1
    result = []
    if len(str_list) == 1:
        result.append((int(count), int(str_list[0])))
    # Iterate through list of characters from 0 to len(list) - 1
    for i in range(len(str_list) - 1):
        # If index of current item in list is not equal to the length of the list
        if i != len(str_list):
            # If next string in list is the same number as current item/index, increase the count by 1
            if str_list[i] == str_list[i + 1]:
                count += 1
            # If next str in list not equal to current item -> add count and char to list and reset count
            if str_list[i] != str_list[i + 1]:
                result.append((int(count), int(str_list[i])))
                count = 1
                # Account for last character in list
            if int(i) + 1 == len(str_list) - 1:
                result.append((int(count), int(str_list[i + 1])))
    return result


final = compressed_str(input())
print(*final)
