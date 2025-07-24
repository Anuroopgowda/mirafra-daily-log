def acmTeam(topic):
    max_topics = 0
    team_count = 0
    n = len(topic)
    for i in range(n):
        for j in range(i + 1, n):
            combined = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            if combined > max_topics:
                max_topics = combined
                team_count = 1
            elif combined == max_topics:
                team_count += 1
    return [max_topics, team_count]
