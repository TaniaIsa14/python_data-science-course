n=int(input('value:'))
a=int(input('value:'))
c=int(input('value:'))
my_dict={'N:': n ,'A:': a,'c:': c}
print(my_dict)
sum=0
for i in my_dict:
    sum=sum+i
print(int(sum))