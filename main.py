import random
from Sentense_checker import Sentense_checker
from Key_words import Key_words

keywords = Key_words()
non_terminals = {
    "<sentence>": ["<affirmative sentence>", "<negative sentence>", "<interrogative sentence>"],#6

    "<affirmative sentence>": ["<base> <complement> <punctuation>"],#5

    "<negative sentence>": [
        "<subject for was> was not <verb in Ving> <complement> <punctuation>",
        "<subject for were> were not <verb in Ving> <complement> <punctuation>"
    ],#4
    "<interrogative sentence>": [
        "was <subject for was> <verb in Ving> <complement> <question mark>",
        "were <subject for were> <verb in Ving> <complement> <question mark>"
    ],#4

    "<base>": [
        "<subject for was> was <verb in Ving>",
        "<subject for were> were <verb in Ving>"
    ],#4


    "<complement>": [
        "<prepositional phrase of place>",
        "<object>",
        "<adverb>",
        "<prepositional phrase of time>",
        "<object> <prepositional phrase of place>",
        "<adverb> <prepositional phrase of place>",
        "<object> <prepositional phrase of time>",
        "<adverb> <prepositional phrase of time>",
        "<object> <adverb>",
        "<adverb> <prepositional phrase of place>",
        "<prepositional phrase of time> <prepositional phrase of place>",
        "<object> <prepositional phrase of time> <prepositional phrase of place>",
        "<adverb> <prepositional phrase of time> <prepositional phrase of place>",
        "<object> <adverb> <prepositional phrase of time>",
        "<object> <adverb> <prepositional phrase of place>",
        "<object> <prepositional phrase of time> <adverb>",
        "<object> <prepositional phrase of place> <adverb>",
        ""
    ], #4

    "<subject for was>": ["I", "he", "she", "it", "John", "<singular noun>"],#2
    "<subject for were>": ["you", "we", "they", "<plural noun>"],#2
    "<verb in Ving>": ["<verb>ing"],#2

    "<prepositional phrase of place>": ["<preposition place> <article> <place>","<preposition place> <place>"], #2

    "<preposition place>": ["in", "at", "on", "by", "with", "under", "near", "behind"], #1
    "<place>": ["park", "home", "street", "river", "tree", "lesson", "dinner", "meeting"], #1
    "<prepositional phrase of time>": ["<preposition time> <duration>"], #3
    "<preposition time>": ["for", "during", "before", "after"], #1
    "<duration>": ["<measurement unit>", "<length> <measurement unit>"], #2
    "<length>": ["3", "a", "a", "two", "several", "long", "short"], #1
    "<measurement unit>": ["weeks", "month", "year", "days", "hours", "time", "while"], #1

    "<object>": ["<article> <noun>"], #2

    "<verb>": ["go", "read", "sleep", "watch", "cook", "run", "walk"], #1
    "<noun>": ["book", "homework", "keys", "ball", "news", "project", "meeting"], #1
    "<article>": ["a", "the", "my"], #1
    "<adverb>": ["quickly", "slowly", "quietly", "loudly", "suddenly", "happily", "sadly", "angrily"], #1

    "<punctuation>": ["<period>", "<exclamation mark>"], #2

    "<singular noun>": ["mom", "dad", "bird", "cat","dog","person","friend","brother","sister"], #1
    "<plural noun>": ["family","birds", "cats","dogs","people","friends","brothers","sisters", "siblings", "neighbors"], #1

    "<question mark>": ["?"], #1
    "<period>": ["."], #1
    "<exclamation mark>": ["!"] #1
}
def generate_sentence(symbol):
    if symbol not in non_terminals:
        return symbol
    sub_rules = non_terminals[symbol]
    sub_rule = random.choice(sub_rules)
    if sub_rule == "":
        return ""
    tokens = []
    i = 0
    while i < len(sub_rule):
        if sub_rule[i] == '<':
            j = i
            while j < len(sub_rule) and sub_rule[j] != '>':
                j += 1
            if j < len(sub_rule):
                tokens.append(sub_rule[i:j+1])
                i = j + 1
            else:
                tokens.append(sub_rule[i:])
                break
        elif sub_rule[i].isspace():
            i += 1
        else:
            j = i
            while j < len(sub_rule) and not sub_rule[j].isspace() and sub_rule[j] != '<':
                j += 1
            tokens.append(sub_rule[i:j])
            i = j

    sentence = ' '.join(generate_sentence(token) for token in tokens if token).strip()
    sentence = sentence.replace(' .', '.').replace(' ?', '?').replace(' ,', ',').replace(' !', '!').replace(' ing', 'ing')
    return sentence

def generate_past_cont_sentence():
    sentence = generate_sentence("<sentence>")
    #sentence = re.sub(r'\s([.,?!])', r'\1', sentence)
    if sentence:
        sentence = sentence[0].upper() + sentence[1:]
    return sentence

while True:
    print("1 - generate sentence (English past continuous\n" +
          "2 - checking the string for grammar compliance\n" +
          "3 - exit")
    choice = input("Choose option: ")

    if choice == '1':
        # reset_and_usage()  # Сбросить использование <AND> перед генерацией нового предложения
        print(generate_past_cont_sentence())
        print("\n")
    elif choice == '2':
        user_input = input("Enter string: ")

        sent_checker = Sentense_checker()
        sent_checker.set_tokens(user_input) # Токенизация и подготовка токенов
        Sentense_checker.parse(sent_checker)  # Запуск разбора
        print("\n")
    elif choice == '3':
        print("See you soon!")
        break
    else:
        print("Incorrect input, try again.")
        print("\n")