   
#문자형은 어떻게 다루는지가 중요하다.
#문자형 인덱싱 슬라이싱 
#문자열을 다루는 방법 
#어떻게 문자열을 효과적으로 다루지? 
# 인덱스는 문자에 붙여진 순서
# 0부터 시작한다. 철수야 안녕 012 34
# 인덱스가 음수라면? -1은 맨끝에서 붙여진 문자 
# 슬라이싱 : '여러개의'문자에 범위로 접근하는 방법
# 리스트 (튜플), 딕셔너리 
#리스트 자료형 
#리스트 : 변할수도 있는 데이터 
#튜플: 변할 수 없는 데이터를 나란히 묶어주는 자료형 
#가장 중요한건 딕셔너리(해쉬)
#딕셔너리 : 우리는 key를 통해 value를 얻는다.
# 문자열 (내장함수)
#str = "이든아"
#str2 = "이든아 넌 나에게 모욕감을 줬어"

#print(str2[0:3])

#슬라이싱은 [x:y] x번째 인덱스부터 y 인덱스 전까지
#문자열 길이를 구해주는 : len(문자열변수) 길이는 1부터 세

#print(len(str2))
#문자열 내에서 특정문자 등장 횟수:문자열 변수 .count('특정문자')

#print(str2.count('이'))

#문자열을 (특정기준으로)나누기 : 문자열 변수 .split()
#print(str2.split('나에게')) #공백을 기준으로 나누겠다.

#특정문자 인덱스 찾기 : find('문자') , index('문자')

#print(str2.index('이'))
#그럼 인덱스랑 파인드는 똑같은거 아님? 
#찾고자 하는 문자가 없을때 차이가 없을때 

#리스트 (내장함수)

#li = [3, 1,'정이든', 4,'바보', 5, 1]

#인덱싱 슬라이싱
#print(li[0:2])
#리스트의 길이를 구해주는거 : len(변수)
#print(len(li))
#리스트 원소 오름차순으로 정렬해주는 함수 :sort()
#print(li)


#li.sort()

#print(li)

#리스트내의 특정 원소 인덱스를 반황해주는 함수 : .index()

#print(li.index("정이든"))

#리스트내의 특정 원소의 갯수 세기 : .count(요소)

#딕셔너리 (내장함수)


#airs = {'잔나비' :'뜨거운감자', '트와이스':'룰루랄라','뭉크':'절규'}

#하나의 키 -value 쌍을 추가하는 방법 

# 딕셔너리형 변수[키] = value
#print(pairs)

#pairs['스탠딩에그']='맛있겠다'

#print(pairs)

#하나의 키 value를 삭제하는 방법 = del 함수 
# del 변수[키]

#del pairs['스탠딩에그']

#print(pairs)

#key로 value를 얻는 : 변수.get(키)

#v = pairs.get('뭉크')
#print(v)

#제어문
#뭘제어해? 
#코드의 흐름을 제어한다!
#분기문 (=if문)
#컴퓨터에게 선택의 여지와 조건을 부여 
##85점 이상으면 pass , fail 

#score = int(input("점수를 입력해주세요: " ))

#if(score>=85):
 #print("pass")
#else:
# print("fail")

#activity = input("너동아리 머행? :")

#if(activity=="멋쟁이사자처럼"):
   # print("맞아?")
#else:
   # print("응 잘가")

#money = int(input("돈 얼마있냐?"))

#if(money>=5000):
    #print("아웃백")
#elif(money>=3000):
    #print("학식")
#elif(money>=1000):
     #print("컵라면")
#else:
   # print("공기밥")

#else if =elif

#반복문이 무엇인가 
#반복문을 수행해주는 문법은 어떤것이 있는가. 
#for while
#for 반복제어변수 in 반복대상:
#range(x,y)
#x이상 y미만의 수 리스트로 반환
#range(x)
#0부터 x미만의 수 리스트로 반환

#for문 이 반복 대상을 반복하세요!
#while문 이조건을 만족하는 동안 반복하세요!
 
#인자 #리턴값(함수가 제기능을 다 한 결과- 리턴값은 하나)
#함수의 존재 목적 : 함수는 코드를 기능적으로 정리한 단위 
#리턴값이 없을 수 도 있다. 

#함수의 안과 밖 : 변수의 범위 
#함수를 만들겠다 =코드를 기능별로 정리정돈 하겠다. 
#함수의 존재목적 =코드를 기능별로 영역구분하겠다.
#지역변수를 쓰고 전역변수는 좀 자제해주세요. 



# count = 1
#while count < 5:
   #if count == 3:
     # continue

  # print("%d번째 반복 중" % count)
  # count = count + 1


# for i in range(1, 5, 1):
   # if i % 2 == 0:
      #  continue

   #  print("%d번째 반복중" % i)

# 문제1. for문을 활용해서 1부터 10까지 숫자를 출력해주세요.
# for i in range(1,11):
   # print(i)



# 문제2. for문을 활용해서 1부터 10까지 숫자 중 3의 배수는 제외하고 출력해주세요. (단, continue이용)

# for i in range(1, 11):
#    if i % 3 ==0:
#       continue
   
#    # print(i)

# count = 2

# while count <6:
#    print("*"*count)
#    count = count + 1

# for i in rnage(5):
#     print(" " * i, end = "")
#     print("*" * (5-i))

# for i in range(5):4
# 
# for j in range(5):
      # if j < i : 
      #    print("*",end="")

# for i in range(5):
#    for j in range(5):
#       if j < i:
#          print(" ", end="")
#       else:
#          print("*",end="")
#    print()

# print("%d번째 반복 중"% 5)
# print("%f입니다. %c호!" % (12.345, "야"))
# print("%c입니다." %"야")
# print("%s!"%"야호")

# count = 5
# print(f"{count}번째 반복 중")

# def add(a,b):
#    return a + b 
# add(1,2)

# print(add(1,2))

# def get_number():
#    return 4

#    print(get_number())

# str = input("문자열을 입력하세요.")

# def reverse_str(str):
#     for i in range(len(str)-1, -1, -1):
#         print(str[i], end="")

# reverse_str(str)




