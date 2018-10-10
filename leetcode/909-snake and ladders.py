

class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        limit = n * n - 1
        routine = [board[i][j] if (i % 2 != n % 2) else board[i][n - 1 - j] for i in range(n - 1, -1, -1) for j in range(n)]

        discovered = [0]
        measured = {0: 0}

        def adjacents(position, limit):
            farthest = -1
            for i in range(min(position + 6, limit), position, -1):
                target = routine[i] - 1
                if target == -2:
                    if farthest == -1:
                        farthest = i
                        yield farthest
                    else:
                        continue
                elif target < limit and i < limit:
                    yield target
                else:
                    yield limit

        while discovered:
            position = discovered.pop(0)
            step = measured[position]
            adjacent = sorted(set(adjacents(position, limit)))

            for a in adjacent:
                if a not in measured:
                    measured[a] = step + 1
                    discovered.append(a)

        if limit in measured:
            return measured[limit]
        else:
            return -1

# board = [
# [1,-1],
# [7,-1]]
   
# board = [
# [1,1,-1],
# [1,1,1],
# [-1,1,1]]

board = [
[-1,-1,19,10,-1],
[2,-1,-1,6,-1],
[-1,17,-1,19,-1],
[25,-1,20,-1,-1],
[-1,-1,-1,-1,15]]

# board = [
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]

s = Solution()
r = s.snakesAndLadders(board)

pass
