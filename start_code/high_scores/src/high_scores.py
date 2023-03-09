def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse = True)[:3]


def high_to_low(scores):
    return sorted(scores, reverse = True)

# def tied_scores(scores):
#     return personal_top_three(scores)
    # if you've already got this function DON'T REPEAT IT
    
