class Node:
    def __init__(self, char):
        self.char = char
        self.data = None
        self.children = {}
        self.length = {}


def insert(word, head):
    curNode = head
    w_len = len(word)
    for w in word:
        if w in curNode.children:
            curNode = curNode.children[w]
        else:
            newNode = Node(w)
            curNode.children[w] = newNode
            curNode = curNode.children[w]
        if w_len in curNode.length:
            curNode.length[w_len] += 1
        else:
            curNode.length[w_len] = 1
    curNode.data = word


def solution(words, queries):
    answer = []
    head = Node('')
    bhead = Node('')
    cnt_dict = {}
    for word in words:
        insert(word, head)
        insert(word[::-1], bhead)
        if len(word) in cnt_dict:
            cnt_dict[len(word)] += 1
        else:
            cnt_dict[len(word)] = 1

    for query in queries:
        if query[0] == '?' and query[-1] == '?':  # ??????일떄
            try:
                answer.append(cnt_dict[len(query)])
            except:
                answer.append(0)
        else:
            org_len = len(query)
            if query[0] == '?':
                query = query[::-1]
                cur = bhead
            else:
                cur = head
            query = query.split("?")[0]
            idx = 0
            flag = 0
            for char in query:
                if char in cur.children:
                    cur = cur.children[char]
                else:
                    flag = 1
                    break
            if flag:
                answer.append(0)
            else:
                try:
                    answer.append(cur.length[org_len])
                except:
                    answer.append(0)

    return answer
