'''
You are watching a volleyball tournament, but you missed the beginning of the very first game of your favorite team. Now you're curious about how the coach arranged the players on the field at the start of the game.

The team you favor plays in the following formation:

0 3 0
4 0 2
0 6 0
5 0 1
where positive numbers represent positions occupied by players. After the team gains the serve, its members rotate one position in a clockwise direction, so the player in position 2 moves to position 1, the player in position 3 moves to position 2, and so on, with the player in position 1 moving to position 6.

Here's how the players change their positions:



Given the current formation of the team and the number of times k it gained the serve, find the initial position of each player in it.

Example

For

formation = [["empty",   "Player5", "empty"],
             ["Player4", "empty",   "Player2"],
             ["empty",   "Player3", "empty"],
             ["Player6", "empty",   "Player1"]]
and k = 2, the output should be

volleyballPositions(formation, k) = [
    ["empty",   "Player1", "empty"],
    ["Player2", "empty",   "Player3"],
    ["empty",   "Player4", "empty"],
    ["Player5", "empty",   "Player6"]
]
For

formation = [["empty", "Alice", "empty"],
             ["Bob",   "empty", "Charlie"],
             ["empty", "Dave",  "empty"],
             ["Eve",   "empty", "Frank"]]
and k = 6, the output should be

volleyballPositions(formation, k) = [
    ["empty", "Alice", "empty"],
    ["Bob",   "empty", "Charlie"],
    ["empty", "Dave",  "empty"],
    ["Eve",   "empty", "Frank"]
]
'''

def volleyballPositions(formation, k):
    p = [
        (2,1),
        (3,2),
        (1,2),
        (0,1),
        (1,0),
        (3,0)        
    ]
    
    res = [["empty" for _ in range(3)] for _ in range(4)]
    for i in range(6):
        oldPos = p[i]
        newPos = p[(i-k)%6]
        res[oldPos[0]][oldPos[1]] = formation[newPos[0]][newPos[1]]
        
    return res

