#Menu Driven Script  To Perform Operation on List
def menudriven():
    ans='y'or'Y'
    while ans=='y' or ans=='Y':
        print("\nNOTE :- You MUST Create List OHERWISE the further operation on list can not be performed\n\tSo You Have To Choose 1 Menu To Perform Other Operations\n")
        print("\n\t\t MENU\n------------------------------------------------ ")
        print("1.Create list till user's choice")
        print("2.print string which has even length")
        print("3.replace odd character of string with index no")
        print("4.enter start and end value and extract character")
        e=[1,2,3,4]
        ch=int(input("\n\nEnter Choice From above list :"))
        print("\n")
        if ch==1:#create list till user's choice
          l=[]
          n=int(input("Enter No Of Element For Creating List :"))
          for i in range(n):
                  a=input("Enter Element To Create list:")
                  l.append(a)
          print("\n",l)

        def evenlenstr():#function for 2nd menu
               for i in l:
                   if len(i)%2==0:
                       print(i)
                       break
               else:
                 print("There Is No Even String Is Inputted By User")
        if ch==2: #if user enter 2,below function is called
           evenlenstr()
           
        def oddchar():#function for 3rd menu
          for i in l:
             for j in range(len(i)):
                  if j%2!=0:
                      li=j
                  else:
                      li=i[j]
                  print(li)
        if ch==3: #if user enter 3,below function is called
              oddchar()
             
        def extractchar():#function for 4th menu
             sp=int(input("\nEnter value for starting position: "))
             ep=int(input("\nEnter value for ending postion:"))
             a=[]
             for i in l:
                a.append(i[sp:ep])
             print("\n",a)
        if ch==4:#if user enter 4,below function is called
             extractchar()
            
        if ch not in e:
            print("INVALID CHOICE")
           
        ans=input("\n\nDo You Want To Continue...? if yes then press Y/y :- ")
menudriven() 
