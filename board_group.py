import neopixel
class BoardGroup:
    
    def __init__(self, dead_zone) -> None:
        self.boards = []
        self.board_sizes = []
        self.dead_zone = dead_zone
 
    def fill(self, color):
        for board in self.boards:
            board.fill(color)
    def show(self):
        for board in self.boards:
            board.show()
    def add_board(self, board:neopixel.NeoPixel, board_size):
        self.board_sizes.append(board_size)
        self.boards.append(board)
    
    @property
    def num_pixels(self):
        return sum(self.board_sizes) - self.dead_zone
    
    def __setitem__(self, input_index:int, color):
        index = input_index + self.dead_zone
        board_index = 0 if index < self.board_sizes[0] else 1
        light_index = index - (board_index * self.board_sizes[0])
        self.boards[board_index][light_index] = color
        