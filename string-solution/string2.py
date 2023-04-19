#script to enter any print palindrome word and total number of palindrome word
def sentpailndrome(s):
    d=[]
    t=0
    c=s.split()
    for i in c:
        cp=i[::-1]
        if cp==i:
            print(cp)
            d.append(cp)
            t=t+1
    print(f"Total {t} Palindrome Word In String :{set(d)}")
s=input("Enter Sentence:")
sentpailndrome(s)
 
