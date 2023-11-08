'''a,b,c=map(int,input().split())
if (a-b+c)%10==0:
    print('대박')
else :
    print('그럭저럭')



a,b,c=map(int,input().split())
if (a-b+c)%10==0:
    print('대박')
else :
    print('그럭저럭')'''
'''
a,b,c=map(int,input().split())
if a<=170 or b<=170 or c<=170:
    print('CRASH')
else:
    print('PASS')

n=int(input())
if n%2==0:
    print('짝수')
else :
    print('홀수')

a=0,b=0
if a%2==0:
    b=b+1

a,b=map(float,input().split())
c=(a-100)*0.9
d=(b-c)*100/c
if d<=10:
    print('정상')
elif 10<d<=20:
    print('과체중')
else:
    print('비만')

h,w=map(float,input().split())
s=0
if h<150:
    s=h-100
elif 150 <=h < 160:
    ((h-150) /2) +50
else:
    s=(h-100) * 0.9
o=((w-s)*100)/s
if o<= 10:
    print("정상")
elif 10<o<=20:
    print("과체중")
else:
    print("비만")
'''
a=int(input())
b=int(input())
print(a+b)
