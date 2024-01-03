num1=float(input()) #使用者輸入並轉為浮點數
num2=float(input())
num3=float(input())
num4=float(input())

print('|%7.2f %7.2f|'%(num1,num2))      #讓間距為7並取到小數點第二位然後向右靠其印出num1跟num2
print('|%7.2f %7.2f|'%(num3,num4))      #同上 但印出num3跟num4
print('|%-7.2f %-7.2f|'%(num1,num2))    #讓間距為7並取到小數點第二位然後向左靠其印出num1跟num2
print('|%-7.2f %-7.2f|'%(num3,num4))    #同上 但印出num3跟num4