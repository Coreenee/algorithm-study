def devide(w):
    if w =='':
        return ''
    check = 0
    w_size=len(w)
    for i in range(w_size):
        if w[i] == "(":
            check += 1
        else:
            check -= 1
        if check==0:
            u = w[:i+1]
            v = w[i+1:]
            if checker(u):
                return u + devide(v)
            else:
                temp = "("
                temp += devide(v)
                temp += ")"
                u = u[1:-1]
                for _ in u:
                    if _ == "(":
                        temp+=")"
                    else: temp +="("
                return temp

def checker(s):
    if s[0]=='(': return True
    else: return False

def solution(p):
    answer = devide(p)
    return answer

# w=")))((("
# ans = devide(w)
# print(ans)