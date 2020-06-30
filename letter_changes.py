# Have the function LetterChanges(str) take the str parameter being passed and modify
# it using the following algorithm.
# Replace every letter in the string with the letter following it in the
# alphabet (ie. c becomes d, z becomes a).
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

# Create dictionary with alphabet in it, and position in the alphabet
# Create list to check to see if final string is a vowel
import string
import pprint

# Create dictionary with {alpha: 0 based index}
alpha_dict = {k: v for k, v in enumerate(string.ascii_lowercase)}
vowels = ['a', 'e', 'i', 'o', 'u']


def get_key_from_value(val):
    for key, value in alpha_dict.items():
        if val == value:
            return key


def letter_changes(input_str):
    result = ""

    for val in input_str:
        if val == 'z':
            result += alpha_dict.get(0)
        elif val in alpha_dict.values() and val != 'z':
            key_for_val = get_key_from_value(val)
            result += alpha_dict.get(key_for_val + 1)
        else:
            result += val

    for res in result:
        if res in vowels:
            res_vowel = res.upper()
            result = result.replace(res, res_vowel)
    return result


sample_input_two = "hello*3"
output_two = letter_changes(sample_input_two)

sample_input = "fun times!"
output = letter_changes(sample_input)

assert output == "gvO Ujnft!"
assert output_two == "Ifmmp*3"