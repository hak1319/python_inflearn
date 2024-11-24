# chater06-1
# 파이썬 클래스
# oop (객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스(붕어빵 틀이다) and 인스턴스(이클래스를 가지고 코드에서 사용하는 객체) 차이 이해
# 인스턴스와 객체의 차이점 어찌보면 인스턴스가 객체에 포함되어 있음
# 네임스페이스 : 객체를 인스턴스화 할ㄷ 때 저장된 공간
# 클래스 변수 : 직접 접근 가능 ,하나를 공유하기에 이걸로 선언된 변수는 변하지 않음
# 인스턴스 변수 : 객체마다 별도 존재 , 나만의 공간에 저장하는거이기에 객체마다 전부 다르다 self.000

#예제1

class dog(): # 모든클래스는 object 를 상속받음 그냥 dog , dog() ,dog(object) 3가지방법
    #클래스속성
    species = 'firstdog'

    #초기화/인스턴스 속성
    def __init__(self, name,age) :
        self.name = name
        self.age = age
# 클래스 정보
print(dog)

# 인스턴스화 -> 이런 클래스 즉 설계도를 바탕으로 구현 된 것을 인스턴스화 되었다 함 (코드로 즉 변수로 사용할 수 잇게 된 시점)
a = dog("woddy",2)
b = dog("baby",3)
c = dog("woddy",2) # 인스턴스화 시켜도 a랑 c 는 다른 것임 인스턴스화 시키면 전부 다른 값임

print(a==c)

# 네임스페이스
print("dog1 ", a.__dict__)
print("dog2 ", b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is  {}'.format(a.name,a.age,b.name,b.age))

