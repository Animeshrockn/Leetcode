# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# ===========================================


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

    # =====================    
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         print(matrix[i][j])
        #         if target == matrix[i][j]:
        #             return True
        
        # return False
    # =====================
        # f_row = 0
        # l_row = len(matrix)-1

        # while(f_row <= l_row):

        #     mid_row = (f_row + l_row) //2

        #     if target < matrix[mid_row][0]:
        #         l_row = mid_row - 1
        #     elif  target > matrix[mid_row][-1]:
        #         f_row = mid_row + 1
        #     else:
        #         break
        
        # l = 0
        # r = len(matrix[0]) -1

        # while l <= r:

        #     mid = ( l + r ) //2

        #     if matrix[mid_row][mid] == target :
        #         return True
        #     elif target > matrix[mid_row][mid]:
        #         l = mid+1
        #     else:
        #         r = mid -1
        # return False

    # ====================

        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i]) -1

            while ( l <= r):

                mid = ( l + r) // 2

                if target == matrix[i][mid]:
                    return True
                elif target > matrix[i][mid]:
                    l = mid +1
                else:
                    
                    r = mid -1

        return False

        




matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target = 340


sol = Solution()
result = sol.searchMatrix(matrix, target)
print(f'Output : {result}')
