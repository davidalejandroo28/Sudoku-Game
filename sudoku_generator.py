import random
class SudokuGenerator:
# Assigns sudoku object attributes.
    def __init__(self, row_length, removed_cells):
        board = []
        for i in range(9):
            row = []
            for j in range(row_length):
                row.append(0)
            board.append(row)

        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = board
        self.box_length = round(row_length ** (0.5))

# Returns board object.
    def get_board(self):
        return self.board
# Prints the board object.
    def print_board(self):
        for i in range(9):
            sel_row = self.board[i]
            print(sel_row, end = '\n')
# Checks if num is not yet found in the row for the board.
    def valid_in_row(self, row, num):
        sel_row = self.board[row]
        for row_num in sel_row:
            if row_num == num :
                return False
        return True
# Checks if num is not yet found in the col for the board.
    def valid_in_col(self, col, num):
        for i in range(9):
            sel_column = self.board[i][col]
            if sel_column == num:
                return False
        return True
# Checks if the numbers can be placed in the box.
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == num:
                    return False
        return True
# Checks if the num is valid for all three conditions.
    def is_valid(self, row, col, num):
        row_check = self.valid_in_row(row, num)
        col_check = self.valid_in_col(col, num)
        box_check = self.valid_in_box(row // 3 * 3, col // 3 * 3, num)
        if row_check and col_check and box_check:
            return True
        else:
            return False
# Fills the box depending the starting coordinates.
    def fill_box(self, row_start, col_start):
        changing_list= []
        for i in range(row_start , row_start + 3):
            for j in range(col_start, col_start + 3):
                run = True
                while run == True:
                    changing_num = random.randint(1,9)
                    if changing_num in changing_list:
                        continue
                    elif changing_num not in changing_list:
                        self.board[i][j] = changing_num
                        changing_list.append(changing_num)
                        run = False
# Fills the diagonals for the board.
    def fill_diagonal(self):
        self.fill_box(0,0)
        self.fill_box(3,3)
        self.fill_box(6,6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
# Fills the necessary values in the board.
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
# Removes cells depending on the difficulty selected.
    def remove_cells(self):
        count = 0
        final_count = self.removed_cells
        while True:
            random_col = random.randint(0,8)
            random_row = random.randint(0,8)
            if self.board[random_row][random_col] == 0:
                continue
            elif self.board[random_row][random_col] != 0:
                self.board[random_row][random_col] = 0
                count += 1
            if count == final_count:
                return False

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
