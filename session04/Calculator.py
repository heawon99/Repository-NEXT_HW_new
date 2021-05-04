class Caculator:
    def __init__(self, name):
        self.name = name
        self.result = 0
    def add(self, num1, num2):
        self.result = num1 + num2
        return self .result

caculator1 = Caculator("정상윤")
print(caculator1.name)
print(caculator1.add(3,5))

