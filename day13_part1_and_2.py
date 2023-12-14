import numpy as np

with open("day13_input.txt", "r") as file:
    data = file.read()
puzzles = [i.split('\n') for i in data.split('\n\n')]

for p in range(0 , len(puzzles)):
    for l in range(0, len(puzzles[p])):
        puzzles[p][l] = puzzles[p][l].replace('.', '0')
        puzzles[p][l] = puzzles[p][l].replace('#', '1')
        puzzles[p][l] = [int(x) for x in puzzles[p][l]]
    puzzles[p] = np.array(puzzles[p])

def findMirror(p, multiplier, part):
    value = 0
    for l in range(1, p.shape[0]):
        block_size = min(p.shape[0] - l, l)
        top_segment = p[l-block_size:l]
        remaining_bot_segment = p[l:l+block_size]
        top_segment_mirrored = np.flip(top_segment, axis=0)
        if part == 1:
            if np.all(top_segment_mirrored == remaining_bot_segment):
                value = l * multiplier
        if part == 2:
            if list((top_segment_mirrored == remaining_bot_segment).flatten()).count(False) == 1:
                value = l * multiplier
    return value

parts = [1,2]
for part in parts:
    point = 0
    for p in puzzles:
        point += findMirror(p, 100, part)
        point += findMirror(np.rot90(p,-1), 1, part)
    print("part: ", part, point)
