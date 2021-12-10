opening_brackets = '[({<'
closing_brackets = '])}>'
points = [2, 1, 3, 4]

def calc_score(closing_bracket):
    return points[closing_brackets.index(closing_bracket)]

def parse_line(line, bracket_stack):
    for bracket in line.strip():
        if bracket in opening_brackets:
            bracket_stack.append(bracket)
            continue
        if len(bracket_stack) == 0:
            return False
        opening_bracket = bracket_stack.pop()
        if opening_brackets.index(opening_bracket) != closing_brackets.index(bracket):
            return False
    return True

with open('input.txt') as input:
    scores = []
    for line in input.readlines():
        bracket_stack = []
        success = parse_line(line, bracket_stack)

        line_score = 0
        if success and len(bracket_stack) != 0:
            for unmatched_bracket in reversed(bracket_stack):
                line_score *= 5
                line_score += points[opening_brackets.index(unmatched_bracket)]
            scores.append(line_score)
    middle_score = sorted(scores)[len(scores) // 2]
    print(middle_score) # 3260812321
            