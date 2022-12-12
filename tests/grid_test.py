import pytest
from mazes.grid import Grid


class TestGrid:

    def test_grid_prep(self):
        grid = Grid(2, 3)
        assert grid.grid[0][2].row == 0
        assert grid.grid[0][2].column == 2
        assert grid.grid[0][0].north is None
        assert grid.grid[1][0].north.row == 0
        assert grid.grid[0][2].east is None
        assert grid.grid[0][1].east.column == 2
