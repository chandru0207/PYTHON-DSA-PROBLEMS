# def split(num):
#     if(num<=0):
#         return False
#     out1=str(num)
#     out2=""
#     for i in num:

out=int(input("enter the number :"))
out1=0
out2=1
while(out>0):
    rem=out%10
    out1=out1+rem
    out2=out2*rem

    out=out//10






if(out1==out2):
        print("it is spy number")
else:
        print("it is not spy number")





