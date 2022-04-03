x=input("What do you want to name your python file? ")
f=open(x+".py","w")
x=input("What is your code? ")
while True:
    y=f.write(x)
    x=input("What is your code? ")
    if x=="done":
        break
f.close()