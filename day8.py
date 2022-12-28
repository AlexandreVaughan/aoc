

class Grid:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.row_count = len(grid)
        self.column_count = len(grid[0])
    
    def is_edge_tree(self,row,column):
        return (column == 0 
                or column == self.column_count-1
                or row == 0
                or row == self.row_count -1)

    def count_visible(self):
        sum_visible = 0
        for row in range(0,self.row_count):
            for column in range(0,self.column_count):
                if self.is_edge_tree(row, column):
                    sum_visible +=1
                    continue
                if self.is_central_tree_visible(row,column):
                    sum_visible +=1
        return sum_visible

    def max_scenic_score(self):
        max_score = 0
        for row in range(0,self.row_count):
            for column in range(0,self.column_count):
                max_score = max(max_score,self.scenic_score(row,column))
        return max_score


    def check_visible_on_line(self,row,column,horz_direction,vert_direction):
        height = self.grid[row][column]
        if vert_direction == -1:
            while row > 0:
                row -= 1
                if self.grid[row][column] >= height:
                    return False
        elif vert_direction == 1:
            while row < self.row_count-1:
                row += 1
                if self.grid[row][column] >= height:
                    return False
        elif horz_direction == -1:
            while column > 0:
                column -= 1
                if self.grid[row][column] >= height:
                    return False
        elif horz_direction == 1:
            while column < self.column_count-1:
                column += 1
                if self.grid[row][column] >= height:
                    return False
        return True

    def visible_tree_count(self,row,column,horz_direction,vert_direction):
        count = 0
        height = self.grid[row][column]
        if vert_direction == -1:
            while row > 0:
                count +=1
                row -= 1
                if self.grid[row][column] >= height:
                    return count
        elif vert_direction == 1:
            while row < self.row_count-1:
                count +=1
                row += 1
                if self.grid[row][column] >= height:
                    return count
        elif horz_direction == -1:
            while column > 0:
                count +=1
                column -= 1
                if self.grid[row][column] >= height:
                    return count
        elif horz_direction == 1:
            while column < self.column_count-1:
                count +=1
                column += 1
                if self.grid[row][column] >= height:
                    return count    
        return count
    
    def scenic_score(self,row,column):
        if self.is_edge_tree(row,column):
            return 0
        return (self.visible_tree_count(row,column,1,0)
        * self.visible_tree_count(row,column,-1,0)
        * self.visible_tree_count(row,column,0,1)
        * self.visible_tree_count(row,column,0,-1))


    def is_central_tree_visible(self,row,column):
        return (self.check_visible_on_line(row,column,1,0)
        or self.check_visible_on_line(row,column,-1,0)
        or self.check_visible_on_line(row,column,0,1)
        or self.check_visible_on_line(row,column,0,-1))


def count_visible_trees(forest):
    grid = Grid(forest)
    return grid.count_visible()
    
def max_scenic_score(forest):
    grid = Grid(forest)
    return grid.max_scenic_score()
    
    
with open('day8.txt') as file:
    forest = []
    for line in file:
        tree_array = list(map(int,list(line.strip())))
        forest.append(tree_array)
    print(count_visible_trees(forest))
    print(max_scenic_score(forest))