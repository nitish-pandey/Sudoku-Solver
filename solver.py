import numpy as np

class Sudoku:
    grid=np.zeros((9,9))

    row=np.zeros((10,10))
    col=np.zeros((10,10))
    box=np.zeros((3,3,10))

    def __init__(self,grid):
        self.grid = np.asarray(grid,dtype=int)

    
        
    def validate(self):
        for i in range(9):
            for j in range(9):
                a=self.grid[i][j]
                if a==0:
                    continue
                if self.row[i][a]==1 or self.col[j][a]==1 or self.box[i//3][j//3][a]==1:
                    return False
                self.box[i//3][j//3][a]=1
                self.col[j][a]=1
                self.row[i][a]=1

        return True
    
    def solve(self,x=0,y=0):
        if y==9:
            y=0
            x+=1
        
        if x==9:
            return True
        
        if self.grid[x][y]!=0:
            return self.solve(x,y+1)

        for i in range(1,10):
            if self.row[x][i] or self.col[y][i] or self.box[x//3][y//3][i]:
                continue

            self.row[x][i]=1
            self.col[y][i]=1
            self.box[x//3][y//3][i]=1

            self.grid[x][y]=i

            if self.solve(x,y+1):
                return True

            self.row[x][i]=0
            self.col[y][i]=0
            self.box[x//3][y//3][i]=0

            self.grid[x][y]=0

        return False
