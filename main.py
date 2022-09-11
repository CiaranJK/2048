"""
2048 Game
"""

# import random
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """

    row = []
    for index in range(0, (len(line))):
        row.append(line[index])
        for number in row:
            if number == 0:
                row.remove(number)
                row.append(0)
    for index in range(0, (len(row)) - 1):
        if row[index] == row[index + 1]:
            row[index] = (row[index] + row[index + 1])
            row[index + 1] = 0
            row.remove(row[index + 1])
            row.append(0)
    return row


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._board = [[0 for col in range(0, self._grid_width)]
                       for row in range(self._grid_height)]
        self._direction_indices = {UP: [(0, col) for col in range(self._grid_width)],
                                   DOWN: [((self._grid_height - 1), col) for col in range(self._grid_width)],
                                   LEFT: [(row, 0) for row in range(self._grid_height)],
                                   RIGHT: [(row, (self._grid_width - 1)) for row in range(self._grid_height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        for row_index in range(self._grid_height):
            for col_index in range(self._grid_width):
                self._board[row_index][col_index] = 0

        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "Twenty Forty Eight"

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        temporary_grid = []
        temporary_grid_2 = []

        counter_1 = 0
        counter_2 = 0

        if direction == UP or direction == DOWN:
            height_or_width = self._grid_height
        elif direction == LEFT or direction == RIGHT:
            height_or_width = self._grid_width
        else:
            height_or_width = 0

        for index in range(0, len(self._direction_indices[direction])):
            temporary_grid.append([])

        for measure in range(0, height_or_width):
            for index in range(0, len(temporary_grid)):
                temporary_grid[index].append(self.get_tile(((self._direction_indices[direction][index][0]) + counter_1),
                                                           ((self._direction_indices[direction][index][1]) + counter_2)))
            counter_1 += OFFSETS[direction][0]
            counter_2 += OFFSETS[direction][1]

        counter_1 = 0
        counter_2 = 0

        for index in range(0, len(temporary_grid)):
            temporary_grid_2.append(merge(temporary_grid[index]))

        for measure in range(0, height_or_width):
            for index in range(0, len(temporary_grid)):
                temporary_grid[index].append(self.set_tile(((self._direction_indices[direction][index][0]) + counter_1),
                                                           ((self._direction_indices[direction][index][1]) + counter_2),
                                                           temporary_grid_2[index][measure]))
            counter_1 += OFFSETS[direction][0]
            counter_2 += OFFSETS[direction][1]

        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        row_index = random.randint(0, (self._grid_height - 1))
        col_index = random.randint(0, (self._grid_width - 1))

        two_or_four_selector = random.randint(1, 10)
        if self.get_tile(row_index, col_index) == 0 and two_or_four_selector != 10:
            self.set_tile(row_index, col_index, 2)
        elif self.get_tile(row_index, col_index) == 0 and two_or_four_selector == 10:
            self.set_tile(row_index, col_index, 4)
        else:
            space_counter = (self._grid_height * self._grid_width)

            for row_index in range(self._grid_height):
                for col_index in range(self._grid_width):
                    if self._board[row_index][col_index] != 0:
                        space_counter -= 1

            if space_counter <= 0:
                return None
            else:
                self.new_tile()

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]
