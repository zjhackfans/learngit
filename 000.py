import random
secret=random.randint(1,10)
guess=int(input("输入一个数字："))
n=0
while guess!=secret and n<=3:
    n=n+1
    if guess>secret:
        print("哥，大了大了~")
    else :
        print("嘿，小了小了~")
    guess=int(input("重新输入："))
    
if guess==secret:
    print("输入正确")
else:
    print("你已经输错3次啦~")
print ("游戏结束")
