from konlpy.tag import Okt
from data import data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,jansu,dic_name,menu,zumun,dic_num,menu_list,name_tuple
import os
import konlpy
import zipfile
import pandas as pd
import openpyxl
import csv

for i in range(2):  # 마지막엔 해당 파일을 삭제 해야한다..
    konlpy_path = os.path.dirname(konlpy.__file__)
    java_path = os.path.join(konlpy_path, "java")
    os.chdir(java_path)
    os.getcwd()
        
    jar_file_path = 'open-korean-text-2.1.0.jar'
        
    with zipfile.ZipFile(jar_file_path, 'r') as jar:
        jar.extractall()
            
    with open("C:/Users/djdjd/AppData/Local/Programs/Python/Python312/Lib/site-packages/konlpy/java/org/openkoreantext/processor/util/noun/names.txt", "r", encoding="UTF-8") as f:
        data = f.read()
    
    data += data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + jansu + menu + data11
        
    with open("C:/Users/djdjd/AppData/Local/Programs/Python/Python312/Lib/site-packages/konlpy/java/org/openkoreantext/processor/util/noun/names.txt", 'w', encoding="UTF-8") as f:
        f.write(data)
    data

okt = Okt()

eat_sum = {"sum" : 0}

def menu_fun(m): # main처럼 함수로 만들기.
    money = (m*cup)
    eat_sum["sum"] += money
    while money > 0:
        if dic_name[ta][4] > 0:
            dic_name[ta][4] -= 100
            dic_name[ta][1] += 100
            money -= 100
        elif dic_name[ta][4] == 0:
            dic_name[ta][0] += 100
            dic_name[ta][1] += 100
            money -= 100
                      


