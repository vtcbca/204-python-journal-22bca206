#program to convert a list of numeric value  into a numpy one dimensional array
import numpy as np
def listnumpy():
     l=[]
     n=int(input("Enter Number Of Element For Create List:"))
     for i in range(n):
          e=float(input("Enter Element For list:"))
          l.append(e)
     print("\nOriginal List :",l)
     a=np.array(l)
     print("\nOne Dimensional Numpy Array:",a)
     print("\nDimension Of Array :",a.ndim)
     print("\nSize Of An Array",a.size)
     print("\nBytes Of An Array",a.nbytes)
listnumpy()
