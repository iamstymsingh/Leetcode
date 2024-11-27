class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rc, cc = len(matrix), len(matrix[0])
        low, high = 0, rc*cc-1
        while low <= high:
            mid = low + (high - low)//2
            processed_val = matrix[mid // cc][mid % cc]
            if processed_val == target:
                return True
            elif processed_val < target:
                low = mid+1
            else:
                high = mid-1
        return False
            