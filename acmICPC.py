from itertools import combinations

def acmTeam(topic):
    topic =  [[int(c) for c in s] for s in topic]
    teams = {}
    perms = list(combinations(range(len(topic)), 2))
    for perm in perms:
        result = [x|y for x,y in zip(topic[perm[0]],topic[perm[1]]) if x|y == 1]
        teams[perm] = result
    
    print(perms,"\n",topic,"\n", teams)
    return [len([c for c in teams.keys() if teams[c] == max(teams.values())]), len(max(teams.values()))]