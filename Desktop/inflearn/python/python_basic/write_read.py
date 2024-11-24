# Chapter09-1
# 파일 읽기 및 쓰기

# 읽기 모드 : r , 쓰기모드 w, 추가모드 a, 텍스트 모드 t(기본값), 바이너리 모드 b
# 상대경로('../,./'), 절대경로('c:\djang\...')

# 파일 읽기(read)
# 예제1

f = open('./resource/it_news.txt','r',encoding ='UTF-8') # 오픈함수
    # 1. 경로
    # 2. 뭐할꺼냐
    # 3. encoding 무슨 인코딩으로 작성되었냐
#print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일이름
print(f.name)
# 모드확인
print(f.mode)
cts=f.read()
print(cts)
# 반드시 close
f.close()

# 예제2

with open('./resource/it_news.txt','r',encoding ='UTF-8') as f :
    c =f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제 3
# read() : 전체읽기, read(10) : 10byte 만 읽어옴

with open('./resource/it_news.txt','r',encoding ='UTF-8') as f :
    c =f.read(20) 
    print(c)
    c =f.read(20) # 커서 즉 어디까지 읽엇냐가 표시됨 2번째 선언되엇을 때는 처음 읽은 20 바이트 다음 바이트부터 읽음
    print(c)
    print(c)
    c =f.seek(0.0) # 처음부터 다시 읽겟다 선언
    print(c)
    c =f.read(20)
    print(c)
print()

# readline : 한줄씩 읽겠다.

with open('./resource/it_news.txt','r',encoding ='UTF-8') as f :
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
print()

# readlines : 전체를 읽은 후 라인 단위 리스트로 저장

with open('./resource/it_news.txt','r',encoding ='UTF-8') as f :
    cts=f.readlines()
    print(cts)
    print()
    for c in cts :
        print(c, end='') # 다시 원문으로 돌림

print()

# 파일 쓰기 (write)

with open('./resource/contents1.txt','w') as f :
    f.write('i love python\n')

with open('./resource/contents1.txt','at') as f :
    f.write('i love python2\n')

# writelines : 리스트 -> 파일
with open('./resource/contents2.txt','w') as f :
    list = ['orage\n','apple\n','banna\n','melon\n']
    f.writelines(list)


with open('./resource/contents3.txt','w') as f :
    print('test text write !', file=f)
    print('test text write !', file=f)
    print('test text write !', file=f)