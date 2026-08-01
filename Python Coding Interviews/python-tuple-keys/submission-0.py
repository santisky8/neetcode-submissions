from typing import List, Set, Tuple


def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    result = set()

    # Unpack index (r_idx) and the row itself (row)
    for r_idx, row in enumerate(grid):
        # Unpack column index (c_idx) and the cell value (val)
        for c_idx, val in enumerate(row):
            # Check the actual value instead of indexing the grid with tuples
            if val == 1:
                result.add((r_idx, c_idx))

    return result


# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
