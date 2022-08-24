# class 類別(種類)
# class 好處: 可以共用所有的function, 屬性, 較好包裝程式

class Student:
	def __init__(self, name, score):  # initialize 初始化
		self.name = name   #將名字存成參數
		self.score = score
		self.x = 5   #class可以給予不同於function的屬性

		print('我誕生了')   
		self.do_hw('英文')    #self 並不是參數, 而是拿來在別的function中自我使用的
		self.study()    #參數是從第二個開始的

	def do_hw(self, hw):     
		print('我在做作業', hw)

	def study(self):
		print('我在讀書')
		self.score += 5

	def sleep(self):
		print('i am sleeping!')
		self.score += -5


s1 = Student('Charlene', 100)
s2 = Student('Allen', 40)


#可將student 存成一個lisy做計算
student = [s1, s2]

for s in student:
	print(s.name, '的分數是', s.score)


#funtion 內部可自行計算
print(s1.name, s1.score)
print(s2.name, s2.score)

s2.study()
print(s2.name, s2.score)
s2.sleep()
print(s2.name, s2.score)

print(dir(s1))