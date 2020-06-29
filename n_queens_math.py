def solveNQueens(n):
    queensPosition = []
    DFS([], [], [], queensPosition, n)
    return queensPosition
    
def DFS(queens, xy_intersect_down, xy_intersect_up, queensPosition, n):
    row = len(queens)
    
    if row == n:
        queens = ['.' * i + 'Q' + '.' * (n - 1 - i) for i in queens]      
        queensPosition.append(queens)
        return
    
    for col in range(n):
        if col in queens or row - col in xy_intersect_down or row + col in xy_intersect_up:
            continue
            
        DFS(queens + [col],
            xy_intersect_down + [row - col],
            xy_intersect_up + [row + col],
            queensPosition, n)

[[print(f'[{column}]') if number != 3 else print(f'[{column}]\n') for number, column in enumerate(board)] for board in solveNQueens(4)]

