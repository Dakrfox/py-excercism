def add_prefix_un(word):
   return f"un{word}"


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    joiner = " :: " + prefix
    return joiner.join(vocab_words)

def remove_suffix_ness(word):
    word =word[:-4]
    if word[-1:]=="i":
        word =word[:-1]+"y"
    return word
    


def adjective_to_verb(sentence, index):
 
    word = sentence.split()[index]

    if word[-1] == '.':
        word = word[:-1] + 'en'
    else:
        word = word + 'en'
    return word
