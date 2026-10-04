class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_memory = {
            0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}
        }
        row_memory = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}}
        box_memory = {
            0: {0: {}, 1: {}, 2: {}}, # top 3 boxes
            1: {0: {}, 1: {}, 2: {}},
            2: {0: {}, 1: {}, 2: {}}
        }
        for row_index in range(0, 9):
            for column_index in range(0, 9):
                item = board[row_index][column_index]
                # pass if no number
                if item == ".":
                    continue
                # check row constraint
                if row_memory[row_index].get(item, None) != None:
                    return False
                # check column constraint
                if column_memory[column_index].get(item, None) != None:
                    return False
                # classify box
                box_x_index = row_index // 3
                box_y_index = column_index // 3
                # check box constraint
                if box_memory[box_x_index][box_y_index].get(item, None) != None:
                    return False

                # all checks passed -> store to memory
                row_memory[row_index][item] = 1
                column_memory[column_index][item] = 1
                box_memory[box_x_index][box_y_index][item] = 1
        return True

                