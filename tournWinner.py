def tournWinner(competition, results):
    best_team = ""
    teamScores = {best_team: 0}
    homeOrAway = -1
    for i, result in enumerate(results):
        if result == 0:
            homeOrAway = 0
        else:
            homeOrAway = 1
        if competition[i][homeOrAway] in teamScores:
            teamScores[competition[i][homeOrAway]] += 3
        else:
            teamScores[competition[i][homeOrAway]] = 3
        if teamScores[competition[i][homeOrAway]] > teamScores[best_team]:
            best_team = competition[i][homeOrAway]
    return best_team

competition = [
    ["HTML", "CSS"],
    ["CSS", "Python"],
     ["Python", "Java"]
]
results = [0, 1, 0]

print(tournWinner(competition, results))