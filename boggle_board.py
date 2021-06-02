import random
import string

class BoggleBoard:
    # I'll represent the board as a list of lists [[column1],[column2], [column3], [column4]] so boggle[i][j] gives:
    # i = row
    # j = column


    def __init__(self):
        self.board = self.blank_board()

    def __str__(self):
        output_str = ""
        for i in range(4):
            line_str = ""
            for char in self.board[i]:
                line_str += char
            line_str += "\n"
            output_str += line_str
        return(output_str)

    def shake(self):
        #if I use these letters elsewhere, I should move this.
        letters = string.ascii_uppercase
        i = 0
        j = 0
        while i < 4:
            j=0
            while j < 4:
                self.board[i][j] = ("".join(random.choice(letters)))
                j += 1
            i += 1
        print("Every time you rattle the board, it's a: \nwhole \nnew \nworld\n")

            

    #This is called at init to create a blank board.
    def blank_board(self):
        blank = "_"
        output_list = []
        for item in range(4):
            line_on_board = []
            for char_index in range(4):
                line_on_board.append(blank)
            output_list.append(line_on_board)
        return output_list

new_boggle = BoggleBoard()
print(new_boggle)
#print(new_boggle.board)
new_boggle.shake()
print(new_boggle)