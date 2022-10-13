class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        traingle = []
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[-1], row[0] = 1,1
            
            for j in range(1,len(row)-1):
                row[j] = traingle[i-1][j] + traingle[i-1][j-1]
            traingle.append(row)
        return traingle