def isRight(w):
    cnt = 0
    for char in w:
        if char == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True


def operate(w):
    if len(w) == 0:
        return ''
    cnt = 0
    u, v = '', ''
    v_idx = 0
    #군형잡힌 문자열 검사
    for idx, char in enumerate(w):
        if char == '(':
            cnt += 1
        else:
            cnt -= 1
        u += char
        if cnt == 0:
            v_idx = idx + 1
            break
    #Valid 인덱스일 때
    if v_idx < len(w):
        v = w[v_idx:]
    #u가 올바른 괄호 문자열이라면
    if isRight(u):
        return u + operate(v)
    #그렇지 않다면
    else:
        new = '(' + operate(v) + ')'
        if len(u) >= 2:
            u = u[1:-1]
            for i in range(len(u)):
                if u[i] == '(':
                    new += ')'
                else:
                    new += '('
        return new


def solution(p):
    answer = ''
    answer = operate(p)
    return answer