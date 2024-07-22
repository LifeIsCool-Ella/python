#전역변수, 지역변수 
gun = 10 

def checkpoint(soldiers):
    global gun 
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))    
checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

#표준체중

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175 
gender = "남자"
weight = round(std_weight(height/ 100 , gender) , 2) 
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))