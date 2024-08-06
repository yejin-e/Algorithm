def solution(friends, gifts):
    answer = 0
    dic = {}
    l = len(friends)
    gift = [[0 for _ in range(l)] for _ in range(l)]         # 주고 받은 선물
    total = [[0 for _ in range(2)] for _ in range(l)]        # 선물지수
    prediction = [0 for _ in range(l)]                       # 예측
       
    for i, x in enumerate(friends):
        dic[x] = i

    for x in gifts:
        a, b = x.split()
        gift[dic[a]][dic[b]] += 1
        total[dic[a]][0] += 1        # 준 선물 수
        total[dic[b]][1] += 1        # 받은 선물 수
    
    for i in range(l):
        for j in range(i+1, l):
            if gift[i][j] > gift[j][i]:
                prediction[i] += 1
            elif gift[i][j] < gift[j][i]:
                prediction[j] += 1
            else:
                a = total[i][0]-total[i][1]
                b = total[j][0]-total[j][1]
                if a > b:
                    prediction[i] += 1
                elif a < b:
                    prediction[j] += 1
                    
    return max(prediction)