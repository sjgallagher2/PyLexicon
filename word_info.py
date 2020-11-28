#   Word information
#       Identification (main form, pronunciation, part of speech, status)
#       Etymology
#       Signification (senses)
#       Illustrative quotations

from categories import Category

class WordID:
    def __init__(self,main_form='',pronunc='',partofspeech='',status='active'):
        self.main_form=main_form
        self.pronunciation=pronunc
        self.partofspeech = partofspeech
        self.status = status

# idx should be the number for this sense, essentially the defn order
# comment is optional text to add to the defn describing usage etc
class WordSignification:
    def __init__(self,idx,defn,comment=''):
        self.idx = idx
        self.defn = defn
        self.comment=comment

class WordInformation:
    def __init__(self, word_id, word_etym=None, word_signifs=[], quotes=[]):
        self.word_identification = word_id
        self.word_etymology = word_etym
        self.word_significations = word_signifs
        self.word_quotes = quotes


