def bfs(left, right, board):
    N = len(board)
    visit_dict = {(left, right): 1}
    queue = [(left, right, 0)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while queue:
        tmp_queue = []
        for ((l_x, l_y), (r_x, r_y), cnt) in queue:
            if (l_x, l_y) == (N - 1, N - 1) or (r_x, r_y) == (N - 1, N - 1):
                return cnt
            for i in range(4):
                nl_x, nl_y = l_x + dx[i], l_y + dy[i]
                nr_x, nr_y = r_x + dx[i], r_y + dy[i]
                if l_x == r_x:
                    if 0 <= nl_x < N and 0 <= nl_y < N and 0 <= nr_x < N and 0 <= nr_y < N:
                        if board[nl_x][nl_y] == 0 and board[nr_x][nr_y] == 0:
                            if i == 1:
                                if ((l_x, l_y), (l_x + 1,
                                                 l_y)) not in visit_dict:
                                    visit_dict[((l_x, l_y), (l_x + 1,
                                                             l_y))] = 1
                                    tmp_queue.append(
                                        ((l_x, l_y), (l_x + 1, l_y), cnt + 1))
                                if ((r_x + 1, r_y), (r_x,
                                                     r_y)) not in visit_dict:
                                    visit_dict[((r_x + 1, r_y), (r_x,
                                                                 r_y))] = 1
                                    tmp_queue.append(
                                        ((r_x + 1, r_y), (r_x, r_y), cnt + 1))
                            elif i == 3:
                                if ((l_x, l_y), (l_x - 1,
                                                 l_y)) not in visit_dict:
                                    visit_dict[((l_x, l_y), (l_x - 1,
                                                             l_y))] = 1
                                    tmp_queue.append(
                                        ((l_x, l_y), (l_x - 1, l_y), cnt + 1))
                                if ((r_x - 1, r_y), (r_x,
                                                     r_y)) not in visit_dict:
                                    visit_dict[((r_x - 1, r_y), (r_x,
                                                                 r_y))] = 1
                                    tmp_queue.append(
                                        ((r_x - 1, r_y), (r_x, r_y), cnt + 1))
                            if ((nl_x, nl_y), (nr_x, nr_y)) not in visit_dict:
                                visit_dict[((nl_x, nl_y), (nr_x, nr_y))] = 1
                                tmp_queue.append(
                                    ((nl_x, nl_y), (nr_x, nr_y), cnt + 1))
                else:
                    if 0 <= nl_x < N and 0 <= nl_y < N and 0 <= nr_x < N and 0 <= nr_y < N:
                        if board[nl_x][nl_y] == 0 and board[nr_x][nr_y] == 0:
                            if i == 0:
                                if ((l_x, l_y), (l_x,
                                                 l_y + 1)) not in visit_dict:
                                    visit_dict[((l_x, l_y), (l_x,
                                                             l_y + 1))] = 1
                                    tmp_queue.append(
                                        ((l_x, l_y), (l_x, l_y + 1), cnt + 1))
                                if ((r_x, r_y + 1), (r_x,
                                                     r_y)) not in visit_dict:
                                    visit_dict[((r_x, r_y + 1), (r_x,
                                                                 r_y))] = 1
                                    tmp_queue.append(
                                        ((r_x, r_y + 1), (r_x, r_y), cnt + 1))
                            elif i == 2:
                                if ((l_x, l_y), (l_x,
                                                 l_y - 1)) not in visit_dict:
                                    visit_dict[((l_x, l_y), (l_x,
                                                             l_y - 1))] = 1
                                    tmp_queue.append(
                                        ((l_x, l_y), (l_x, l_y - 1), cnt + 1))
                                if ((r_x, r_y - 1), (r_x,
                                                     r_y)) not in visit_dict:
                                    visit_dict[((r_x, r_y - 1), (r_x,
                                                                 r_y))] = 1
                                    tmp_queue.append(
                                        ((r_x, r_y - 1), (r_x, r_y), cnt + 1))
                            if ((nl_x, nl_y), (nr_x, nr_y)) not in visit_dict:
                                visit_dict[((nl_x, nl_y), (nr_x, nr_y))] = 1
                                tmp_queue.append(
                                    ((nl_x, nl_y), (nr_x, nr_y), cnt + 1))
        queue = tmp_queue
    return 0


def solution(board):
    return bfs((0, 0), (0, 1), board)