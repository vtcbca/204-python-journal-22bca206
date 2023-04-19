#Script To Check String Is Palindrome Or Not
def strpalindrome(s):
    re=s[::-1]
    print("Reverse Of Inputted String Is \"{}\" ".format(re))
    if re==s:
         print("\"{}\"  Is Palindrome ".format(s))
    else:
        print("\"{}\" Is Not Palindrome".format(s))
s=input("Enter String To Check:")
strpalindrome(s)

    
