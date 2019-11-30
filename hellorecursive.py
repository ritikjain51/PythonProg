
a=0
def hello():
    global a
    print("hello world")
    if(a<5):
        a=a+1
        hello()
hello()   