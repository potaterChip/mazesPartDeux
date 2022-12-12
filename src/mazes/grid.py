from mazes.cell import Cell


class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        grid = []
        for row in range(self.rows):
            grid.append([])
            for column in range(self.columns):
                grid[row].append(Cell(row, column))
        return grid

    def configure_cells(self):
        for cell_row in self.grid:
            for cell in cell_row:
                if cell is None:

                    continue
                else:
                    row, column = cell.row, cell.column
                    cell.north = self.get_cell(row - 1, column)
                    cell.south = self.get_cell(row + 1, column)
                    cell.west = self.get_cell(row, column - 1)
                    cell.east = self.get_cell(row, column + 1)

    def get_cell(self, row, column):
        if row in range(0, self.rows) and column in range(0, self.columns):
            return self.grid[row][column]
        else:
            return None

    def each_cell(self):
        for row in self.grid:
            for cell in row:
                if cell is not None:
                    yield cell
                else:
                    continue

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"

        for row in self.grid:
            top = "|"
            bottom = "+"

            for cell in row:
                if cell is None:
                    cell = Cell(-1, -1)

                body = "   "
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary

                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner

            output += top + "\n" + bottom + "\n"
        return output
