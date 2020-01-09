filename = input("대화 파일 이름을 확장자 포함 입력하세요: ")
the_takative = dict()
takative_time = dict()
lengthy_one = dict()
most, time, line = None, None, None
# 한 발화에 가장 길게 말한 사람 찾기 위한 변수들
maxLineTalker = '' 
maxLineCnt = 1
lineCnt = 1 # 한 사람이 말한 횟수 저장 변수 

with open(filename,'r') as f:
    while True:
        line = f.readline()
        if line.startswith('['):
            most, time = line.split('] ')[0], line.split('] ')[1]
            # 많이 말한 사람
            if most not in the_takative: the_takative[most] = 1
            else: the_takative[most] += 1
            # 많이 말한 시간
            if time not in takative_time: takative_time[time] = 1
            else: takative_time[time] += 1
        elif line.startswith('-'): continue
        elif not line: break
        """
        else:
            while True:
                if line.startswith('[') != True: break
                if lineCnt == 1: maxLineTalker = most
                lineCnt += 1
                line = f.readline()
            if lineCnt > maxLineCnt:
                maxLineCnt = lineCnt
         """

            

    max_k, max_v = None, None
    for k,v in the_takative.items():
        if max_v==None or max_v < v:
            max_k = k
            max_v = v
    print("가장 많이 말한 사람: ", max_k[1:], ",   횟수: ", max_v)

    max_k, max_v = None, None
    for k,v in takative_time.items():
        if max_v==None or max_v < v:
            max_k = k
            max_v = v
    print("가장 많이 말한 시간: ", max_k[1:], ",   횟수: ", max_v)

    """
    max_k, max_v = None, None
    for k,v in lengthy_one.items():
        if max_v==None or max_v < v:
            max_k = k
            max_v = v
    print("가장 길게 말한 사람: ", "줄수: ")
    """