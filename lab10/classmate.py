"""contains Classmate class and its factory function

CPE202 Spring 2019
"""
class Classmate:
    """class for Classmate

    Attributes:
        last (str) : last name
        first (str) : first name
        major (str) : major
        year (str) : year 
    """
    def __init__(self, last, first, major, year):
        self.last = last
        self.first = first
        self.major = major
        self.year = year 

    def __repr__(self):
        return "Classmate{last: %s, first: %s, major: %s, year: %s}"\
            % (self.last, self.first, self.major, self.year)

    def __eq__(self, other):
        return isinstance(other, Classmate)\
            and self.last == other.last\
            and self.first == other.first\
            and self.major == other.major\
            and self.year == other.year

def classmate_factory(tokens):
    """Create a Classmate object by parsing tokens

    Args:
        tokens (list) : a list of str
                        The second item contains the name but in last, first format.
    Returns:
        Classmate : a Classmate object
    """
    name_parts = tokens[1].split(',')
    last = name_parts[0].strip()
    first = name_parts[1].strip()
    major = tokens[2]
    year = tokens[3].strip('\n')
    return Classmate(last, first, major, year)
