def Fibo(n):
    if (n <= 1):
        return n
    else:
        return Fibo(n-1) + Fibo(n-2)
    

if __name__ == "__main__":
    print(Fibo(20))
