class Solution(object):
    def minTimeToReach(self, moveTime):
        N, M = len(moveTime), len(moveTime[0])
        di = [(-1, 0), (0, 1), (0, -1), (1, 0)] #NEWS
        hp = [(0, 0, 0)] #cost, start, end
        res = [[float('inf')] * M for _ in range(N)]
        res[0][0] = 0
        while hp:
            cost, x, y = heappop(hp)
            for dx, dy in di:
                newx, newy = x + dx, y + dy
                if 0 <= newx < N and 0 <= newy < M:
                    curr = max(cost + 1, moveTime[newx][newy] + 1)
                    if curr < res[newx][newy]:
                        res[newx][newy] = curr
                        heappush(hp, (curr, newx, newy))
        return res[N - 1][M - 1] 