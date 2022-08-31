def is_primer(n):
    prime = True
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            prime=False
            break;

    return prime
prime_count=0
last_prime = 0
for i in range(1,101):
    if is_primer(i):
        last_time=i
        prime_count+=1
        print(i,end=" ")
print("")
print("We have a",prime_count,"prime counter")
print("last time number was",last_time)




