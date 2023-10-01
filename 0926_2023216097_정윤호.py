Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
aa = [0,0,0,0]
hap = 0

aa[0] = int(input("1번째 숫자: "))
1번째 숫자: 10
aa[1] = int(input("2번째 숫자: "))
2번째 숫자: 20
aa[2] = int(input("3번째 숫자: "))
3번째 숫자: 30
aa[3] = int(input("4번째 숫자: "))
4번째 숫자: 40

hap = aa[0] + aa[1] + aa[2] + aa[3]

print("합계 ==> $d" %hap)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("합계 ==> $d" %hap)
TypeError: not all arguments converted during string formatting
print("합계 ==> %d" %hap)
합계 ==> 100

aa = []
aa.append(0)
aa.append(0)
aa.append(0)
aa.append(0)
print(aa)
[0, 0, 0, 0]

aa = []
for i in range(0,100) :
    aa.append(0)

    
len(aa)
100
aa = []
for i in range(0,10) :
    aa.append(0)

    
hap = 0

for i in range(0,10):
    aa[i] = int(input(str(i + 1) + "번째 숫자 : "))

    
1번째 숫자 : 10
2번째 숫자 : 20
3번째 숫자 : 30
4번째 숫자 : 40
5번째 숫자 : 50
6번째 숫자 : 60
7번째 숫자 : 70
8번째 숫자 : 80
9번째 숫자 : 90
10번째 숫자 : 100
i = 0
while i<10
SyntaxError: incomplete input
while i<10 :
    hap += aa[i]
    i = i + 1

print("합계 ==> %d" %hap)
합계 ==> 550



aa = []
bb = []
value = 0

for i in range(0,100):
    aa.append(value)
    value += 2

    
for i in range(0,100):
    bb.append(aa[99 - i])

    
print("bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다." %(bb[0], bb[99]))
bb[0]에는 198이, bb[99]에는 0이 입력됩니다.



aa = [10, 20, 30, 40]
aa[0:3]
[10, 20, 30]
aa[2:4]
[30, 40]

================ RESTART: C:/Users/Administrator/Desktop/7-1.py ================
1번째 숫자 : 1
2번째 숫자 : 2
3번째 숫자 : 3
4번째 숫자 : 4
5번째 숫자 : 5
6번째 숫자 : 6
7번째 숫자 : 7
8번째 숫자 : 8
9번째 숫자 : 9
10번째 숫자 : 10
합계 ==> 55


aa = []
bb = []
vlaue = 0

for i in range(0,100) :
    aa.appned(value)
    value += 2

    
Traceback (most recent call last):
  File "<pyshell#72>", line 2, in <module>
    aa.appned(value)
AttributeError: 'list' object has no attribute 'appned'. Did you mean: 'append'?
for i in range(0,100) :
    aa.append(value)
    value +=2

    
Traceback (most recent call last):
  File "<pyshell#76>", line 2, in <module>
    aa.append(value)
NameError: name 'value' is not defined. Did you mean: 'vlaue'?
value - 0
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    value - 0
NameError: name 'value' is not defined. Did you mean: 'vlaue'?
value = 0
for i in range(0,100) :
    aa.append(value)
    value += 2

for i in range(0,100) :
    bb.append(aa[99 - i])

    
print("bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다." %(bb[0], bb[99]))
bb[0]에는 198이, bb[99]에는 0이 입력됩니다.


aa = [10,20,30,40,50,60,70,80,90,100]
aa[2:10]
[30, 40, 50, 60, 70, 80, 90, 100]
aa[2:7] //3번째 칸부터 7칸까지
SyntaxError: invalid decimal literal



aa = [10,20,30]
bb = [40,50,60]
aa + bb
[10, 20, 30, 40, 50, 60]
aa * 3
[10, 20, 30, 10, 20, 30, 10, 20, 30]
aa = [10,20,30,40,50,60,70]
aa[::2]
[10, 30, 50, 70]
aa[::-2]
[70, 50, 30, 10]
aa[::-1]
[70, 60, 50, 40, 30, 20, 10]
aa = [10,20,30]
aa[1:2] = [200,201]
aa
[10, 200, 201, 30]


aa = [10,20,30]
aa[1:2] = [200,201]
aa
[10, 200, 201, 30]
aa = [10, 20, 30]
del(aa[1])
aa
[10, 30]
aa = [10,20,30,40,50]
aa[1:4] = []
aa
[10, 50]
myList = [30, 10, 20]
print("현재 리스트 : %s" %myList)
현재 리스트 : [30, 10, 20]

= RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python311/07-05.py
현재 리스트 : [30, 10, 20]
append(40) 후의 리스트 : [30, 10, 20, 40]
pop()으로 추출한 값 : 40
pop() 후의 리스트 : [30, 10, 20]
sort() 후의 리스트 : [10, 20, 30]
reverse() 후의 리스트 : [30, 20, 10]
20값의 위치 : 1
insert(2,222) 후의 리스트 : [30, 20, 222, 10]
remove(222)후의 리스트 : [30, 20, 10]
extend([77,88,77])후의 리스트 : [30, 20, 10, 77, 88, 77]
77값의 개수 : 2


list1 = []
list2 = []
value = 1
for i in range(0,3):
    for k in range(0,4) :
        list1.append(value)
        value +=1
    list2.append(list1)
    list1 = []

for i in range(0,3) :
    for k in range(0,4) :
        print("%3d" %list2[i][k], end = "")
    print("")

    
  1  2  3  4
  5  6  7  8
  9 10 11 12


ttt1 = (10,20,30); tt1
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    ttt1 = (10,20,30); tt1
NameError: name 'tt1' is not defined. Did you mean: 'ttt1'?
tt1 = (10,20,30); tt1
(10, 20, 30)
tt2 = 10,20,30; tt2
(10, 20, 30)
tt5 = (10,); tt5
(10,)
>>> tt1.append(40)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    tt1.append(40)
AttributeError: 'tuple' object has no attribute 'append'
>>> tt1[0] = 40
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    tt1[0] = 40
TypeError: 'tuple' object does not support item assignment
>>> del(tt1[0])
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    del(tt1[0])
TypeError: 'tuple' object doesn't support item deletion
>>> 
>>> 
>>> tt1 = (10, 20, 30, 40)
>>> tt1[0]
10
>>> tt1[0] + tt1[1] + tt1[2]
60
>>> tt2 = ('A', 'B')
>>> tt1 +tt2
(10, 20, 30, 40, 'A', 'B')
>>> t2 * 3
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    t2 * 3
NameError: name 't2' is not defined. Did you mean: 'tt2'?
>>> tt2*3
('A', 'B', 'A', 'B', 'A', 'B')
>>> myTuple = (10,20,30,)
>>> myList = list(myTuple)
>>> myList.append(40)
>>> myTuple = tuple(myList)
>>> myTuple
(10, 20, 30, 40)
