from collections import deque


def check_stick(pos, stick_list, bo_list):
    x, y = pos
    if y == 0:
        # 지면일 때
        return True
    if (x, y - 1) in stick_list:
        # 어떤 기둥위일 떄
        return True
    if (x - 1, y) in bo_list or (x, y) in bo_list:
        # 어떤 보 위일 때
        return True
    return False


def check_bo(pos, stick_list, bo_list):
    x, y = pos
    if (x, y - 1) in stick_list:
        # 보 시작좌표에 기둥이 있을 때
        return True
    if (x + 1, y - 1) in stick_list:
        # 보 끝좌표에 기둥이 있을 때
        return True
    if (x - 1, y) in bo_list and (x + 1, y) in bo_list:
        # 보 양쪽 끝에 보가 있을 떄
        return True
    return False


# 기둥 = 바닥위, 보의 한쪽 끝, 다른 기둥 위
# 보 = 한쪽 끝 부분이 기둥위, 양쪽 끝 부분이 다른 보
def solution(n, build_frame):
    answer = []
    stick_list = []
    bo_list = []
    for x, y, a, b in build_frame:
        # 구조물 삭제
        if b == 0:
            if a == 0:  # 기둥
                sflag = 0
                bflag = 0
                idx = stick_list.index((x, y))
                stick_list.pop(idx)
                for item in stick_list:
                    if not check_stick(item, stick_list, bo_list):
                        sflag = 1
                        break
                for item in bo_list:
                    if not check_bo(item, stick_list, bo_list):
                        bflag = 1
                        break
                if sflag or bflag:
                    stick_list.append((x, y))
            else:  # 보
                sflag = 0
                bflag = 0
                idx = bo_list.index((x, y))
                bo_list.pop(idx)
                for item in stick_list:
                    if not check_stick(item, stick_list, bo_list):
                        sflag = 1
                        break
                for item in bo_list:
                    if not check_bo(item, stick_list, bo_list):
                        bflag = 1
                        break
                if sflag or bflag:
                    bo_list.append((x, y))

        else:  # 구조물 생성
            if a == 0:  # 기둥
                if check_stick((x, y), stick_list, bo_list):
                    stick_list.append((x, y))
            else:  # 보
                if check_bo((x, y), stick_list, bo_list):
                    bo_list.append((x, y))

    for x, y in stick_list:
        answer.append((x, y, 0))
    for x, y in bo_list:
        answer.append((x, y, 1))

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer
