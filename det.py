

from sympy import Symbol, symbols,  Matrix, Function, simplify

from sympy import Derivative
from sympy.solvers.pde import pdsolve
from sympy import Function, Eq, latex


i = Symbol('\\vectorunit{i}')
j = Symbol('\\vectorunit{j}')
k = Symbol('\\vectorunit{k}')

Ex, Ey, Ez = symbols('\\vb{E_{x}} \\vb{E_{y}} \\vb{E_{z}}')

dx  = Symbol('\\pdv{}{x}')
dy  = Symbol('\\pdv{}{y}')
dz  = Symbol('\\pdv{}{z}')

A = Matrix([[i, j, k], [dx, dy, dz], [Ex, Ey, Ez]])
B = A.det()

print( "det" + latex(A) + " = " + latex( B) )


