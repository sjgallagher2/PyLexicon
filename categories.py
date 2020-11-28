# Categories and subcategories for words, translation examples, idioms

# I think this will be easier, and sufficient...
class Category:
    COMMON=0
    PHYSICS=1
    MATH=2

def get_category_name(c):
    if c == Category.COMMON:
        return "Common"
    if c == Category.PHYSICS: # Forgo the elif because it's not necessary
        return "Physics"
    if c == Category.MATH:
        return "Math"

class TimePeriod:
    SIXTEENTH=0
    SEVENTEENTH=1
    EIGHTEENTH=2
    NINETEENTH=3
    TWENTIETH=4
    TWENTYFIRST=5


# Old
# Categories can follow Dewey Decimal System, or the expanded Universal Decimal Classification (UDC), so only a
# number is required to be stored, and a single mapping to categories, subcategories, etc, to be used for user
# interfacing. UDC categories:
# 0     Science and Knowledge. Organization. Comp sci. Info science. Documentation. Librarianship. Institutions.
#       Publications.
# 1     Philosophy, Psychology
# 2     Religion, Theology
# 3     Social Sciences
# 4     [vacant]
# 5     Mathematics. Natural Sciences
# 6     Applied Sciences. Medicine, Technology
# 7     The Arts. Entertainment. Sport
# 8     Linguistics. Literature
# 9     Geography. History
# Most useful will be Pure science (500) so that will be fleshed out more. Other than that, Language can be used
# as a catch-all for conjunctions, common words, etc; sort of abusing the system but whatever
# This is hierarchical, so it's important to preserve hierarchy
