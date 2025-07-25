# 미로 찾기
def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    stack = [start]

    # 상, 하, 좌, 우
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while stack:
        current = stack.pop()
        x, y = current

        if (x, y) == end:
            print("성공: 출구에 도착했습니다.")
            return True

        if visited[x][y]:
            continue

        visited[x][y] = True  # 현재 위치 방문 표시

        # 상하좌우 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and
                maze[nx][ny] == 0 and not visited[nx][ny]):
                stack.append((nx, ny))

    print("실패: 출구에 도달할 수 없습니다.")
    return False

# 예시 미로 (0 = 이동 가능, 1 = 벽)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # 생쥐의 시작 위치
end = (4, 4)    # 출구 위치

solve_maze(maze, start, end)