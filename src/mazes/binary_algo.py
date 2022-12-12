from random import sample


class BinaryTree:

    def __init__(self, grid):
        for cell in grid.each_cell():
            neighbors = []
            if cell.north is not None:
                neighbors.append(cell.north)
            if cell.east is not None:
                neighbors.append(cell.east)

            if len(neighbors):
                cell.link(sample(neighbors, 1)[0])
