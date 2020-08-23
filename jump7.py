i=0
while i<100:
    i+=1
    if(7==i%10) or (0==i%7) or (7==i//10):
        continue
    print(i)

