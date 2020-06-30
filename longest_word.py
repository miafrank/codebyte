import string


def longest_word(sen):
    for s in sen:
        if not s.isalnum():
            sen = sen.replace(s, "")
            print(sen)
    new_sen = list(filter(None, list(sen)))
    print(new_sen)

sample_input = "fun&!! time"
sent = "".join(e for e in sample_input if e.isalpha())
longest_word(sample_input)


test_list = ["", "GeeksforGeeks", "", "is", "best", ""]
test_list = list(filter(None, test_list))
print ("Modified list is : " + str(test_list))