"""
The Towers of Hanoi puzzle, invented by the French mathematician Edouard Lucas in 1883, consists of a board with three
vertical poles and a stack of n disks.
The diameter of the disks increases as we progress from the top to bottom, creating a tower structure.
The objective is to move all of the disks from the starting pole to one of the other two poles to create a new tower.
There are, however, two restrictions:
                                    (1) only one disk can be moved at a time
                                    (2) a larger disk can never be placed on top of a smaller disk.

Solution:
         (S: Source Pole, D: Destination Pole, I: Intermediate Pole)
         Move the top n − 1 disks from pole S to pole I using pole D.
         Move the remaining disk from pole S to pole D.
         Move the n − 1 disks from pole I to pole D using pole S.

"""


def move(n: int, source_pole: int, destination_pole: int, intermediate_pole: int):
    if n >= 1:
        move(n-1, source_pole, intermediate_pole, destination_pole)
        print(f'Move {source_pole} -> {destination_pole}')
        move(n-1, intermediate_pole, destination_pole, source_pole)


move(4, 1, 3, 2)
