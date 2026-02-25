#QUESTION: Egg Dropping Puzzle (Minimum Number of Attempts
# eggs → number of eggs
# floors → number of floors in a building
# There exists a floor F such that:
# Any egg dropped from floor > F will break
# Any egg dropped from floor ≤ F will NOT break
# Your goal is to determine:
# 🎯 What is the minimum number of moves (in worst case) needed to guarantee finding F?

class Solution:
    def eggDrop(self, eggs, floors):
        dp = [[0]*(floors+1) for _ in range(eggs+1)]
        
        for i in range(1, eggs+1):
            for j in range(1, floors+1):
                if i == 1:         # Only 1 egg => must check each floor
                    dp[i][j] = j
                elif j == 1:       # Only 1 floor => 1 move
                    dp[i][j] = 1
                else:
                    dp[i][j] = float('inf')
                    for x in range(1, j+1):
                        worst = 1 + max(dp[i-1][x-1], dp[i][j-x])
                        dp[i][j] = min(dp[i][j], worst)
        
        return dp[eggs][floors]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.eggDrop(1, 2))   # Output: 2
    print(sol.eggDrop(2, 10))  # Output: 4
