from boggle_board import BoggleBoard
from boggle_dice import BoggleDice

# initialize dice
dice_values_list = [
    "AAEEGN",
    "ELRTTY",
    "AOOTTW",
    "ABBJOO",
    "EHRTVW",
    "CIMOTU",
    "DISTTY",
    "EIOSST",
    "DELRVY",
    "ACHOPS",
    "HIMNQU",
    "EEINSU",
    "EEGHNW",
    "AFFKPS",
    "HLNNRZ",
    "DEILRX"
]

dice_list = [BoggleDice(s) for s in dice_values_list]

# initialize board
bb = BoggleBoard(dice_list)

# call shake
i = 4
while i > 0:
    bb.shake()
    i -= 1
