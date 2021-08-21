a = int(input("Enter a number: "))
bool = True
for i in range(2,a//2):
    if a%i == 0:
        print("Not prime")
        bool = False
        break
if bool:
    print("Prime")