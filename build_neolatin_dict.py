from categories import Category
from lexicon_entry import LexiconEntry,Lexicon
from transl_info import TranslationInfo,TranslationExample
from word_info import WordID,WordSignification,WordInformation
import re

# FORMAT EXAMPLES
# General symbols:
#   *   Modern word (after 1400 AD)
#   (*) Ancient word but first used in given meaning in modern times
#   +   Medieval word (700-1400 AD)
#   (+) Ancient word but first used in given meaning in Medieval times


#103 pink  roseus, a, um (EGGER R.A. 73: "columnae ... e lapid granite ravi roseique coloris."  >> subruber, bra, brum (ERASMUS Coll. 199, of rosé wine; Pharm. Austr. 424)
#{index} {english}  {latin definition} ({example citation}: "{example}"  >> {latin word} ({source})

#103 pastel  >>
#{index} {english} >>

#092 conjecture (editorial)  coniectûra, ae f. (Septuagint, "Praef.": "satius est visum locos vel aliquo modo suspectos ... relinqui quam eos ex alicuius ingenio aut coniecturâ emendari")
#{index} {english}  {latin} ({example cit},"{cit}": "{example}")

#092 edition  (version of a book, consisting of a set of copies published together)  \\ êditio, ônis f.  \ QUINT. 5, 11, 40, of the varying ancient editions of Homer: "Megarios ab Atheniensibus .. victos Homeri versu, qui tamen ipse non in omni editione reperitur."  \ HIER. Ep. 112, 19: "ex Theodotionis editione."  \ 1569 MERCURIALE 22, in a second edition: "in primâ editione."  \ Septuagint praef., of the Sixtine edition of the Septuagint: "nova haec editio."  |  (a text, esp. of a classical work, established by a particular editor in accordance with principles of textual criticism)  \\ recensio, ônis f.  \
#{index} {english}  ({disambiguation})  \\ {latin} \ {example citation}: "{example}"  \ {repeat}  | ({disambiguation})  \\ {latin}  \

#07 publish  >> êdere  >> in lucem êdere  PP 1891 VELENOVSKÝ i.  >> divulgare  >> evulgare  PP 1794 RUIZ v.  >> publici iuris facere  PP 1784 THUNBERG xxvi.  >> foras dare  PP HASE v. |  be published  >> prodîre in lucem  >> prodîre  PP 1652 TURS. 356. 1794 RUIZ iv.  |  send to the publisher, have published  >> typis mandare  PP 1652 TURS. 301.
#07 parts: table (in book), chart  tabula, ae f. 1843 TRAPPEN 41; Pharm. Austr. xx)  >> tabella, ae f. 1843 TRAPPEN 40)  >> conspectus, ûs m. 1843 TRAPPEN 45)
#/9 name: what is your name?  qui vocaris? quod tibi nomen est?
#/21 veterinary  >> veterinârius, a, um  PP Col.  1826 LÜDERS 14.
#/21    ANIMAL MATTERS
#//41 Tunisia  Tûnêsia, ae f. (EGGER S.L. 51)  |  adj.  Tûnêsiensis, e (EGGER S.L. 51)  >>>> Tûnêtânum regnum (1698 Hofmann; 1652 TURS. 253; 1798 DESFONTAINES i)  >> ager Tunetanus (1798 DESFONTAINES title page)
#// /general city: King's Mountain, Königsberg, Monterrey, Montréal  >> Regi(o)montium, i n.


# We're interested in the range 4271 : 4423 which includes:
#   'MATH': 4271
#   'GEOMETRY': 4324
#   'MEASURE': 4341
#   'SCIENCE': 4376
#   'PHYSICS': 4396

lines = []
with open('neolatin_dict.txt','r') as f:
    lines = f.readlines()
    lines = lines[4271:4340]
    lines = [l.strip() for l in lines]

# Return dictionary with {section name : first line}
def get_section_titles(lines):
    title_lines = []
    title_line_idx = []
    for i in range(len(lines)):
        if '    ' in lines[i] and '     ' not in lines[i] and '>>' not in lines[i] and '*' not in lines[i] and '(' not in lines[i]:
            title_lines.append(lines[i])
            title_line_idx.append(i)
    titles = [t[t.find('    ')+4:].strip() for t in title_lines]

    i = 0
    while i < len(titles):
        if titles[i] == '' or len(titles[i]) > 100:
            titles = titles[0:i] + titles[i+1:]
            title_line_idx = title_line_idx[0:i] + title_line_idx[i+1:]
        i += 1
    out_dict = {}
    for i in range(len(titles)):
        out_dict[titles[i]] = title_line_idx[i]
    return out_dict

tdic = get_section_titles(lines)
title_idx = list(tdic.values()) # line numbers for titles

# Get rid of title lines (without changing length as we go)
lines_t = []
for i in range(len(lines)):
    if i not in title_idx and not lines[i].isnumeric():
        lines_t.append(lines[i])
        
lines = lines_t
lines_t = []
    
for i in range(len(lines)):
    lines[i] = lines[i].strip('0123456789 ') # Strip leading numbers and spaces
    lines[i] = lines[i].split('  ') # Separate by double spaces (which seem to be a reliable separator)

transls = []
exs = []
for l in lines:
    if len(l) > 1:
        t = l[1] # This will store our translation
        if t.find('(') != -1:
            transls.append( t[:t.find('(')] )
            if t.find(')') != -1:
                exs.append(t[t.find('(')+1 : t.find(')')])
            else:
                exs.append('')
        else:
            transls.append('')
            exs.append('')
    else:
        transls.append('')
        exs.append('')


# BUILD THE LEXICON
lex = Lexicon('NeoLatin Math','Collection of neo-Latin math terms')

for i in range(len(lines)):
    l = lines[i]
    w_info = WordInformation(WordID(l[0]))
    t_info = TranslationInfo()
    t_info.common_translations.append(transls[i])
    t_info.translation_examples.append(exs[i])
    lex_e = LexiconEntry(w_info,t_info,Category.MATH)
    lex.add_entry(lex_e)




