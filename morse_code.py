# http://rubyquiz.com/quiz121.html
def get_morse_dict():
    return {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..'
    }


def main(name):
    result = ""
    translation = get_morse_dict()

    for i in range(len(name)):
        if name[i].upper() in translation:
            result += translation[name[i].upper()]
        if i + 1 != len(name):
            result += "|"
    return result


if __name__ == '__main__':
    sofia_morse = main('Sofia')
    eugenia_morse = main('Eugenia')
    none_morse = main('')
    assert not none_morse
    assert sofia_morse == '...|---|..-.|..|.-'
    assert eugenia_morse == '.|..-|--.|.|-.|..|.-'
