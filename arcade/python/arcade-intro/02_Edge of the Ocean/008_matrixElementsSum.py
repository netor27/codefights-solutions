def matrixElementsSum(matrix):
    '''
    After they became famous, the CodeBots all decided to move to a new building 
    and live together. The building is represented by a rectangular matrix of rooms. 
    Each cell in the matrix contains an integer that represents the price of the room. 
    Some rooms are free (their cost is 0), but that's probably because they are haunted, 
    so all the bots are afraid of them. That is why any room that is free or is located 
    anywhere below a free room in the same column is not considered suitable for the bots 
    to live in.
    Help the bots calculate the total price of all the rooms that are suitable for them.
    '''
    maxX = len(matrix)
    maxY = len(matrix[0])
    total = 0

    # Sum every colum until we found a 0, then move to the next column
    for y in range(maxY):
        for x in range(maxX):
            if matrix[x][y] == 0:
                break
            total += matrix[x][y]

    return total


print(matrixElementsSum([[0, 1, 1, 2], 
                         [0, 5, 0, 0], 
                         [2, 0, 3, 3]]))
