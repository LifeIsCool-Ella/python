print("Python", "Java","JavaScript", sep=",")
print("Python", "Java","JavaScript", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys 
print("Python", "Java", file=sys.stdout)
print("python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #왼쪽정렬, 오른쪽정렬
    
for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3))    # 공백 0으로 채우기
    

#표준입력
#answer = input("아무 값이나 입력하세요 : ")    
#answer = 19 
#print(type(answer))
#print("입력하신 값은 "+ answer + " 입니다. ")

# 빈 자리는 빈공간으로 두고 , 오른쪽 정렬, 총 10자리 공간 확보 
print("{0: >10}".format(500))

# 양수 일 땐 + 로 표시, 음수 일때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸 _
print("{0:_<+10}".format(500))

# 3자리 마다 콤마
print("{0:,}".format(1000000000000000000))

# 3자리 마다 콤마, +- 부호 붙이기 
print("{0:+,}".format(-1000000000000000000))

# 3자리마다 콤마, 부호, 자리수
print("{0:^<+30,}".format(100000000000000))

print("{0:^>+30,}".format(100000000000000))
print("{0:^>30,}".format(100000000000000))

#소수점
print("{0:f}".format(5/3))

#소수점 특정 자리수까지 
print("{0:.2f}".format(5/3))
