scores = [100, 0, 90, 30]
scores1 = [30, 30, 25, 100, 0, 40]
scores2 = [4, 20]
scores3 = [40]

def latest(scores):
    return scores[-1]
    


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort()
    return scores[-1:-4:-1]


def from_highest_to_lowest(scores):
    scores.sort()
    scores.reverse()
    return scores


def top_three_when_there_is_a_tie(scores1):
    for num in scores1:
        if num == num:
            scores1.sort()
        return scores1[-1:-4:-1]
    else: 
        return False

def top_three_when_there_are_less_than_three(scores2):
    if len(scores2) < 3:
        scores2.sort()
    return (scores2[-1:-3:-1])

def top_three_when_there_are_less_than_one(scores3):
    if len(scores3) < 1:
        scores3.sort()
    return (scores3)



