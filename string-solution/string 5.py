#check user inputted string is symmetrical or not.
def strsymmetric(s):
    a=len(s)//2
    f1=s[0:a]
    f2=s[a:]
    if f1==f2:
        print(f"\"{s}\"  Is Symmetircal  String")
    else:
        print(f"\"{s}\"  Is Not Symmetircal String")
def inputstr():
       s=input("Enter String:")        
       strsymmetric(s)
inputstr()
