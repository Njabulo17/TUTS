# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:18:36 2017

@author: Njabulo Mbanjwa, Computational Physics
"""

#Problem3
import numpy as np
import pylab
from scipy.integrate import quad
#
def npoints(n):
    x = np.linspace(0,np.pi/2,n)
    return x

#Problem 3 continues
def Simpsons_rule(n):

        p = [10,30,100,300,1000]

        for n in p:

                dx=(np.pi/2-0)/n

                x=np.linspace(0,np.pi/2,n)

                y=np.cos(x)

                Simple_meth=y.sum()*dx

                print 'The integral is ' + repr(Simple_meth) + ' with number of points equal ' + repr(n)

#Question 4
def Simpsons_rule(n):

        dx=np.pi/2/(n*2)

        Xn=np.cos(npoints(n))

        Xeven=Xn[2:-1:2] #selection of even numbers 

        Xodd=Xn[1:-1:2]#selection of odd numbers

        tot =1/6*(Xn[0]) + 1/3*(np.sum(Xeven)) + 2/3*(np.sum(Xeven)) + 1/6*(Xn[-1])

        return tot*dx


if __name__=='__main__':

#Problem5
        answer=Simpsons_rule(11)

        error=np.abs(answer-1)

        print ' The answer is ' + repr(answer)

        print 'error for 11 points ' + repr(error)

        for n in p:

                error=abs(Simpsons_rule(n)-1)

                print 'The error for ' + repr(n)+ ' points is ' + repr(error)

        

#Question 6

	p =[11,31,101,301,1001,3001,10001,3001,100001]  

	p = np.array(p)

	simpson_error=np.zeros(p.size)

	simple_error=np.zeros(p.size)

	for k in range(p.size):

		n=p[k]

		dx=np.pi/2/n

                x=np.linspace(0,np.pi/2,n)

                y=np.cos(x)

		Simple_meth=y.sum()*dx

		simpson_error[k]=np.abs(Simpsons_rule(n)-1)

		simple_error[k]=np.abs(Simple_meth-1)

	pylab.plot(p,simple_error,'r-o')

	pylab.plot(p,simpson_error,'b-o')

	ax=pylab.gca()



	ax.set_yscale('log')

	ax.set_xscale('log')

