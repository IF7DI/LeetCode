class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for row in matrix:
            for col in row:
                
                if col == target:
                    return True
        else:
            return False
        