import pickle
profile_file =open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile 에 있는 정보를 file 에 저장
profile_file.close()


profile_file =open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
    
    
with open("study.txt", "w", encoding="utf8 ") as study_file:
    study_file.write("파이썬 예제 중")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
    

for i in range(1, 51):
    #with open("I:\\dev\\git\\python\\python1\\report\\"+str(i) + "주차.txt", "w", encoding="utf8") as report_file:
    with open(".\\python1\\report\\"+str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")
        