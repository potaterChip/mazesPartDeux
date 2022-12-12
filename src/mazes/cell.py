class Cell:

    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.links = {}
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def link(self, cell, bidirectional=True):
        self.links[cell] = True
        if bidirectional:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidirectional=True):
        del self.links[cell]
        if bidirectional:
            cell.unlink(self, False)
        return self

    def is_linked(self, cell):
        return cell in self.links
