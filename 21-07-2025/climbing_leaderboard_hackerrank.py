def climbingLeaderboard(ranked, player):
    scores = sorted(list(set(ranked)), reverse=True)
    result = []
    index = len(scores) - 1
    for score in player:
        while index >= 0 and score >= scores[index]:
            index -= 1
        result.append(index + 2)
    return result
