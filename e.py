
from sympy import *

A, EA, B, EB = symbols('A EA B EB')

mu, epsilon, K = symbols('mu epsilon K')

z, r = symbols('z r')

lam = symbols('lam')

I, pi = symbols('I pi')


###  E_theta

A = (z - (lam/4)) / ( lam*r * sqrt( r**2 + (z - (lam/4))**2 ))
EA = -I*2*pi * ( sqrt( r**2 + (z - (lam/4))**2 ) / lam )

B = (z + (lam/4)) / (lam*r * sqrt( r**2 + (z + (lam/4))**2 ))
EB = -I*2*pi * ( sqrt( r**2 + (z + (lam/4))**2 ) / lam )

E_theta = I*2*pi * sqrt(mu/epsilon) * K * (( A * exp(EA) ) - (B * exp(EB)))