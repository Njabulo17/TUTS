# -*- coding: utf-8 -*-
"""
Created on Mon May 08 03:36:13 2017

@author: njabulo mbanjwa, CP Tutorial 2
"""
import numpy as np
import pylab
from numpy.fft import fft,ifft

#Question 1 and 2 function
def corrF(x,y): #defining the correlation funnction
    assert(x.size==y.size) # the vectors of the same size
    ft1 = fft(x)
    ft2 = fft(y)
    ft2conj=np.conj(ft2)
    return np.real(ifft(ft1*ft2conj))
 
 #Question 3 function              
def myshift(x,n=0):#defining a function
    vec=0*x  #make a vector of zeros the same length as the input vector
    vec[n]=1
    vecft=fft(vec)
    xft=fft(x)
    return np.real(ifft(xft*vecft))


#Question 4 function
def circConv(x,y): #defining a function
    assert(x.size==y.size) # the vectors of the same size
    xx=np.zeros(2*x.size)
    xx[0:x.size]=x

    yy=np.zeros(2*y.size)
    yy[0:y.size]=y
    xxft=fft(xx)
    yyft=fft(yy)
    vec=np.real(ifft(xxft*yyft))
    return vec[0:x.size]

#The gaussian function 
def mygauss(x):
    y=np.exp(-0.5*x**2/2**2)#sigma = 2
    return y


if __name__=='__main__':

    x=np.arange(-15,15,0.1)
    y=mygauss(x)
    
    #Problem 1 results
    yshift = myshift(y,100)
    pylab.plot(x,y)
    pylab.plot(x,yshift)
    pylab.show()  
    
    #Problem 2 results
    ycorr=corrF(y,y)
    pylab.plot(x,ycorr,'r--')
    pylab.show()
    
   #Problem 3 results    
    ycorr=corrF(y,y)
    yshift=myshift(y,y.size/4)
    yshiftcorr=corrF(yshift,yshift)
    meanerr=np.mean(np.abs(ycorr-yshiftcorr))
    print 'The mean difference between the two correlation functions is ' + repr(meanerr)
    pylab.plot(x,ycorr)
    pylab.plot(x,yshiftcorr,'g--')        
    pylab.show()       
    
   # Problem 4 results
    y=y/y.sum()
    yconv=circConv(y,y)
    pylab.plot(x,y)
    pylab.plot(x,yconv)
    pylab.show()


   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    