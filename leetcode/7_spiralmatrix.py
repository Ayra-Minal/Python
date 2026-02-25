'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        while matrix:
            
            #1 append 1st non empty list in order
            ret +=(matrix.pop(0))

            #2 append last elem of all list if not empty and pop
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            #3 append rev of last list if not empty
            if matrix:
                ret+=matrix.pop()[::-1]

            #4 append 1st elem in remaining in rev order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret

if __name__ == '__main__':
    sol=Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(matrix))
                               
