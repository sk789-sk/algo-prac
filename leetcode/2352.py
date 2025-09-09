# # 2352. Equal Row and Column Pairs

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


def solution(grid):
        #Get all Rows in the Grid and Get all COlumns in the grid.
        #Add all the rows to the set. then see column is in the set. if so +=1 and return total.
        
        #way to get the columns
        # col_list = []
        # for i in range(0,len(grid)):
        #     col_list.append([row[i] for row in grid])
        # print(col_list)
        
        n = len(grid)
        # col = {i:[] for i in range(n)}
        cols = [[] for _ in range(n)]
        #can replace with a list of lists [[col0],[col1],[col2]]
        count = 0

        row_dict = {}
        for row in grid:
            row_dict[tuple(row)] = row_dict.get(tuple(row),0) + 1
            # row_dict[](tuple(row))
            for idx,val in enumerate(row):
                cols[idx].append(val)

        for col in cols:
            count += row_dict.get(tuple(col),0)
        print(count)
        return count


# grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

solution(grid)