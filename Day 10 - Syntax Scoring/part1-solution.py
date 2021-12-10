opening_brackets = '[({<'
closing_brackets = '])}>'
points = [57, 3, 1197, 25137]

def calc_score(closing_bracket):
    return points[closing_brackets.index(closing_bracket)]

with open('input.txt') as input:
    syntax_score = 0
    for line in input.readlines():
        bracket_stack = []
        for bracket in line.strip():
            if bracket in opening_brackets:
                bracket_stack.append(bracket)
                continue
            if len(bracket_stack) == 0:
                syntax_score += calc_score(bracket)
                break
            
            opening_bracket = bracket_stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(bracket):
                syntax_score += calc_score(bracket)
                break
    print(syntax_score) # 240123
            