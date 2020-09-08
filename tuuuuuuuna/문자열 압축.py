def zip(s,i):
    len_s = len(s)
    index = 0
    now_string = ""
    new_string = ""
    cnt=1
    while index <=len_s:
        # print(now_string)
        next_string=s[index:index+i]
        # print("next",next_string)
        if now_string == next_string:
            cnt += 1
        else:
            if cnt == 1:
                new_string += now_string
                now_string=next_string
            else:
                # print(cnt)
                new_string += str(cnt) + now_string
                now_string = next_string
                cnt=1
        index+=i
    new_string+=now_string
    return new_string

def solution(s):
    answer = 1000
    max_size = len(s)//2 + 2
    #  len(s)//2 + 1 은 문제 5번을 통과하지 못함 -> 스트링 길이가 1일때 answer 1000 나옴
    #  print(solution('a')) -> 1000
    for i in range(1,max_size):
        temp = zip(s,i)
        if len(temp) < answer:
            answer=len(temp)
    return answer

# print(solution('a'))
# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))