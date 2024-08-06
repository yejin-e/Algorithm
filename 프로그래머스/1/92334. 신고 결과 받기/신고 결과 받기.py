def solution(id_list, report, k):
    l = len(id_list)
    answer = []
    uid = []
    arr = [[0 for _ in range(l)] for _ in range(l)]
    
    dic = {k: v for v, k in enumerate(id_list)}   # {유저 ID: index}
    
    for r in report:          
        a, b = r.split()
        arr[dic[a]][dic[b]] = 1   # 2차원배열로 신고 취합 (신고자, 불량자)
    
    for i, col in enumerate(zip(*arr)):
        if k <= sum(col):         # 정지 기준 < 신고당한 횟수
            uid.append(i)         # i = 정지된 ID의 index
    
    for i in range(l):            # 처리 결과 메일을 받은 횟수
        s = 0
        for j in uid:
            s += (arr[i][j])    
        answer.append(s)

    return answer