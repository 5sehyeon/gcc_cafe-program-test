import pandas as pd
import csv

 # 5.2일 알고리즘 시험 완료..시범운용가능상태..
 # 해야할 것들: 카톡이름보면서, 예외추가와 메뉴추가(가격정확하게!), 가능한 맨트들 추가.
 # 버전 업그레이드를 위한 생각: 문자열안에 포맷문자 생각해보기,,대화 하나하나를 읽는 알고리즘 생각해보기,,엄마 아빠 매칭(2세한테.),,어르신 = 신종훈 목사님 = 대표님, 위상무 = 위세량 오봉 = 오봉엽, 산양 = 선영, 
 

with open("C:/Users/오세현/Desktop/버전1시험 최종 카톡내용.txt", "r", encoding="UTF-8") as f:
    
    # 딕셔너리로 이름과 항목별 돈을 정리.
    dic1 = {"세현": [0, 0, 0, 0], "오쭈": [0, 0, 0, 0], "유빈": [0, 0, 0, 0], "싸리" : [0, 0, 0, 0], "하루" : [0, 0, 0, 0],
            "하루나" : [0, 0, 0, 0], "박혜" : [0, 0, 0, 0], "주혜" : [0, 0, 0, 0], "장미" : [0, 0, 0, 0], "김미" : [0, 0, 0, 0],
            "이쭈" : [0, 0, 0, 0], "단디" : [0, 0, 0, 0], "데이빗" : [0, 0, 0, 0], "까루나" : [0, 0, 0, 0], "재순" : [0, 0, 0, 0]
            ,"김향" : [0, 0, 0, 0], "규온": [0, 0, 0, 0], "김호": [0, 0, 0, 0], "정설":[0, 0, 0, 0], "윤미": [0, 0, 0, 0], "세량": [0, 0, 0, 0],
            "데코팀" : [0, 0, 0, 0], "농사팀" : [0, 0, 0, 0], "서인":[0, 0 ,0 ,0]}
                      # 먹 주 받 총
    lst2 = [""]

                    
    # 반복되는 (예외)부분 함수로 정리.   # 이름이 직접써져있는 코드들은 전부 예외의 경우 ! 홍이모!!!!!!!
    def lots_give(i, dic1, cup, count):
        
        for j in range(0, (i.count(",")+1)):
            count = count + 2
            re = i[(len(i)-(count))][0:2]
            if (re == "하루") and (i[(len(i)-(count))][2] == "나"):
                dic1["하루나"][2] = dic1["하루나"][2] + (3000*cup)
                dic1["하루나"][3] = dic1["하루나"][3] + (3000*cup)
            elif re == "까루":
                dic1["까루나"][2] = dic1["까루나"][2] + (3000*cup)
                dic1["까루나"][3] = dic1["까루나"][3] + (3000*cup)
            elif re == "데이":
                dic1["데이빗"][2] = dic1["데이빗"][2] + (3000*cup)
                dic1["데이빗"][3] = dic1["데이빗"][3] + (3000*cup)
            # 이름이 두 글자인 경우(콤마를 쓸때, 성까지 붙여서 말해줘야한다.ex)정설이 , 김향누나 , 김호에게)
            elif re == "김향":
                dic1["김향"][2] = dic1["김향"][2] + (3000*cup)
                dic1["김향"][3] = dic1["김향"][3] + (3000*cup)
            elif re == "김호":
                dic1["김호"][2] = dic1["김호"][2] + (3000*cup)
                dic1["김호"][3] = dic1["김호"][3] + (3000*cup)
            elif re == "정설":
                dic1["정설"][2] = dic1["정설"][2] + (3000*cup)
                dic1["정설"][3] = dic1["정설"][3] + (3000*cup) 
                
                
            else:
                dic1[re][2] = dic1[re][2] + (3000*cup)
                dic1[re][3] = dic1[re][3] + (3000*cup)
                
    def one_give(re, dic1, i, cup):
        # 이름을 세글자로 불러야 하는 경우.
        if (re == "하루") and (i[(len(i)-4)][2] == "나"):                            
            dic1["하루나"][2] = dic1["하루나"][2] + (3000*cup)
            dic1["하루나"][3] = dic1["하루나"][3] + (3000*cup)
        elif re == "까루":                                                          
            dic1["까루나"][2] = dic1["까루나"][2] + (3000*cup)
            dic1["까루나"][3] = dic1["까루나"][3] + (3000*cup)
        elif re == "데이":
            dic1["데이빗"][2] = dic1["데이빗"][2] + (3000*cup)
            dic1["데이빗"][3] = dic1["데이빗"][3] + (3000*cup)
            
        # 이름이 두 글자인 경우(김향)
        elif re == "향님":
            dic1["김향"][2] = dic1["김향"][2] + (3000*cup)
            dic1["김향"][3] = dic1["김향"][3] + (3000*cup)
        elif re == "향이":
            dic1["김향"][2] = dic1["김향"][2] + (3000*cup)
            dic1["김향"][3] = dic1["김향"][3] + (3000*cup)
        elif re == "향언":
            dic1["김향"][2] = dic1["김향"][2] + (3000*cup)
            dic1["김향"][3] = dic1["김향"][3] + (3000*cup)
        elif re == "향에":
            dic1["김향"][2] = dic1["김향"][2] + (3000*cup)
            dic1["김향"][3] = dic1["김향"][3] + (3000*cup)
        elif re == "향누":
            dic1["김향"][2] = dic1["김향"][2] + (3000*cup)
            dic1["김향"][3] = dic1["김향"][3] + (3000*cup)
        # 이름이 두 글자인 경우(김호)
        elif re == "호님":
            dic1["김호"][2] = dic1["김호"][2] + (3000*cup)
            dic1["김호"][3] = dic1["김호"][3] + (3000*cup)
        elif re == "호형":
            dic1["김호"][2] = dic1["김호"][2] + (3000*cup)
            dic1["김호"][3] = dic1["김호"][3] + (3000*cup)
        elif re == "호삼":
            dic1["김호"][2] = dic1["김호"][2] + (3000*cup)
            dic1["김호"][3] = dic1["김호"][3] + (3000*cup)
        elif re == "호오":
            dic1["김호"][2] = dic1["김호"][2] + (3000*cup)
            dic1["김호"][3] = dic1["김호"][3] + (3000*cup)
        elif re == "호에":
            dic1["김호"][2] = dic1["김호"][2] + (3000*cup)
            dic1["김호"][3] = dic1["김호"][3] + (3000*cup)
        # 이름이 두 글자인 경우(정설)
        elif re == "설님":
            dic1["정설"][2] = dic1["정설"][2] + (3000*cup)
            dic1["정설"][3] = dic1["정설"][3] + (3000*cup)
        elif re == "설형":
            dic1["정설"][2] = dic1["정설"][2] + (3000*cup)
            dic1["정설"][3] = dic1["정설"][3] + (3000*cup)
        elif re == "설삼":
            dic1["정설"][2] = dic1["정설"][2] + (3000*cup)
            dic1["정설"][3] = dic1["정설"][3] + (3000*cup)
        elif re == "설오":
            dic1["정설"][2] = dic1["정설"][2] + (3000*cup)
            dic1["정설"][3] = dic1["정설"][3] + (3000*cup)
        elif re == "설에":
            dic1["정설"][2] = dic1["정설"][2] + (3000*cup)
            dic1["정설"][3] = dic1["정설"][3] + (3000*cup)
            
            
        else:
            dic1[re][2] = dic1[re][2] + (3000*cup)
            dic1[re][3] = dic1[re][3] + (3000*cup)
            
    def d():
        l = 4
        for m in range(0, (len(i)-5), 2):
            l = l + m
            if i[l][0] == "베":
                dic1[ta][0] = dic1[ta][0] - (2500*int(i[l+1][0]))
                dic1[ta][3] = dic1[ta][3] - (2500*int(i[l+1][0]))
            
    
        
                
            
                    
    # 본격적으로 파일을 읽고 처리하는 부분시작.  ta는 선물주는 사람, re는 선물받는 사람 cup은 잔 수
    for i in f:
        i = i.split()
        count = 2
        # 1번 알고리즘(선물하는 경우)
        if ("선물합니다." in i) or ("선물부탁드립니다." in i):
            #여러명 나열할때(1-1)
            if "," in i:
                ta = i[0][2:4]
                
            # 별명과 본명이 다른 경우
                if ta == "지수":
                   cup = int(i[(len(i)-2)][0])
                   dic1["싸리"][1] = dic1["싸리"][1] - (3000*(i.count(",")+1)*cup)
                   dic1["싸리"][3] = dic1["싸리"][3] - (3000*(i.count(",")+1)*cup)
                   lots_give(i, dic1, cup, count)

                            
                elif ta == "주_":
                    cup = int(i[(len(i)-2)][0])
                    dic1["하루"][1] = dic1["하루"][1] - (3000*(i.count(",")+1)*cup)
                    dic1["하루"][3] = dic1["하루"][3] - (3000*(i.count(",")+1)*cup)
                    lots_give(i, dic1, cup, count)
                    
                    
                elif ta == "ag":   
                    cup = int(i[(len(i)-2)][0])
                    dic1["재순"][1] = dic1["재순"][1] - (3000*(i.count(",")+1)*cup)
                    dic1["재순"][3] = dic1["재순"][3] - (3000*(i.count(",")+1)*cup)
                    lots_give(i,dic1,cup,count)
                
                elif ta == "이빗":   
                    cup = int(i[(len(i)-2)][0])
                    dic1["데이빗"][1] = dic1["데이빗"][1] - (3000*(i.count(",")+1)*cup)
                    dic1["데이빗"][3] = dic1["데이빗"][3] - (3000*(i.count(",")+1)*cup)
                    lots_give(i, dic1, cup, count)
                    
                # 이름이 두 글자인 경우
                elif ta == "향]":
                    cup = int(i[(len(i)-2)][0])
                    dic1["김향"][1] = dic1["김향"][1] - (3000*(i.count(",")+1)*cup)
                    dic1["김향"][3] = dic1["김향"][3] - (3000*(i.count(",")+1)*cup)
                    lots_give(i, dic1, cup, count)
                    
                elif ta == "온]":
                    cup = int(i[(len(i)-2)][0])
                    dic1["규온"][1] = dic1["규온"][1] - (3000*(i.count(",")+1)*cup)
                    dic1["규온"][3] = dic1["규온"][3] - (3000*(i.count(",")+1)*cup)
                    lots_give(i, dic1, cup, count)
                
                elif ta == "호]":
                    cup = int(i[(len(i)-2)][0])
                    dic1["김호"][1] = dic1["김호"][1] - (3000*(i.count(",")+1)*cup)
                    dic1["김호"][3] = dic1["김호"][3] - (3000*(i.count(",")+1)*cup)
                    lots_give(i, dic1, cup, count)
                
                elif ta == "설]":
                    cup = int(i[(len(i)-2)][0])
                    dic1["정설"][1] = dic1["정설"][1] - (3000*(i.count(",")+1)*cup)
                    dic1["정설"][3] = dic1["정설"][3] - (3000*(i.count(",")+1)*cup)
                    lots_give(i, dic1, cup, count)
                    
                    
                    
                    
                

                
                
                        
            # 동명이인 구분
                elif ta == "미애":
                    if i[0][1] == "장":
                        cup = int(i[(len(i)-2)][0])
                        dic1["장미"][1] = dic1["장미"][1] - (3000*(i.count(",")+1)*cup)
                        dic1["장미"][3] = dic1["장미"][3] - (3000*(i.count(",")+1)*cup)
                        lots_give(i,dic1,cup,count)
                            
        
                    elif i[0][1] == "김":
                        cup = int(i[(len(i)-2)][0])
                        dic1["김미"][1] = dic1["김미"][1] - (3000*(i.count(",")+1)*cup)
                        dic1["김미"][3] = dic1["김미"][3] - (3000*(i.count(",")+1)*cup)
                        lots_give(i,dic1,cup,count)
                
                elif ta == "주현":
                    if i[0][1] == "이":
                        cup = int(i[(len(i)-2)][0])
                        dic1["이쭈"][1] = dic1["이쭈"][1] - (3000*(i.count(",")+1)*cup)
                        dic1["이쭈"][3] = dic1["이쭈"][3] - (3000*(i.count(",")+1)*cup)
                        lots_give(i,dic1,cup,count)
                        
                    elif i[0][1] == "오":
                        cup = int(i[(len(i)-2)][0])
                        dic1["오쭈"][1] = dic1["오쭈"][1] - (3000*(i.count(",")+1)*cup)
                        dic1["오쭈"][3] = dic1["오쭈"][3] - (3000*(i.count(",")+1)*cup)
                        lots_give(i,dic1,cup,count)
                        
                        
                        
                        
            # 그외 사람들
                else :
                    cup = int(i[(len(i)-2)][0])
                    dic1[ta][1] = dic1[ta][1] - (3000*(i.count(",")+1)*cup)
                    dic1[ta][3] = dic1[ta][3] - (3000*(i.count(",")+1)*cup)
                    lots_give(i,dic1,cup,count)
                        
                        
                    
                    
            # 섬김이들에게 선물할때(1-2)
            elif "섬김이분들께" in i:
                lst = input("섬김이들 이름을 입력하시오:") 
                lst = lst.split(" ")
                ta = i[0][2:4]
            # 별명과 본명이 다른 사람 구분
                if ta == "지수":                   
                   cup = int(i[(len(i)-2)][0])
                   dic1["싸리"][1] = dic1["싸리"][1] - (3000*cup*len(lst))
                   dic1["싸리"][3] = dic1["싸리"][3] - (3000*cup*len(lst))
                   for h in lst:
                       dic1[h][2] = dic1[h][2] + (3000*cup)
                       dic1[h][3] = dic1[h][3] + (3000*cup)
                
                elif ta == "주_":
                    cup = int(i[(len(i)-2)][0])
                    dic1["하루"][1] = dic1["하루"][1] - (3000*cup*len(lst))
                    dic1["하루"][3] = dic1["하루"][3] - (3000*cup*len(lst))
                    for h in lst:
                        dic1[h][2] = dic1[h][2] + (3000*cup)
                        dic1[h][3] = dic1[h][3] + (3000*cup)
                
                elif ta == "ag":
                    cup = int(i[(len(i)-2)][0])
                    dic1["재순"][1] = dic1["재순"][1] - (3000*cup*len(lst))
                    dic1["재순"][3] = dic1["재순"][3] - (3000*cup*len(lst))
                    for h in lst:
                        dic1[h][2] = dic1[h][2] + (3000*cup)
                        dic1[h][3] = dic1[h][3] + (3000*cup)
                
                elif ta == "이빗":
                    cup = int(i[(len(i)-2)][0])
                    dic1["데이빗"][1] = dic1["데이빗"][1] - (3000*cup*len(lst))
                    dic1["데이빗"][3] = dic1["데이빗"][3] - (3000*cup*len(lst))
                    for h in lst:
                        dic1[h][2] = dic1[h][2] + (3000*cup)
                        dic1[h][3] = dic1[h][3] + (3000*cup)
                        
            # 이름이 두 글자인 경우
                elif ta == "향]":
                    cup = int(i[(len(i)-2)][0])
                    dic1["김향"][1] = dic1["김향"][1] - (3000*cup*len(lst))
                    dic1["김향"][3] = dic1["김향"][3] - (3000*cup*len(lst))
                    for h in lst:
                        dic1[h][2] = dic1[h][2] + (3000*cup)
                        dic1[h][3] = dic1[h][3] + (3000*cup)
                elif ta == "온]":
                    cup = int(i[(len(i)-2)][0])
                    dic1["규온"][1] = dic1["규온"][1] - (3000*cup*len(lst))
                    dic1["규온"][3] = dic1["규온"][3] - (3000*cup*len(lst))
                    for h in lst:
                        dic1[h][2] = dic1[h][2] + (3000*cup)
                        dic1[h][3] = dic1[h][3] + (3000*cup)
                elif ta == "호]":
                    cup = int(i[(len(i)-2)][0])
                    dic1["김호"][1] = dic1["김호"][1] - (3000*cup*len(lst))
                    dic1["김호"][3] = dic1["김호"][3] - (3000*cup*len(lst))
                    for h in lst:
                        dic1[h][2] = dic1[h][2] + (3000*cup)
                        dic1[h][3] = dic1[h][3] + (3000*cup)
                elif ta == "설]":
                    cup = int(i[(len(i)-2)][0])
                    dic1["정설"][1] = dic1["정설"][1] - (3000*cup*len(lst))
                    dic1["정설"][3] = dic1["정설"][3] - (3000*cup*len(lst))
                    for h in lst:
                        dic1[h][2] = dic1[h][2] + (3000*cup)
                        dic1[h][3] = dic1[h][3] + (3000*cup)
                    
                 
                    
                    
                        
                                   
            # 동명이인 구분 
                elif ta == "미애":
                    if i[0][1] == "장":
                        cup = int(i[(len(i)-2)][0])
                        dic1["장미"][1] = dic1["장미"][1] - (3000*cup*len(lst))
                        dic1["장미"][3] = dic1["장미"][3] - (3000*cup*len(lst))
                        for h in lst:
                            dic1[h][2] = dic1[h][2] + (3000*cup)
                            dic1[h][3] = dic1[h][3] + (3000*cup)
                    
                    elif i[0][1] == "김":
                        cup = int(i[(len(i)-2)][0])
                        dic1["김미"][1] = dic1["김미"][1] - (3000*cup*len(lst))
                        dic1["김미"][3] = dic1["김미"][3] - (3000*cup*len(lst))
                        for h in lst:
                            dic1[h][2] = dic1[h][2] + (3000*cup)
                            dic1[h][3] = dic1[h][3] + (3000*cup)              
                elif ta == "주현":
                    if i[0][1] == "이":
                        cup = int(i[(len(i)-2)][0])
                        dic1["이쭈"][1] = dic1["이쭈"][1] - (3000*cup*len(lst))
                        dic1["이쭈"][3] = dic1["이쭈"][3] - (3000*cup*len(lst))
                        for h in lst:
                            dic1[h][2] = dic1[h][2] + (3000*cup)
                            dic1[h][3] = dic1[h][3] + (3000*cup)
                    
                    elif i[0][1] == "오":
                        cup = int(i[(len(i)-2)][0])
                        dic1["오쭈"][1] = dic1["오쭈"][1] - (3000*cup*len(lst))
                        dic1["오쭈"][3] = dic1["오쭈"][3] - (3000*cup*len(lst))
                        for h in lst:
                            dic1[h][2] = dic1[h][2] + (3000*cup)
                            dic1[h][3] = dic1[h][3] + (3000*cup)
                        
                        
            # 그외 사람들 
                else :
                    cup = int(i[(len(i)-2)][0])
                    dic1[ta][1] = dic1[ta][1] - (3000*cup*len(lst))
                    dic1[ta][3] = dic1[ta][3] - (3000*cup*len(lst))
                    for h in lst:
                        dic1[h][2] = dic1[h][2] + (3000*cup)
                        dic1[h][3] = dic1[h][3] + (3000*cup)
                        
                    
                    
                
            # 한명에게 선물하는 경우(1-3) 
            elif "섬김이분들께" not in i:
                re = i[(len(i)-4)][0:2]
                cup = int(i[(len(i)-2)][0])
                ta = i[0][2:4]
            # 별명과 본명이 다른 사람 구분
                if ta == "지수":   
                   dic1["싸리"][1] = dic1["싸리"][1] - (cup*3000) 
                   dic1["싸리"][3] = dic1["싸리"][3] - (cup*3000)
                   one_give(re, dic1, i, cup)
                   
                    

                elif ta == "주_":
                    dic1["하루"][1] = dic1["하루"][1] - (cup*3000) 
                    dic1["하루"][3] = dic1["하루"][3] - (cup*3000)
                    one_give(re,dic1,i,cup)
 
                    
                    
                elif ta == "루나":
                    dic1["하루나"][1] = dic1["하루나"][1] - (cup*3000) 
                    dic1["하루나"][3] = dic1["하루나"][3] - (cup*3000)
                    one_give(re,dic1,i,cup)

                    
                elif ta == "경현":
                    dic1["까루나"][1] = dic1["까루나"][1] - (cup*3000) 
                    dic1["까루나"][3] = dic1["까루나"][3] - (cup*3000) 
                    one_give(re,dic1,i,cup)
                    
                elif ta == "ag":
                    dic1["재순"][1] = dic1["재순"][1] - (cup*3000) 
                    dic1["재순"][3] = dic1["재순"][3] - (cup*3000) 
                    one_give(re,dic1,i,cup)
                        
                elif ta == "이빗":
                    dic1["데이빗"][1] = dic1["데이빗"][1] - (cup*3000) 
                    dic1["데이빗"][3] = dic1["데이빗"][3] - (cup*3000) 
                    one_give(re,dic1,i,cup)
            
            # 이름이 두 글자인 경우
                elif ta == "향]":
                    dic1["김향"][1] = dic1["김향"][1] - (cup*3000) 
                    dic1["김향"][3] = dic1["김향"][3] - (cup*3000) 
                    one_give(re,dic1,i,cup)
                elif ta == "온]":
                    dic1["규온"][1] = dic1["규온"][1] - (cup*3000) 
                    dic1["규온"][3] = dic1["규온"][3] - (cup*3000) 
                    one_give(re,dic1,i,cup)
                elif ta == "호]":
                    dic1["김호"][1] = dic1["김호"][1] - (cup*3000) 
                    dic1["김호"][3] = dic1["김호"][3] - (cup*3000) 
                    one_give(re,dic1,i,cup)
                elif ta == "설]":
                    dic1["정설"][1] = dic1["정설"][1] - (cup*3000) 
                    dic1["정설"][3] = dic1["정설"][3] - (cup*3000) 
                    one_give(re,dic1,i,cup)
                    
                    
                    
                    
                

                     
                     
            # 동명이인 구분       
                elif ta == "미애":
                    if i[0][1] == "장":
                        dic1["장미"][1] = dic1["장미"][1] - (cup*3000) 
                        dic1["장미"][3] = dic1["장미"][3] - (cup*3000)
                        one_give(re,dic1,i,cup)
                        
                    if i[0][1] == "김":
                        dic1["김미"][1] = dic1["김미"][1] - (cup*3000) 
                        dic1["김미"][3] = dic1["김미"][3] - (cup*3000) 
                        one_give(re,dic1,i,cup)
                        
                
                elif ta == "주현":
                    if i[0][1] == "이":
                        dic1["이쭈"][1] = dic1["이쭈"][1] - (cup*3000) 
                        dic1["이쭈"][3] = dic1["이쭈"][3] - (cup*3000)
                        one_give(re,dic1,i,cup)
                        
                    if i[0][1] == "오":
                        dic1["오쭈"][1] = dic1["오쭈"][1] - (cup*3000) 
                        dic1["오쭈"][3] = dic1["오쭈"][3] - (cup*3000) 
                        one_give(re,dic1,i,cup)
                    
                    
            # 그외 사람들
                else:
                    dic1[ta][1] = dic1[ta][1] - (cup*3000) 
                    dic1[ta][3] = dic1[ta][3] - (cup*3000) 
                    one_give(re, dic1, i, cup)
                    
   
        # 2번 알고리즘(주문하는 경우)
        elif ("부탁드립니다." in i) or ("먹었습니다." in i) or ("주문합니다." in i) or ("부탁합니다." in i) or ("신청합니다."in i) or ("부탁드려요^^"in i) or ("부탁드려요"in i):
            menu = i[(len(i)-3)]
            cup = int(i[(len(i)-2)][0])
            ta = i[0][2:4]
            # 별명으로 부르는 경우
            if ta == "지수":
                if menu[0] == "베":
                    dic1["싸리"][0] = dic1["싸리"][0] - (2500*cup)
                    dic1["싸리"][3] = dic1["싸리"][3] - (2500*cup)
                   
            elif ta == "주_":
                if menu[0] == "베":
                    dic1["하루"][0] = dic1["하루"][0] - (2500*cup)
                    dic1["하루"][3] = dic1["하루"][3] - (2500*cup)
            
            elif ta == "루나":
                if menu[0] == "베":
                    dic1["하루나"][0] = dic1["하루나"][0] - (2500*cup)
                    dic1["하루나"][3] = dic1["하루나"][3] - (2500*cup)
                   
            elif ta == "경현":
                if menu[0] == "베":
                    dic1["까루나"][0] = dic1["까루나"][0] - (2500*cup)
                    dic1["까루나"][3] = dic1["까루나"][3] - (2500*cup)
            
            elif ta == "디 ":
                if menu[0] == "베":
                    dic1["단디"][0] = dic1["단디"][0] - (2500*cup)
                    dic1["단디"][3] = dic1["단디"][3] - (2500*cup)
            
            elif ta == "ag":
                if menu[0] == "베":
                    dic1["재순"][0] = dic1["재순"][0] - (2500*cup)
                    dic1["재순"][3] = dic1["재순"][3] - (2500*cup)
                    
            elif ta == "이빗":
                if menu[0] == "베":
                    dic1["데이빗"][0] = dic1["데이빗"][0] - (2500*cup)
                    dic1["데이빗"][3] = dic1["데이빗"][3] - (2500*cup)
        
        # 이름이 두 글자인 경우
            elif ta == "향]":
                if menu[0] == "베":
                    dic1["김향"][0] = dic1["김향"][0] - (2500*cup)
                    dic1["김향"][3] = dic1["김향"][3] - (2500*cup)
            elif ta == "온]":
                if menu[0] == "베":
                    dic1["규온"][0] = dic1["규온"][0] - (2500*cup)
                    dic1["규온"][3] = dic1["규온"][3] - (2500*cup)
            elif ta == "호]":
                if menu[0] == "베":
                    dic1["김호"][0] = dic1["김호"][0] - (2500*cup)
                    dic1["김호"][3] = dic1["김호"][3] - (2500*cup)
            elif ta == "설]":
                if menu[0] == "베":
                    dic1["정설"][0] = dic1["정설"][0] - (2500*cup)
                    dic1["정설"][3] = dic1["정설"][3] - (2500*cup)
                    
                    
            elif ta == "미애":
                    if i[0][1] == "장":
                        if menu[0] == "베":
                            dic1["장미"][0] = dic1["장미"][0] - (cup*2500) 
                            dic1["장미"][3] = dic1["장미"][3] - (cup*2500)
                        
                        
                    if i[0][1] == "김":
                        if menu[0] == "베":
                            dic1["김미"][0] = dic1["김미"][0] - (cup*2500) 
                            dic1["김미"][3] = dic1["김미"][3] - (cup*2500)
                            
                            
            elif ta == "주현":
                    if i[0][1] == "이":
                        if menu[0] == "베":
                            dic1["이쭈"][0] = dic1["이쭈"][0] - (cup*2500) 
                            dic1["이쭈"][3] = dic1["이쭈"][3] - (cup*2500)
                        
                        
                    if i[0][1] == "오":
                        if menu[0] == "베":
                            dic1["오쭈"][0] = dic1["오쭈"][0] - (cup*2500) 
                            dic1["오쭈"][3] = dic1["오쭈"][3] - (cup*2500)
                        
                        
                    
            else:
                if menu[0] == "베":
                    dic1[ta][0] = dic1[ta][0] - (2500*cup)
                    dic1[ta][3] = dic1[ta][3] - (2500*cup)
                    
            
            
                        
            
            
                    
            
        
                            
        
        # 3번 알고리즘(주문하는 경우)
        elif i != []:
            if (i[len(i)-1]) in ["1", "2", "3", "4", "5"]:
                # 다른사람이름 달고 먹을때(3-1)
                if i[3] in dic1.keys():
                    ta = i[3]
                    l = 2
                    for m in range(0, (len(i)-5), 2):
                        l = l + 2
                        if i[l][0] == "베":
                            dic1[ta][0] = dic1[ta][0] - (2500*int(i[l+1][0]))
                            dic1[ta][3] = dic1[ta][3] - (2500*int(i[l+1][0]))
                        # 메뉴적기
                # 본인이름으로 먹을떄(3-2)
                else:
                    ta = i[0][2:4]
                    # 별명이랑 본명이랑 다른 사람
                    if ta == "지수":
                        l = 1
                        for m in range(0, (len(i)-3), 2):
                            l = l + 2
                            if i[l][0] == "베":
                                dic1["싸리"][0] = dic1["싸리"][0] - (2500*int(i[l+1][0]))
                                dic1["싸리"][3] = dic1["싸리"][3] - (2500*int(i[l+1][0]))
                            
                        # 메뉴적기
                    
                    
                    elif ta == "주_":
                        l = 1
                        for m in range(0, (len(i)-3), 2):
                            l = l + 2
                            if i[l][0] == "베":
                                dic1["하루"][0] = dic1["하루"][0] - (2500*int(i[l+1][0]))
                                dic1["하루"][3] = dic1["하루"][3] - (2500*int(i[l+1][0]))
                                
                                '''
                                예외들 적어야 한다..
                                '''
                                
                                
                    
                    # 그외 사람들
                    else:
                        l = 1
                        for m in range(0, (len(i)-3), 2):
                            l = l + 2
                            if i[l][0] == "베":
                                dic1[ta][0] = dic1[ta][0] - (2500*int(i[l+1][0]))
                                dic1[ta][3] = dic1[ta][3] - (2500*int(i[l+1][0]))
                       
                        
            
                
    # 행렬표를 만들기 위해, 딕셔너리형태에서 이차원리스트형태로.
    c = [["이름", "먹은", "선물한", "선물받은", "합산"]]
    d = []
    for name, money in dic1.items():
        d.append(name)
        d.extend(money)
        c.append(d)
        d = []
    
    
    # 표를 보여준다.
    df = pd.DataFrame(c) # e{at)는 먹은금액, g(vie)는 준선물, r(ecieve)은 받은선물, s(sum)는 정산결과
    print(df)
    
     
with open("doo/공감.csv", "w", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerows(c)
    