def menu_all():
    if i_menu == "베리고":
        menu_fun(4000)
    elif i_menu == "에스프레소":
        menu_fun(2500)
    elif i_menu == "뜨아":
        menu_fun(2500)
    elif i_menu == "따아":
        menu_fun(2500)
    elif i_menu == "아아":
        menu_fun(2500)
    elif i_menu == "아메리카노":
        menu_fun(2500)
    elif i_menu == "아메":
        menu_fun(2500)
    elif i_menu == "라떼":
        menu_fun(3000)
    elif i_menu == "따라":
        menu_fun(3000)
    elif i_menu == "아라":
        menu_fun(3000)
    elif i_menu == "카페라떼":
        menu_fun(3000)
    elif i_menu == "카푸치노":
        menu_fun(3000)
    elif i_menu == "바닐라라떼":
        menu_fun(3500)
    elif i_menu == "아바라":
        menu_fun(3500)
    elif i_menu == "카페모카":
        menu_fun(3500)
    elif i_menu == "더치":
        menu_fun(3500)
    elif i_menu == "콜드브루":
        menu_fun(3000)
    elif i_menu == "더치라떼":
        menu_fun(4000)
    elif i_menu == "보리커피":
        menu_fun(2500)
    elif i_menu == "탄산수":
        menu_fun(500)
    elif i_menu == "탄산":
        menu_fun(500)
    elif i_menu == "밀크티":
        menu_fun(3000)
    elif i_menu == "딸기라떼":
        menu_fun(3500)
    elif i_menu == "캐모마일":
        menu_fun(2500)
    elif i_menu == "루이보스":
        menu_fun(2500)
    elif i_menu == "보이차":
        menu_fun(2500)
    elif i_menu == "페퍼민트":
        menu_fun(2500)
    elif i_menu == "레몬그라스":
        menu_fun(2500)
    elif i_menu == "라벤더":
        menu_fun(2500)
    elif i_menu == "차":
        menu_fun(2500)
    elif i_menu == "티":
        menu_fun(2500)
    elif i_menu == "아이스크림":
        menu_fun(2500)
    elif i_menu == "녹차아이스크림":
        menu_fun(2500)
    elif i_menu == "맥주":
        menu_fun(3000)
    elif i_menu == "제주누보":
        menu_fun(3000)
    elif i_menu == "누보":
        menu_fun(3000)
    elif i_menu == "아바":
        menu_fun(3500)
    elif i_menu == "아보바나나":
        menu_fun(3500)
    elif i_menu == "아보카도":
        menu_fun(3500)
    elif i_menu == "미숫가루":
        menu_fun(3500)
    elif i_menu == "망고":
        menu_fun(4000)
    elif i_menu == "망스":
        menu_fun(4000)
    elif i_menu == "망바":
        menu_fun(4000)
    elif i_menu == "아포카도":
        menu_fun(4000)
    elif i_menu == "아포카토":
        menu_fun(4000)
    elif i_menu == "아인슈페너":
        menu_fun(4000)
    elif i_menu == "포춘쿠키":
        menu_fun(1000)
    elif i_menu == "포츈쿠키":
        menu_fun(1000)
    elif i_menu == "포춘":
        menu_fun(1000)
    elif i_menu == "포츈":
        menu_fun(1000)
    elif i_menu == "민트초코라떼":
        menu_fun(4000)
    elif i_menu == "민트초코":
        menu_fun(4000)
    elif i_menu == "민초라떼":
        menu_fun(4000)
    elif i_menu == "민초라":
        menu_fun(4000)
    elif i_menu == "초코민트라떼":
        menu_fun(4000)
    elif i_menu == "초코민트":
        menu_fun(4000)       
    elif i_menu == "초민라":
        menu_fun(4000)
    elif i_menu == "페퍼민트라떼":
        menu_fun(4000)
    elif i_menu == "페퍼민트":
        menu_fun(4000)
    elif i_menu == "페민라":
        menu_fun(4000)
    elif i_menu == "스피아민트라떼":
        menu_fun(4000)
    elif i_menu == "스피아민트":
        menu_fun(4000)
    elif i_menu == "스민라":
        menu_fun(4000)
    elif i_menu == "애플민트스무디":
        menu_fun(3500)
    elif i_menu == "쌍화탕":
        menu_fun(1700)
    elif i_menu == "보약":
        menu_fun(1700)
    elif i_menu == "아사히":
        menu_fun(3000)
    elif i_menu == "아사이":
        menu_fun(3000)
    elif i_menu == "드립":
        menu_fun(4000)
    elif i_menu == "섭":
        menu_fun(4000)
    elif i_menu == "패션후르츠에이드":
        menu_fun(3500)
    elif i_menu == "레몬에이드":
        menu_fun(3500)
    elif i_menu == "복바에이드":
        menu_fun(3500)
    elif i_menu == "복숭아에이드":
        menu_fun(3500)
    elif i_menu == "복숭아바질에이드":
        menu_fun(3500)
    elif i_menu == "하이볼":
        menu_fun(5000)
    elif i_menu == "브륄레":
        menu_fun(3000)
    elif i_menu == "브릴레":
        menu_fun(3000)
    elif i_menu == "로즈마리라떼":
        menu_fun(4000)
    elif i_menu == "로즈마리":
        menu_fun(4000)
    elif i_menu == "꼼빠냐":
        menu_fun(3500)
    elif i_menu == "비건":
        menu_fun(2000)
    elif i_menu == "튀일":
        menu_fun(2000)
    elif i_menu == "튀일쿠키":
        menu_fun(2000)
    elif i_menu == "트윌":
        menu_fun(2000)
    elif i_menu == "아몬드":
        menu_fun(2000)
    elif i_menu == "수제":
        menu_fun(2000)
    elif i_menu == "트윌쿠키":
        menu_fun(2000)
    elif i_menu == "유자민트":
        menu_fun(4000)
    elif i_menu == "유자민트티":
        menu_fun(4000)                  # 우유, 오트 체크
    elif i_menu == "모히또":
        menu_fun(5000)
    elif i_menu == "모히토":
        menu_fun(5000)
    elif i_menu == "샹그리아":
        menu_fun(5000)
    elif i_menu == "깔루아밀크":
        menu_fun(5000)
    elif i_menu == "칼루아밀크":
        menu_fun(5000)
    elif i_menu == "잭콜":
        menu_fun(5000)
    elif i_menu == "잭콕":
        menu_fun(5000)
    elif i_menu == "안주":
        menu_fun(3000)
    

    
        
    
    
