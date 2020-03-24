import datetime
def getdate():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c = int(input("enter 1 for excersise and 2 for food "))
        if(c==1):
            value = input("type here\n")
            with open("p1_exe.txt", "a") as op:
                op.write(str([str(getdate())])+": "+ value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("p1_fd.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food "))
        if (c == 1):
            value = input("type here\n")
            with open("p2_exe.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("p2_fd.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food "))
        if (c == 1):
            value = input("type here\n")
            with open("p3_ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("p3_fd.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input ")


def retrieve(k):
    if k==1:
        c = int(input("enter 1 for excersise and 2 for food "))
        if(c==1):
            with open("p1_exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("p1_fd.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food "))
        if (c == 1):
            with open("p2_exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("p2_fd.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food "))
        if (c == 1):
            with open("p3_exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("p3_fd.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (p1,p2,p3)")
print("health management system: ")
a =int(input("press 1 for lock the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for p1 2 for p2 3 for p3 "))
    take(b)
else:
    b = int(input("press 1 for p1 2 for p2 3 for p3 "))
    retrieve(b)