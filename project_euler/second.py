def LPF(x):
    k=2
    while(x>k):
        if (x%k == 0):
            x = x/k;
            k=2;
        else:
            k=+1;
    print("the largest prime factor is ", k)

LPF(6)
