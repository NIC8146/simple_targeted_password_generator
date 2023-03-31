import time
print("\033[0;33m starting password genrator \033[0m")
time.sleep(2)
name = input("\033\n[0;33m Enter first name of target : \033[0m")
lastName = input("\033[0;33m Enter last name of target : \033[0m")
petName = input("\033[0;33m Enter name of pet or target : \033[0m")
nickName = input("\033[0;33m Enter nick name of target : \033[0m")
fatherName = input("\033[0;33m Enter father's name of target : \033[0m")
motherName = input("\033[0;33m Enter mothers's name of target : \033[0m")

dobcheck = True

while dobcheck:
    dob = input("\033[0;33m Enter date of birth of target (DDMMYYYY) or enter \033[0;34mno\033[0;33m if there is no info about date of brith : \033[0m")
    if dob != "no":
        if (len(dob)==8 and dob.isnumeric()):
            current_year=time.localtime().tm_year
            current_month=time.localtime().tm_mon
            current_date=time.localtime().tm_mday
            birthDate = dob[0:2]
            birthMonth = dob[2:4]
            birthYear = dob[4:]
            if current_month > birthMonth:
                age=str(current_year-(int(birthYear)))
            elif current_month == birthMonth:   
                if current_date >= birthDate:
                    age=str(current_year-(int(birthYear)))
                else:
                    age=str(current_year-(int(birthYear))-1)
            else:
                age=str(current_year-(int(birthYear))-1)
            dobcheck = False
        else:
            print("\033[0;31m date of birth of target you have given is incorrect /n it shouldd in format DDMMYYYY \033[0m ")
    else:
        birthDate = ""
        birthMonth = ""
        birthYear = ""
        age=""
        dobcheck = False

partner = input("\033[0;33m is any information about target's partner ? (yes/no) : \033[0m ")

if partner == "yes":
    partnerName = input("\033[0;33m Enter name of target's : \033[0m")
    partnerNick = input("\033[0;33m Enter nick name of target's partner : \033[0m")
    partnerdobcheck = True
    while partnerdobcheck:
        partnerdob = input("\033[0;33m Enter birth date of target's partner (DDMMYYYY) or enter \033[0;34mno\033[0;33m if there is no info about date of brith : \033[0m")
        if partnerdob=="no":
            if len(partnerdob)==8 and partnerdob.isnumeric():
                partnerbirthDate = partnerdob[0:2]
                partnerbirthMonth = partnerdob[2:4]
                partnerbirthYear = partnerdob[4:]
                partnerdobcheck = False
            else:
                print("\033[0;31m date of birth of target's partner you have given is incorrect /n it shouldd in format DDMMYYYY \033[0m ")
        else:
            partnerbirthDate = ""
            partnerbirthMonth = ""
            partnerbirthYear = ""
            partnerdobcheck = False
else:
    partnerName = ""
    partnerNick = ""
    partnerbirthDate = ""
    partnerbirthMonth = ""
    partnerbirthYear = ""



children = input("\033[0;33m is any information about target's children ? (yes/no) : \033[0m ")
if children == "yes":
    childCount=int(input("\033[0;33m Enter number of children : \033[0m"))
    childrenDetail=[]
    x=0
    while x<(childCount*4):
        childrenDetail.append(input("\033[0;33m Enter name of target's : \033[0m"))
        childrenDetail.append(input("\033[0;33m Enter nick name of target's partner : \033[0m"))
        childrenDobCheck = True
        while childrenDobCheck:
            childrenDob = input("\033[0;33m Enter birth date of target's partner (DDMMYYYY) or enter \033[0;34mno\033[0;33m if there is no info about date of brith : \033[0m")
            if childrenDob !="no":
                if len(childrenDob)==8 and childrenDob.isnumeric():
                    childrenDetail.append(childrenDob[0:2])
                    childrenDetail.append(childrenDob[2:4])
                    childrenDetail.append(childrenDob[4:])
                    childrenDobCheck  = False
                else:
                    print("\033[0;31m date of birth of target's partner you have given is incorrect it shouldd in format DDMMYYYY \033[0m ")
            else:
                childrenDobCheck  = False

        x+=4




info = [name, lastName, age, petName, nickName, birthDate, birthMonth, birthYear, partnerName, partnerNick, partnerbirthDate, partnerbirthMonth, partnerbirthYear, fatherName, motherName]
if children=="yes":
    info=info+childrenDetail
symboles = ["@", "#", "$", "!", "&",""]

for x in info:
    for y in info:
        for z in symboles:
            for a in symboles:
                for b in symboles:
                    if x == "" or y == "":
                        pass
                    else:
                        with open("test.txt","a") as f:
                            f.write(a+x+b+y+z+"\n")
                            f.close()

