#program to create 3*3 matrix
import numpy as np
def matrix(arr):
     rearr=array.reshape((3,3))
     print(rearr)
     print("\n Dimension Of Array Is :",rearr.ndim)
     print("\n Total Elements In Above Array :",rearr.size)
     print("\n Size Of An Each Element In Above Array :",rearr.itemsize)
     print("\n Size Of An Array :",rearr.nbytes)
array=np.arange(2,11)
matrix(array)
