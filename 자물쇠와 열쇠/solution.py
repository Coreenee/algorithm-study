def rotate(arr, ith, m):
    if ith == 0:
        return arr
    dx = []
    dy = []
    new_arr = []
    for pos in arr:
        if ith == 1:
            new_arr.append((pos[1], m - pos[0] - 1))
        elif ith == 2:
            new_arr.append((m - pos[0] - 1, m - pos[1] - 1))
        else:
            new_arr.append((m - pos[1] - 1, pos[0]))
    return new_arr


def solution(key, lock):
    answer = True
    key_list = []
    lock_dict = {}
    lock_set = set()
    all_set = set()
    M = len(key)
    N = len(lock)

    for i in range(N):
        for j in range(N):
            all_set.update({(M - 1 + i, M - 1 + j)})
            if lock[i][j] == 0:
                lock_set.update({(M - 1 + i, M - 1 + j)})
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                key_list.append((i, j))
    key_dict = set()
    for ith in range(1, 4):
        new_arr = rotate(key_list, ith, M)
        for i in range(M + N):
            for j in range(M + N):
                for x, y in new_arr:
                    key_dict.update({(x + i, y + j)})
                if all_set.intersection(key_dict) == lock_set:
                    return True
                key_dict.clear()
    return False


print(
    solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
             [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
