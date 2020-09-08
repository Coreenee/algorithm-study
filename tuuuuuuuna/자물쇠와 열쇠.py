import copy

def turn_key(key):
    size_key = len(key)
    turned_key=[]
    for i in range(size_key):
        turned_key.append([])
    for row in key:
        for index in range(size_key):
            turned_key[size_key-index-1].append(row[index])
    return turned_key

def LockPlusKey(key,lock,start_x,start_y):
    size_key = len(key)
    new_lock = copy.deepcopy(lock)
    for i in range(size_key):
        for j in range(size_key):
            if 0<=(start_x+j)<len(lock) and 0<= (start_y+i) <len(lock):
                new_lock[start_x+j][start_y+i] += key[j][i]
    return new_lock


def is_open(key,lock):
    TF_list=[]
    size_lock = len(lock)
    size_key = len(key)
    max_size = size_lock - size_key + 1
    for i in range(1-size_key, size_lock+size_key):
        for j in range(1-size_key, size_lock+size_key):
            checker=1
            new_lock = LockPlusKey(key,lock,i,j)
            for k in range(size_lock):
                for l in range(size_lock):
                    checker *= new_lock[k][l]
            TF_list.append(checker)
    return TF_list


def solution(key,lock):
    ans_list = []
    for i in range(4):
        ans_list=is_open(key, lock)
        key = turn_key(key)
        if 1 in ans_list:
            return True
    return False



# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# print(solution(key,lock))