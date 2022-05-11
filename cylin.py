#
#
#    Experiments with Vector Calculus in
#    Cylindrical Coordinates
#
#    You can define your E field in terms of
#    E_r  E_phi  E_z
#
#    Then the code will calculate the induced B field
#    and display the equation as LATEX.
#
#

import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

from sympy import *
from sympy import symbols
from sympy.vector import Del
from sympy.vector import divergence
from sympy.vector import curl
from sympy.vector import gradient
from sympy import diff, Derivative
from sympy import exp
from sympy import integrate
from sympy import I, pi

from sympy.vector import CoordSys3D



#  Calculate the Divergence of a Vector Field
#  in Cylindrical Coordinates.
def mydiv( F, N):
	Fr = F & N.r
	Fphi = F & N.phi
	Fz = F & N.z
	result = ((1/N.R) * Derivative( N.R * Fr, N.R )) + ((1/N.R) * Derivative( Fphi, N.PHI )) + Derivative( Fz, N.Z)
	return result



#  Calculate the Gradient of a Scalar Field
#  in Cylindrical Coordinates
def mygrad(T,N):
	gR = Derivative(T, N.R) * N.r
	gF = Derivative(T,N.PHI) * (1/N.R) * N.phi
	gZ = Derivative(T,N.Z) * N.z
	result = gR + gF + gZ
	return result
	
#  Set up a Cylindrical Coordinate space
N = CoordSys3D('N', transformation='cylindrical', vector_names=("r", "phi", "z"), variable_names=("R", "PHI", "Z"))

#  Variables
R = N.R
PHI = N.PHI
Z = N.Z

R._latex_form = 'r'
PHI._latex_form = '\\phi'
Z._latex_form = 'z'



#  Basis Unit Vectors
rhat = N.r
phihat = N.phi
zhat = N.z

rhat._latex_form = '\\vectorunit{r}'
phihat._latex_form = '\\vectorunit{\\phi}'
zhat._latex_form = '\\vectorunit{z}'



#  Prepare the r, phi, and z components of the Electric Field
E_r = Symbol('E_{r}')
E_phi = Symbol('E_{\\phi}')
E_z = Symbol('E_{z}')





#  Symbols
x, y, z, t = symbols('x y z t')
wavenumber = symbols('k')

#  Amplitude of E field
E_0 = symbols('E_0')

#  Omega is Angular Frequency
w = symbols('omega' , real=True, positive=True)






#  The Electric Field
E = (E_r * rhat) + (E_phi * phihat) + (E_z * zhat)

#  It's OK to define the E field as we did above, as purely
#  symbolic. 
#  We can also make E_r E_phi E_z to be functions of
#  R, PHI, and Z.
#  Example:
#  Define E_phi(r,phi,z,t)
#  Note:    I = sqrt(-1)
#  E_phi = (1/R) * smp.exp( I * ( w*t ))
#  E_phi = 7 * smp.exp( I * w * t)
#  E_r = PHI



#    Now we will find the B field from the E field.
#
#    B = - Integral of the Curl of E w.r.t. time
#
#    Curl E   =   - dB/dt
#    integrate( (curl E) , t )   =   - B
#  - integrate( (curl E) , t )   =     B
sean_curl_E = curl( E )
B = -integrate( sean_curl_E, t )


#   We may also be interested in seeing the Divergence of E
sean_div_E = mydiv( E, N)
# sean_div_E = divergence(E)
# sean_div_E = ((1/R) * diff( R * E_r, R)) \
# + ((1/R) * diff(E_phi, PHI)) \
# + diff( E_z, Z)




#  Recalculate!  For when you are doing python -i
def se():
	global E, E_r, E_phi, E_z, sean_curl_E, sean_div_E, B
	E = (E_r * rhat) + (E_phi * phihat) + (E_z * zhat)
	sean_curl_E = curl( E )
	sean_div_E = mydiv( E, N)
	B = -integrate( sean_curl_E, t )


#  Display the answers as LATEX
#  init_printing(use_unicode=True, wrap_line=False)
def ds():
	print("$$ \\require{physics} $$")
	print("$$ \\vb{E} = " + latex(E) + " $$")
	print("$$ \\divergence{\\vb{E}} = " + latex(sean_div_E) + " $$")
	print("$$ \\curl{\\vb{E}} = " + latex(sean_curl_E) + " $$")
	print("$$ \\vb{B} = " + latex(B.simplify()) + " $$")

init_printing( use_latex='mathjax' )
print("$$ \\require{physics} $$")
print("$$ \\vb{E} = " + latex(E) + " $$")
print("$$ \\divergence{\\vb{E}} = " + latex(sean_div_E) + " $$")
print("$$ \\curl{\\vb{E}} = " + latex(sean_curl_E) + " $$")
print("$$ \\vb{B} = " + latex(B.simplify()) + " $$")





#  Alternative Way of defining the components of
#  the Electric Field:
#  The r, phi, and z components of the Electric Field

# E_r = smp.Function('E_r')()
# E_phi = smp.Function('E_phi')()
# E_z = smp.Function('E_z')()

# E_r._latex_form = 'E_{r}'
# E_phi._latex_form = 'E_{\\phi}'
# E_z._latex_form = 'E_{z}'

#  Note that if we define these variables as symbols()
#  Then we have to give the latex form this way:
#  E_phi = symbol('E_{\\phi}')
#  symbols have no attribute ._latex_form
#  Whereas Functions do.




# E_r = smp.Function('E_r')
# E_phi = smp.Function('E_phi')
# E_z = smp.Function('E_z')

# E_r = E_r( R,PHI,Z)
# E_phi = E_phi( R,PHI,Z)
# E_z = E_z( R,PHI,Z)

# E_r._latex_form = 'E_{r}'
# E_phi._latex_form = 'E_{\\phi}'
# E_z._latex_form = 'E_{z}'

