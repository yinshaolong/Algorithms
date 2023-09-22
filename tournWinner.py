def tournWinner(competitions, results):
    best_team = ""
    teamScores = {best_team: 0}
    homeOrAway = -1
    for i, result in enumerate(results):
        homeOrAway = abs(result - 1)
        if competitions[i][homeOrAway] in teamScores:
            teamScores[competitions[i][homeOrAway]] += 3
        else:
            teamScores[competitions[i][homeOrAway]] = 3
        if teamScores[competitions[i][homeOrAway]] > teamScores[best_team]:
            best_team = competitions[i][homeOrAway]
    return best_team

competitions = [
    ["HTML", "CSS"],
    ["CSS", "Python"],
     ["Python", "Java"]
]
results = [0, 0, 1]


print(tournWinner(competitions, results))