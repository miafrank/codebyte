# Print Yes if he can use the magazine to create an untraceable replica of his ransom note. Otherwise, print No.
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
mag = "two times three is not four"
note = "two times two is four"

mag_two = "give me one grand today night"
note_two = "give one grand today"

mag_three = "ive got a lovely bunch of coconuts"
note_three = "ive got some coconuts"

mag_four = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg"
note_four = "elo lxkvg bg mwz clm w"

def count_words_in_dict(input_str):
    input_list = input_str.split()
    result = {}
    for word in input_list:
        if word in result:
            curr_val = result.get(word)
            result[word] = curr_val + 1
        if word not in result:
            result[word] = 1
    return result


def all_the_same(elements):
    if not elements:
        return True
    res = [elements[0]] * len(elements) == elements
    return res


def get_diff_from_mag(note_dict, mag_dict):
    res = []
    for word, count in note_dict.items():
        if word in mag_dict:
            mag_val = mag_dict[word]
            note_val = note_dict[word]
            if note_val <= mag_val:
                res.append(True)
            else:
                res.append(False)
        else:
            res.append(False)

    if not all_the_same(res):
        return "No"
    else:
        return "Yes"


assert(get_diff_from_mag(count_words_in_dict(note), count_words_in_dict(mag))) == "No"
assert(get_diff_from_mag(count_words_in_dict(note_two), count_words_in_dict(mag_two))) == "Yes"
assert(get_diff_from_mag(count_words_in_dict(note_three), count_words_in_dict(mag_three))) == "No"
assert(get_diff_from_mag(count_words_in_dict(note_four), count_words_in_dict(mag_four))) == "Yes"
