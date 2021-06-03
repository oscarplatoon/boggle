from boggle_board import BoggleBoard

bb = BoggleBoard()
bb.shake()

i = 4
while i > 0:
    bb.shake()
    i -= 1