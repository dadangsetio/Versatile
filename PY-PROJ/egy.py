
class game_of_life:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

       

       
