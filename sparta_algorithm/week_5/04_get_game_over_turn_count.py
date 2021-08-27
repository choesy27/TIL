k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(chess_map)
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)

    turn_count = 1

    while turn_count <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]

            # 파란색이거나 맵을 나갔을 때
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)

                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                # 앞길이 막혔다면 그 자리에 머무름.
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                continue

            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]

                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break

            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c

            # 턴이 진행되는 중, 말이 4개 이상 쌓이는 순간 종료된다.
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        turn_count += 1
    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다