# 초코 관련 메뉴 추가. 샷추가. 오트추가
    
    
    
    
if __name__ == "__main__":
    # 메인 문장 시작(텍스트 파일을 읽는다.)
    with open("C:/Users/djdjd/Desktop/파이널 공감.txt", "r", encoding="UTF-8") as f:
        text = f.read().split()
        b = ""
        for i in text:
            b = b + " " + i
        # 단락구분가능
        b = b.split(" [") # 먼저 텍스트 파일에서 ] [ 이걸 ][로 바꿔줘야 한다 !
    
        # 문장 진짜 시작.
        for filt_b in b:
            pos_tags = okt.pos(filt_b)
            result = [word for word, pos in pos_tags if pos in ["Noun", "Josa", "Number", "Verb"]]
            ta = result[0]
            result.pop(0)
            print(ta, result)
        # 일반적으로 선물 주는 경우
            if ("에게" in result) and ("선물" in result):
            
            # 갯수 체크(수량 잡기)
                for cup in result:
                    if cup in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔"]:
                        num1 = dic_num[cup]
                        break
                    elif cup in ["1", "2", "3", "4", "5", "6", "7"]:
                        if (result.index(cup) < result.index("선물")) and (result.index(cup) > result.index("에게")): # 선물하는 경우에서, 다른 숫자들이 나오면 안된다..ex) 22기 졸업생
                            num1 = dic_num[cup]
                            break
                    else:
                        num1 = 1
                    
                # 이름 중복 제외
                result = set(result)
                result = list(result)
                    
                # 준 사람 & 받은 사람
                count = 0
                for rec in result:
                    
                    if rec in dic_name.keys() :
                        count += 1
                        # 받는 사람
                        if dic_name[rec][0] > 0:
                            money = num1 * 3000
                            while money > 0:
                                if dic_name[rec][0] > 0:
                                    dic_name[rec][0] -= 100
                                    dic_name[rec][3] += 100
                                    money -= 100
                                elif dic_name[rec][0] == 0:
                                    dic_name[rec][4] += 100
                                    dic_name[rec][3] += 100
                                    money -= 100
                        elif dic_name[rec][0] == 0:
                            dic_name[rec][4] += num1 * 3000
                            dic_name[rec][3] += num1 * 3000
            
                # 준 사람
                dic_name[ta][2] += (num1 * count * 3000)
                money = (num1 * count * 3000)
                while money > 0:
                    if dic_name[ta][4] > 0:
                        dic_name[ta][4] -= 100
                        money -= 100
                    elif dic_name[ta][4] == 0:
                        dic_name[ta][0] += 100
                        money -= 100
            
            
            # 주문 맨트 없는 주문(끝이 숫자로 끝나는 경우)
            elif result[len(result)-1] in ["1", "2", "3", "4", "5", "6", "7"]:
                try:
                    list(set(result)&set(menu_list)).pop(0)
                except IndexError:
                    pass
                # 메뉴를 시킨 경우라고 의심가능 상황
                else:
                    try:
                        list(set(result)&set(dic_name.keys())).pop(0)  # 여러개의 리스트 원소들중, 여러개 원소가 들어 있는 리스트간의 교집합.
                    except IndexError:
                        print("자기 이름으로 먹는 경우")
                        for i in result:
                            if i in menu_list:
                                i_menu = i
                            elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7", "8","9","10"]:
                                cup = dic_num[i]
                                menu_all()
                                    
                    else:
                        print("다른 사람이름으로 먹는경우")
                        for i in result:
                            if i in dic_name.keys():
                                ta = i
                            elif i in menu_list:
                                i_menu = i
                            elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7","8","9","10"]:
                                cup = dic_num[i]
                                menu_all()
                                
            # 주문 맨트가 있는 주문              
            else:
                try:
                    list(set(result)&set(zumun)).pop(0) in zumun
                except IndexError:
                    pass
                else:
                    try:
                        list(set(result)&set(dic_name.keys())).pop(0)
                    except IndexError:
                        print("자기이름으로")
                        for i in result:
                            if i in menu_list:
                                i_menu = i
                            elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7","8","9","10"]:
                                cup = dic_num[i]
                                menu_all()
                    else:
                        print("남의 이름으로")
                        for i in result:
                            if i in dic_name.keys():
                                ta = i
                            elif i in menu_list:
                                i_menu = i
                            elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7","8","9","10"]:
                                cup = dic_num[i]
                                menu_all()
                                
        
        
    # 이름 합치기(오세현과 세현 하나로 합치기)
    for first, second in name_tuple:
        if (dic_name[second][4] != 0) and (dic_name[first+second][0] != 0):
            last = dic_name[first+second][0]
            while last > 0:
                if dic_name[second][4] > 0:
                    dic_name[second][4] -= 100
                    last -= 100
                elif dic_name[second][4] == 0:
                    dic_name[second][0] += 100
                    last -= 100
            dic_name[second][1] += dic_name[first+second][1]
            dic_name[second][2] += dic_name[first+second][2]
            dic_name[second][3] += dic_name[first+second][3]
            dic_name[first+second] = [0, 0, 0, 0, 0]
    
        elif (dic_name[first+second][4] != 0) and (dic_name[second][0] != 0):
            last = dic_name[second][0]
            while last > 0:
                if dic_name[first+second][4] > 0:
                    dic_name[first+second][4] -= 100
                    last -= 100
                elif dic_name[first+second][4] == 0:
                    dic_name[first+second][0] += 100
                    last -= 100
            dic_name[second][0] = dic_name[first+second][0]
            dic_name[second][4] = dic_name[first+second][4]
            dic_name[second][1] += dic_name[first+second][1]
            dic_name[second][2] += dic_name[first+second][2]
            dic_name[second][3] += dic_name[first+second][3]
            dic_name[first+second] = [0 ,0 ,0 ,0 ,0] # 성이 붙은 것은 초기화.
    
        else:
            dic_name[second][0] += dic_name[first+second][0]
            dic_name[second][1] += dic_name[first+second][1]
            dic_name[second][2] += dic_name[first+second][2]
            dic_name[second][3] += dic_name[first+second][3]
            dic_name[second][4] += dic_name[first+second][4]
            dic_name[first+second] = [0, 0, 0, 0, 0]

