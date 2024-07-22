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
answer = input("아무 값이나 입력하세요 : ")    
#answer = 19 
print(type(answer))
print("입력하신 값은 "+ answer + " 입니다. ")
