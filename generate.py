import sys

# Usage: 'python generate.py x y', x is a set of comma separated
# characters and y is the length of the combination

default_set = ['session', 'cigar', 'grape', 'merry', 'useful', 'churn', 'fatal', 'thought', 'very', 'any', 'arm', 'unaware', 'clock', 'fresh', 'security', 'field', 'caution', 'effort', 'gorilla', 'speed', 'plastic', 'common', 'tomato', 'echo']
default_length = 12


# Returns the list of possible combinations
# with given set s and of length n
def generate(s, n):
    return generate_list(s, len(s), n)


# Recursive function that generates the
# list of possible combinations where
# s is the set of characters and n is
# the length of the combination
def generate_list(s, n, ending=''):

    if n == 0:
        return [ending]

    lst = []
    for i in range(len(s)):
        new_ending = ending + s[i]
        lst += generate_list(s, n-1, ending=new_ending)
    return lst


if __name__ == '__main__':

    c_set = []
    c_length = 0

    if len(sys.argv) == 3:
        c_set = sys.argv[1].split(',')
        c_length = sys.argv[2]
    else:
        c_set = default_set
        c_length = default_length

    for o in generate_list(c_set, int(c_length)):
        print(o)