# dic_name에서 필요한 이름만 거르기
    dic_name_filt = {}
    count = 0  
    for key, value in dic_name.items():
        if count < 167:
            dic_name_filt[key] = value
            count += 1
        else:
            break
    
    
# 공감 excel에 추가.
    file_path = "C:/Users/djdjd/Desktop/카페_7월.xlsx"
    workbook = openpyxl.load_workbook(file_path, data_only=True)
    sheet = workbook["정산"]
    
    
    num = 5
    for name, money in dic_name_filt.items():
        num += 1
        num = str(num)
        if money[0] > 0:
            if sheet["N"+num].value > 0:
                money1 = money[0]
                while money1 > 0:
                    if sheet["N"+num].value > 0:
                        sheet["N"+num].value -= 100
                        money1 -= 100
                    elif sheet["N"+num].value == 0:
                        sheet["F"+num].value += 100
                        money1 -= 100
            else:
                sheet["F"+num].value += money[0]
                
        if money[1] > 0:
            sheet["H"+num].value += money[1]
        
        if money[2] > 0:
            sheet["I"+num].value += money[2]
            
        if (money[1] > 0) or (money[2] > 0):
            sheet["J"+num].value += (money[1] + money[2])
        
        if money[3] > 0:
            sheet["K"+num].value += money[3]
            
        if money[4] > 0:
            sheet["N"+num].value += money[4]
        
        sheet["L"+num].value = sheet["F"+num].value
            
        num = int(num)
    
    workbook.save(file_path)
    
    # csv파일 만들기
    c = [["이름", "내야할돈", "먹은", "선물한", "선물받은", "남은선물"]]
    d = []
    for name, money in dic_name_filt.items():
        d.append(name)
        d.extend(money)
        c.append(d)
        d = []
    df = pd.DataFrame(c, columns=["이름", "내야할", "먹은금액", "선물한", "선물받은",  "남은선물"])
    
    with open("C:/Users/djdjd/Desktop/Python/python_cafe/cafe_data.csv", "w", encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerows(c)
    
    
    # 페이제외, 먹은 액수와 선물한 액수의 합 
    print(f"페이제외,eat의 합은 {eat_sum["sum"]}입니다.")
            
            
           
                    

        











                


            