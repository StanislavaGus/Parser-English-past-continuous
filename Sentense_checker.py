import re
from Key_words import Key_words

class Sentense_checker:
    def __init__(self):
        self.tokens = []
        self.curr_index = 0
        self.curr_word = None
        self.key_words = Key_words

    def parse(self):
        if len(self.tokens) != 0 :
            try:
                self.level1()
            except Exception as e:
                print("Error:", str(e))

    def next_word(self):
        self.curr_index += 1
        if self.curr_index < len(self.tokens):
            self.curr_word = self.tokens[self.curr_index]
        else:
            raise Exception("End of token list...")

    def set_tokens(self, input_string):
        # Проверка на допустимые символы
        if len(input_string) == 0:
            print("Empty input is valid.")
            return

        if not (input_string[0].isupper()):
            print("The sentence must begin with a capital letter.")
            return

        if not re.match(r"^[a-zA-Z0-9-.,!? ]+$", input_string):
            print("Error: Input contains invalid characters.")
            self.tokens.clear()
            return

        input_string = input_string[0].lower() + input_string[1:]
        while(input_string[-1]==' '):
            input_string = input_string[:-1]

        while (input_string[0] == ' '):
            input_string = input_string[1:]

        last_symbol = input_string[len(input_string)-1]

        if re.match(r"[.!?]", last_symbol):
            input_string = input_string[:-1]  # удалить последний символ
        # Разбиваем строку на слова по символам пробела и запятой
        tokens = re.split(r'[,\s]+', input_string)
        tokens += last_symbol



        # Добавляем токен конца строки
        tokens.append('$')

        # Устанавливаем токены
        self.tokens = tokens

    def level1(self):
        self.curr_index = 0
        self.curr_word = self.tokens[0]
        if self.curr_word == '$':
            print("Empty input.")
            return
        self.sentense()
        if self.curr_word != '$':
            raise Exception("Sentences isn't correct...")
        else: print("Sentence is correct!")


    # уровень 6
    #"<sentence>": ["<affirmative sentence>", "<negative sentence>", "<interrogative sentence>"],  # 6
    def sentense(self):
        start_position = self.curr_index
        self.affirmative_sentencee_lev_5()

        if start_position == self.curr_index:
            self.negative_sentencee_lev_4()

        if start_position == self.curr_index:
            self.interrogative_sentencee_lev_4()


    # уровень 5
    #"<affirmative sentence>": ["<base> <complement> <punctuation>"],  # 5
    def affirmative_sentencee_lev_5(self):
        start_position = self.curr_index
        self.base_lev_4()

        if not start_position == self.curr_index:
            self.complement_lev_4()
            self.punctuation_lev_2()
        else:
            return
            #raise Exception("Error in affirmative_sentencee_lev_4 with word " + self.curr_word)

            #raise Exception("Error in affirmative_sentencee_lev_4 with word " + self.curr_word)



    # уровень 4
    #"<negative sentence>": [
     #   "<subject for was> was not <verb in Ving> <complement> <punctuation>",
      #  "<subject for were> were not <verb in Ving> <complement> <punctuation>"]
    def negative_sentencee_lev_4(self):
        start_position = self.curr_index
        many_flag = 2 # 0-was 1-were 2-None

        self.subject_for_was_lev_2()
        if self.curr_index != start_position:
            many_flag = 0
            if self.curr_word == "was":
                self.next_word()
            else:
                return
                #raise Exception("Error in negative_sentense_lev_4 with word " + self.curr_word + " insted of was")

        else:
            self.subject_for_were_lev_2()
            if self.curr_index != start_position:
                many_flag = 1
                if self.curr_word == "were":
                    self.next_word()
                else:
                    return
                    #raise Exception("Error in negative_sentense_lev_4 with word " + self.curr_word + " insted of were")

        if many_flag == 2:
            self.curr_index = start_position
            self.curr_word = self.tokens[self.curr_index]
            return

        if self.curr_word == "not":
            self.next_word()
            before_index = self.curr_index
            self.verb_in_Ving_lev_2()

        if not before_index == self.curr_index:
            self.complement_lev_4()
            self.punctuation_lev_2()

            return
            #raise Exception("Error in negative_sentense_lev_4 with word " + self.curr_word)

    #"<interrogative sentence>": [
     #   "was <subject for was> <verb in Ving> <complement> <question mark>",
      #  "were <subject for were> <verb in Ving> <complement> <question mark>"],  # 4
    def interrogative_sentencee_lev_4(self):
        start_position = self.curr_index
        many_flag = 2 # 0-was 1-were 2-None

        if self.curr_word == "was":
            many_flag = 0
            self.next_word()

        elif self.curr_word == "were":
            many_flag = 1
            self.next_word()

        else:
            return
            #raise Exception("Error in interrogative_sentense_lev_4 with word " + self.curr_word + " insted of was/were")

        start_position = self.curr_index

        if many_flag == 0:
            self.subject_for_was_lev_2()
            if self.curr_word == start_position:
                return
                #raise Exception("Error in interrogative_sentense_lev_4 with word " + self.curr_word)

        elif many_flag == 1:
            self.subject_for_were_lev_2()
            if self.curr_word == start_position:
                return
                #raise Exception("Error in interrogative_sentense_lev_4 with word " + self.curr_word)

        before_index = self.curr_index
        if not many_flag == 2:
            self.verb_in_Ving_lev_2()
        else:
            self.curr_index = start_position
            self.curr_word = self.tokens[self.curr_index]
            return

        if not before_index == self.curr_index:
            self.complement_lev_4()
            self.question_mark_lev_1()
        return

    #"<base>": [
    #    "<subject for was> was <verb in Ving>",
    #    "<subject for were> were <verb in Ving>"],  # 4
    def base_lev_4(self):
        start_position = self.curr_index
        many_flag = 2 # 0-was 1-were 2-None

        self.subject_for_was_lev_2()
        if self.curr_index != start_position:
            many_flag = 0
            if self.curr_word == "was":
                self.next_word()
            else:
                return

        else:
            self.subject_for_were_lev_2()
            if self.curr_index != start_position:
                many_flag = 1
                if self.curr_word == "were":
                    self.next_word()
                else:
                    return

        position_before = self.curr_index
        if not many_flag == 2:
            self.verb_in_Ving_lev_2()

        if self.curr_index == position_before+1:
            return
        else:
            self.curr_index = start_position
            self.curr_word = self.tokens[self.curr_index]
            return

    def complement_lev_4(self):
        start_position = self.curr_index

        # "<prepositional phrase of place>"
        self.prepositional_phrase_of_place_lev_2()

        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<object>"
        self.object_lev_2()
        self.next_word()
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<adverb>"
        self.adverb_lev_1()
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<prepositional phrase of time>"
        self.prepositional_phrase_of_time_lev_3()
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        #"<object> <prepositional phrase of place>"
        self.object_lev_2()
        self.prepositional_phrase_of_place_lev_2() #2
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        #"<adverb> <prepositional phrase of place>"
        self.adverb_lev_1()
        self.prepositional_phrase_of_place_lev_2()#2
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        #"<object> <prepositional phrase of time>"
        self.object_lev_2()
        self.prepositional_phrase_of_time_lev_3()
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        #"<adverb> <prepositional phrase of time>"
        self.adverb_lev_1()
        self.prepositional_phrase_of_time_lev_3()
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<object> <adverb>"
        self.object_lev_2()
        self.adverb_lev_1()
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<adverb> <prepositional phrase of place>"
        self.adverb_lev_1()
        self.prepositional_phrase_of_place_lev_2()#3
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<prepositional phrase of time> <prepositional phrase of place>"
        self.prepositional_phrase_of_time_lev_3()
        self.prepositional_phrase_of_place_lev_2()#3
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<object> <prepositional phrase of time> <prepositional phrase of place>"
        self.object_lev_2()
        self.prepositional_phrase_of_time_lev_3()
        self.prepositional_phrase_of_place_lev_2()#3
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<adverb> <prepositional phrase of time> <prepositional phrase of place>"
        self.adverb_lev_1()
        self.prepositional_phrase_of_time_lev_3()
        self.prepositional_phrase_of_place_lev_2()#3
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<object> <adverb> <prepositional phrase of time>"
        self.object_lev_2()
        self.adverb_lev_1()
        self.prepositional_phrase_of_time_lev_3()
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<object> <adverb> <prepositional phrase of place>"
        self.object_lev_2()
        self.adverb_lev_1()
        self.prepositional_phrase_of_place_lev_2()#3
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<object> <prepositional phrase of time> <adverb>"
        self.object_lev_2()
        self.prepositional_phrase_of_time_lev_3()#2
        self.adverb_lev_1()
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # "<object> <prepositional phrase of place> <adverb>",
        self.object_lev_2()
        self.prepositional_phrase_of_place_lev_2()#3
        self.adverb_lev_1()
        if re.match(r"[.!?]", self.curr_word):
            return
        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]

        # ""
        return

    # уровень 3
    def prepositional_phrase_of_time_lev_3(self):
        start_position = self.curr_index
        self.preposition_time_lev_1()

        before_position = self.curr_index
        if not self.curr_index == start_position:
            self.duration_lev_2()
        else:
            self.curr_index = start_position
            self.curr_word = self.tokens[self.curr_index]
            return


        if not self.curr_index == before_position:
            return
        else:
            self.curr_index = start_position
            self.curr_word = self.tokens[self.curr_index]
            return

            #raise Exception("Error in prepositional_phrase_of_time_lev_3 with word " + self.curr_word)


    #уровень 2
    def subject_for_was_lev_2(self):
        if ((self.curr_word not in self.key_words.subject_for_was) and (self.curr_word not in self.key_words.singular_noun)):
            return
            #raise Exception("Error in subject_for_was_lev_2 with word " + self.curr_word)
        self.next_word()

    def subject_for_were_lev_2(self):
        if ((self.curr_word not in self.key_words.subject_for_were) and (self.curr_word not in self.key_words.plural_noun)):
            return
            #raise Exception("Error in subject_for_were_lev_2 with word " + self.curr_word)
        self.next_word()

    def verb_in_Ving_lev_2(self):
        for i in self.key_words.verb:
            if (self.curr_word == (i + "ing")):
                self.next_word()
                return
        #raise Exception("Error in verb_in_Ving_lev_2 with word " + self.curr_word)

    #"<prepositional phrase of place>": ["<preposition place> <article> <place>", "<preposition place> <place>"],
    def prepositional_phrase_of_place_lev_2(self):
        start_position = self.curr_index
        finish_position = self.curr_index + 3
        self.preposition_place_lev_1()
        if (start_position + 1) == self.curr_index:
            self.article_lev_1()

        if start_position + 2 == self.curr_index:
            self.place_lev_1()

        if self.curr_index == finish_position:
            return

        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]
        finish_position = self.curr_index + 2
        self.preposition_place_lev_1()
        self.place_lev_1()

        if self.curr_index == finish_position:
            return
        else:
            self.curr_index=start_position
            #raise Exception("Error in prepositional_phrase_of_place_lev_2 with word " + self.curr_word)


    def duration_lev_2(self):
        start_position = self.curr_index

        finish_position = self.curr_index + 1
        self.measurement_unit_lev_1()

        if finish_position == self.curr_index:
            return

        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]
        finish_position = self.curr_index + 2
        self.length_lev_1()
        self.measurement_unit_lev_1()

    def object_lev_2(self):
        finish_position = self.curr_index + 3
        self.article_lev_1()
        self.noun_lev_1()

    def punctuation_lev_2(self):
        start_position = self.curr_index

        finish_position = self.curr_index + 1
        self.period_lev_1()

        if finish_position == self.curr_index:
            return

        self.curr_index = start_position
        self.curr_word = self.tokens[self.curr_index]
        finish_position = self.curr_index + 1
        self.exclamation_mark_lev_1()

    #уровень 1
    def preposition_place_lev_1(self):
        if self.curr_word not in self.key_words.preposition_place:
            return
            #raise Exception("Error in preposition_place_lev_1 with word " + self.curr_word)
        self.next_word()

    def place_lev_1(self):
        if self.curr_word not in self.key_words.place:
            return
            #raise Exception("Error in place_lev_1 with word " + self.curr_word)
        self.next_word()

    def preposition_time_lev_1(self):
        if self.curr_word not in self.key_words.preposition_time:
            return
            #raise Exception("Error in place_lev_1 with word " + self.curr_word)
        self.next_word()

    def verb_lev_1(self):
        if self.curr_word not in self.key_words.verb:
            return
            #raise Exception("Error in verb_lev_1 with word " + self.curr_word)
        self.next_word()

    def noun_lev_1(self):
        if self.curr_word not in self.key_words.noun:
            return
            #raise Exception("Error in noun_lev_1 with word " + self.curr_word)
        self.next_word()

    def article_lev_1(self):
        if self.curr_word not in self.key_words.article:
            return
            #raise Exception("Error in article_lev_1 with word " + self.curr_word)
        self.next_word()

    def adverb_lev_1(self):
        if self.curr_word not in self.key_words.adverb:
            return
            #raise Exception("Error in adverb_lev_1 with word " + self.curr_word)
        self.next_word()

    def singular_noun_lev_1(self):
        if self.curr_word not in self.key_words.singular_noun:
            return
            #raise Exception("Error in singular_noun_lev_1 with word " + self.curr_word)
        self.next_word()

    def plural_noun_lev_1(self):
        if self.curr_word not in self.key_words.plural_noun:
            return
            #raise Exception("Error in plural_noun_lev_1 with word " + self.curr_word)
        self.next_word()

    def question_mark_lev_1(self):
        if self.curr_word not in self.key_words.question_mark:
            return
            #raise Exception("Error in question_mark_lev_1 with word " + self.curr_word)
        self.next_word()

    def period_lev_1(self):
        if self.curr_word not in self.key_words.period:
            return
            #raise Exception("Error in period_lev_1 with word " + self.curr_word)
        self.next_word()

    def exclamation_mark_lev_1(self):
        if self.curr_word not in self.key_words.exclamation_mark:
            return
            #raise Exception("Error in exclamation_mark_lev_1 with word " + self.curr_word)
        self.next_word()

    def measurement_unit_lev_1(self):
        if self.curr_word not in self.key_words.measurement_unit:
            return
            #raise Exception("Error in measurement_unit_lev_1 with word " + self.curr_word)
        self.next_word()

    def length_lev_1(self):
        if self.curr_word not in self.key_words.length:
            return
            #raise Exception("Error in length_lev_1 with word " + self.curr_word)
        self.next_word()

















