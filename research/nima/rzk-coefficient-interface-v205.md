# v205: two-grade conductor trace supplies the a+b residue block

Past normalization-duality work contains an explicit source-derived trace, not merely an abstract residue parameter. On the two selected source coordinates `(p_A,e35)`, the endpoint and reciprocal traces are

`R(nu_E)=(-beta*e0,0)`

and

`R(nu_R)=(-beta*e0,-beta*e1)`.

Equivalently, the raw coefficient matrix is

`-beta * [[1,1],[0,1]]`,

with columns `(p_A,e35)`. Therefore a class with coordinates `(a,b)` has reciprocal trace value `-beta(a+b)`, while the endpoint trace separately reads `-beta*a`. The normalized matrix is unimodular for fixed nonzero beta; no occurrence variable is inverted and no division by beta is asserted at beta zero.

Composing the reciprocal trace with the selected relation coordinate `c=rho0(v)` gives exactly

`-beta(a+b)-beta*c = -beta(a+(b+c))`.

Thus the algebraic pointwise residue formula is source-derived on the selected three-line packet. The remaining physical premise is not the residue algebra: it is the map carrying the selected physical Gysin class to `(a*p_A+b*e35,c*v)` in this packet.
