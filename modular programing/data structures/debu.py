for i in range(1,5):
    print("outer loop",i)
    for j in range (1,3):
        print("inner loop",j)
        if i ==2:
           break