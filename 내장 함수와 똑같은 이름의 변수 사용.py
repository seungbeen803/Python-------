# 내장 함수와 똑같은 이름의 변수 사용
str = "나는 문자열"
print(str)

n = 3
print(str(n))
# 에러 발생
# 내장 함수명과 똑같은 이름의 변수를 만들어 사용할 경우
# 함수는 변수 처리되어 사용할 수 없다
# 파이썬에서는 함수도 객체로 다루기 때문에 일어나는 현상
# not callable -> 함수랑 같은 변수가 있다라는 의미