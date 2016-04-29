import re

def read_away_parenthesized(inputstring):
    just_started = True
    counter = 0
    result = ""
    for i in range(len(inputstring)):
        c = inputstring[i]
        if c == '(':
            counter+=1
        elif c == ')':
            counter-=1
        result += c
        if counter > 0 and just_started == True:
            just_started = False
        if counter == 0 and not just_started:
            return result, inputstring[i+1:]


def starts_with(keyword, string):
    return any([re.search(r"^\s*" + word + "\s+.*", string) for word in list(keyword)])


