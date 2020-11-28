# An entry includes:
#   Word information
#       Identification (main form, part of speech, status
#       Signification (senses)
#       Illustrative quotations
#   Word category (and subcategories)
#   Translation information
#       Common translations
#       Translated definitions
#       Idioms and phrases
#       Translation examples (context/category, time period, author, citation)

from categories import Category

class LexiconEntry:
    def __init__(self, word_info, transl_info, categ = Category.COMMON):
        self.word_info = word_info
        self.word_category = categ
        self.translation_info = transl_info


class Lexicon:
    def __init__(self,label='',desc=''):
        self.label=label
        self.desc=desc
        self.entries=[]
    def add_entry(self,entry):
        self.entries.append(entry)
    def print_lexicon(self):
        # This is separate from __str__ which should print object information
        print(self.label)
        print(self.desc+'\n')
        for e in self.entries:
            print(e.word_info.word_identification.main_form,end=' : ')
            if e.translation_info.common_translations:
                print(e.translation_info.common_translations[0])
            else:
                print()

