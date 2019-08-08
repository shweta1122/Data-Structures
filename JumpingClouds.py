def jumpingOnClouds(c):
    length=len(c)
    i=0
    count=-1
    while(i<len(c)):
      if i+2<length:
        if c[i+2]==0:
            count+=1
            i+=2
        else:
            i+=1
            count+=1
      else:
            i+=1
            count+=1
          

    print(count)


c = [0, 0, 0, 0, 1, 0]
jumpingOnClouds(c)

        


