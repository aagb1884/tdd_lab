def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse = True)[:3]



# Your task is to write methods that return the highest score 
# from the list, the last added score and the three highest scores.

# In this exercise, you're going to use and manipulate lists. 