import re
from random import shuffle

text = str(input())


def mix_letters_in_words(text_to_mix):

    x = text_to_mix.split(' ')
    mixed_text = []
    for i in range(len(x)):
        word_to_mix = x[i]
        if len(word_to_mix) > 2:
            last_letter = word_to_mix[-1]
            first_letter = word_to_mix[0]
            if not bool(re.match('r\w', last_letter)):
                last_letter = word_to_mix[-2]
                punctuation_mark = True
            elif bool(re.match('r\w', last_letter)):
                punctuation_mark = False
            if punctuation_mark:
                mixing_part_list = list(word_to_mix[1:-2])
            elif not punctuation_mark:
                mixing_part_list = list(word_to_mix[1:-1])
            shuffle(mixing_part_list)
            mixed_letters = ''.join(mixing_part_list)
            new_word = first_letter + mixed_letters + last_letter
            if punctuation_mark:
                new_word += x[i][-1]
            mixed_text.append(new_word)
        else:
            mixed_text.append(word_to_mix)

    mixed_text_str = ''
    for i in range(len(mixed_text)):
        mixed_text_str += mixed_text[i] + ' '
    print(mixed_text_str)


mix_letters_in_words(text)
