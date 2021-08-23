work_done = 1
money = 0
while(work_done != 0):
    work_done = int(input("Have you done your task? "))
    if work_done:
        money+=10
    print("Your current money is {}".format(money))
print("You earned {} in your internship!".format(money))
