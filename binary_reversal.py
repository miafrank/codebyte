# https://www.w3resource.com/w3r_images/python-math-image-exercise-31.svg


# def find_dec_value(bin_num):
#     i_bin_formatted = '{0:08b}'.format(int(bin_num))
#
#     while len(i_bin_formatted) % 8 != 0:
#         i_bin_formatted = '0' + i_bin_formatted
#     return int(i_bin_formatted[::-1], 2)
#
#
# print(find_dec_value(input()))


def BinaryReversal(string):
    padded_binary = '{0:08b}'.format(int(string))

    while len(padded_binary) % 8 != 0:
        padded_binary = '0' + padded_binary

    return int(padded_binary[::-1], 2)

print(BinaryReversal(input()))