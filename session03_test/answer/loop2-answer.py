# while문을 사용하여 아래와 같이 별을 표시하는 프로그램을 작성해주세요.

"""
*
**
***
****
*****
"""

i = 1

while i < 6:
    print("*" * i)
    i = i + 1



# 시간이 남으신 분들은 for문을 사용하여 아래 문제도 풀어보세요!

# 힌트 : for문 안에 for문이 들어가는 것도 가능합니다.
# 힌트 : print문을 실행하고 enter가 되는 것을 막으려면 print(실행내용, end = "") 을 이용하시면 됩니다.

"""
*****
 ****
  ***
   **
    *
"""
# 풀이1
for i in range(5):
    for j in range(5):
        if j < i:
            print(" ", end = "")
        else:
            print("*", end = "")
    print()

# 풀이2
for i in range(5, 0, -1):
    print(" " * (5 - i), end = "")
    print("*" * i)

