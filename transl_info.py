#   Translation information
#       Common translations
#       Idioms and phrases
#       Translation examples (context/category, time period, author, citation)

from categories import Category,TimePeriod

class TranslationInfo:
    def __init__(self):
        self.common_translations = []
        self.idioms_and_phrases = []
        self.translation_examples = []

class TranslationExample:
    def __init__(self,foreign,english,cat=Category.COMMON,time=TimePeriod.TWENTYFIRST,auth="",cite=""):
        self.category = cat
        self.foreign_language = foreign
        self.english_language = english
        self.time_period = time
        self.author = auth
        self.citation = cite

