def make_word_dict(words):
    words_dict={}
    for word in words:
        key = len(word)
        if key in words_dict:
            words_dict[key].append(word)
        else:
            words_dict[key]=[word]
    return words_dict

def first_wildcard(query,key):
    reverse = 0
    if query[0]=="?":
        query = query[::-1]
        reverse = 1
    for i in range(key):
        if query[i] == "?":
            return i, reverse

def find(query,key,words_dict):
    cnt=0
    wildcard, reverse = first_wildcard(query,key)
    if reverse:
        new_query = query[::-1][:wildcard]
    else:
        new_query = query[:wildcard]
    for word in words_dict[key]:
        if reverse:
            new_word=word[::-1][:wildcard]
        else:
            new_word=word[:wildcard]
        if new_query == new_word:
            cnt +=1
    return cnt


def solution(words, queries):
    answer = []
    words_dict = make_word_dict(words)
    ans_dict={}
    for query in queries:
        if query not in ans_dict:
            key = len(query)
            if key in words_dict:
                temp=find(query,key,words_dict)
                answer.append(temp)
                ans_dict[query]=temp
            else:
                answer.append(0)
                ans_dict[query]=0
        else:
            answer.append(ans_dict[query])
    return answer


words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
# 효율성 검사 2번 통과 못함