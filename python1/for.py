print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0,1,2,3,4] :
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(5) :
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(1, 6) :
    print("대기번호 : {0}".format(waiting_no)) 
    
starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다. ".format(customer))    
    
#while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요. ".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")
        
#customer = "아이언맨"     
#index = 1    
#while True:
#    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요. ".format(customer, index))
#    index +=1

customer = "토르"
person = "Unknown"

while person != customer : 
    print("{0}, 커피가 준비되었습니다. ".format(customer))
    person = input("이름이 어떻게 되세요? ")
    
absent = [2, 5] # 결석
no_book = [7] #책을 깜빡했음
for student in range(1, 11) : # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
    
    