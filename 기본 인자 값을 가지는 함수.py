def hello(msg="안녕하세요"):
    print(msg + "!")
hello("오랜만이에요")
hello("이영희")
hello()

print()

def hello(name="무명", msg="안녕하세요"):
    print(name + "님, " + msg + "!")
hello("김철수", "오랜만이에요")
hello()

def hello(name, msg="안녕하세요"):
    print(name + "님, " + msg + "!")
hello("김철수", "오랜만이에요")
hello("이영희")