def solution(s):
    ans = len(s)
    # 분할되는 사이즈
    sep = 1
    # 최대로는 전체 문자열 사이즈의 절반까지 슬라이싱 가능
    for sep in range(1, len(s)//2 + 1):
        # 슬라이싱 했을 때 문자
        new_s = ''
        # 전에 슬라이싱한 문자
        bef_char = ''
        # start idx를 나타냄
        st = 0
        # 중복되는 슬라이싱 문자의 갯수를 나타냄
        cnt = 1
        while True:
            # 처음 담을 때
            if bef_char == '':
                bef_char = s[st:st+sep]
                st = st+sep
                continue
            # 전 문자열이랑 지금문자열이랑 같을 때
            if bef_char == s[st:st+sep]:
                cnt += 1
            # 같지 않을 때
            else:
                # 1일 때는 숫자 안 넣어줌
                new_s += bef_char if cnt == 1 else str(cnt)+bef_char
                bef_char = s[st:st+sep]
                cnt = 1
            st = st+sep
            # 인덱스 초과했을 때
            if st > len(s):
                new_s += bef_char
                break
        ans = min(ans, len(new_s))
    return ans
