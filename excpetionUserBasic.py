s=int(input('enter a no'))
class myexcep(Exception):
    pass
try:
    if(s>50):
        raise myexcep
except myexcep:
    print("please enter value less than 50")
