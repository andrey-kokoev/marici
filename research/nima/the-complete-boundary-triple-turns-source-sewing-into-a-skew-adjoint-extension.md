# The complete boundary triple turns source sewing into a skew-adjoint extension

## Boundary Cayley coordinates

Let \(A_{\min}\) be the closed minimal centered dilation operator and let

\[
A_{\max}=-A_{\min}^*.
\]

Assume the complete Green identity can be written with two boundary maps

\[
\Gamma_+,\Gamma_-:
\operatorname{Dom}A_{\max}\longrightarrow\mathcal H_{\partial}
\]

as

\[
\langle A_{\max}f,g\rangle
+
\langle f,A_{\max}g\rangle
=
\langle\Gamma_+f,\Gamma_+g\rangle_{\partial}
-
\langle\Gamma_-f,\Gamma_-g\rangle_{\partial}.
\]

The Hadamard wall--jump frame is exactly the finite endpoint instance of these
incoming and outgoing Cayley coordinates.

## Unitary sewing theorem

Let \(U:\mathcal H_{\partial}\to\mathcal H_{\partial}\) be unitary and define

\[
\operatorname{Dom}A_U
=
\{f\in\operatorname{Dom}A_{\max}:
\Gamma_-f=U\Gamma_+f\}.
\]

Then the boundary flux vanishes on \(\operatorname{Dom}A_U\), so \(A_U\) is
skew-symmetric.

It is skew-adjoint if the combined trace

\[
\Gamma=(\Gamma_+,\Gamma_-)
\]

is onto the complete boundary quotient and has kernel
\(\operatorname{Dom}A_{\min}\). Equivalently, the Green boundary space must
represent every deficiency direction, not only the visible observer ports.

Thus the source problem separates into:

1. complete trace theorem;
2. unitarity of the sewing map;
3. source identification of the graph condition.

The existing response graph addresses the second item. It does not alone prove
the first or third.

## Completeness audit by strata

The trace quotient must include every stratum that survives the Green form:

\[
\mathcal H_{\partial}
=
\mathcal H_{\mathrm{wall}}
\oplus
\mathcal H_{\mathrm{endpoint}}
\oplus
\mathcal H_{\mathrm{prime}}
\oplus
\mathcal H_{\mathrm{square}}
\oplus
\mathcal H_{\mathrm{conn}}
\oplus
\mathcal H_{\infty},
\]

after the authorized radical reductions and horizontal Fourier equalizer.

For each summand one must prove:

- the trace is continuous in its declared topology;
- every boundary coordinate has a lift in
  \(\operatorname{Dom}A_{\max}\);
- the lifts can be chosen with a uniform graph-norm bound;
- overlap corrections do not change previously fixed coordinates;
- the only common kernel is \(\operatorname{Dom}A_{\min}\).

Separate surjectivity of each coordinate is insufficient. The assembled trace
needs a bounded right inverse, or an equivalent open-mapping theorem, to rule
out mixed hidden deficiency.

## Characteristic operator

Fix a reference extension \(A_0\), for example
\(\Gamma_-=U_0\Gamma_+\). For spectral parameter
\(\lambda=s-\tfrac12\), let \(M(\lambda)\) be the source Weyl or
boundary-response operator obtained by solving

\[
(A_{\max}-\lambda)f=0
\]

and reading its two traces.

The extension eigenvalue condition is then a boundary equation of the form

\[
C_U(\lambda)c=0,
\qquad
C_U(\lambda)=U-M(\lambda),
\]

with the exact sign and fractional-linear convention frozen by the source
Cayley frame.

Hence

\[
\ker(A_U-\lambda)
\cong
\ker C_U(\lambda).
\]

This is the missing kernel isomorphism. It must be constructed by the Poisson
solution operator, not inferred from equality of determinants.

## Krein resolvent comparison

When the boundary triple is complete, the resolvent difference has the
schematic form

\[
(A_U-\lambda)^{-1}
-
(A_0-\lambda)^{-1}
=
\gamma(\lambda)
C_U(\lambda)^{-1}
\gamma^\sharp(\lambda),
\]

where \(\gamma(\lambda)\) is the Poisson operator.

This identity provides four needed gates at once:

1. extension eigenvalues are boundary-characteristic zeros;
2. multiplicities are controlled by the boundary pencil;
3. Schatten class of the resolvent difference is reduced to the response
   operators;
4. completion spectral pollution is excluded by resolvent convergence.

## Xi identification

The theta--Mellin--Poisson line functional already trivializes a chiral
determinant. To finish the identification theorem, it must be shown that this
line is specifically

\[
\operatorname{Det}C_U(s-\tfrac12),
\]

not merely the determinant of a parallel Euler loop.

The required equality is a determinant-line intertwiner between:

- the prime/square/connected Euler factorization;
- the endpoint and archimedean boundary factors;
- the Weyl response of the same extension \(A_U\).

After choosing the source trivializations, the ratio of the two determinant
sections must be holomorphic and nowhere zero. Matching scalar values on an
initial half-plane is then sufficient only if both sections are already
defined on the same determinant line.

## Quantitative completion theorem

Finite cutoffs require uniform control of:

\[
\|\Gamma_X\|,
\qquad
\|R_X\|,
\qquad
\|\gamma_X(\lambda)\|,
\qquad
\|U_X\|,
\qquad
\|U_X^{-1}\|,
\]

where \(R_X\) is a right inverse for the trace.

The critical lower quantity is the trace-surjectivity margin

\[
\delta_{\mathrm{tr},X}
=
\inf_{\|b\|=1}
\inf_{\Gamma_Xf=b}
\frac{1}{\|f\|_{\mathrm{graph}}}.
\]

Completion requires a positive compact-uniform lower bound. Every finite trace
may be onto while \(\delta_{\mathrm{tr},X}\to0\), producing hidden deficiency
at the limit.

This is upstream of the five global Green margins: without a complete
boundary triple, those margins are measured on an incomplete quotient.

## Hostiles

1. A unitary sewing graph on a proper subspace of the deficiency boundary.
2. Coordinatewise trace surjectivity without joint surjectivity.
3. A boundary characteristic determinant equal to \(\xi\) but attached to a
   different extension.
4. A correct finite Krein formula with right-inverse norms diverging.
5. A horizontal Fourier equalizer that removes a genuine deficiency
   coordinate.
6. A response operator with the correct scalar trace but wrong ordered
   boundary action.

## Verdict

The remaining extension theorem has a standard exact form: construct a
complete boundary triple for centered dilation, prove that source sewing is a
unitary graph in its Cayley coordinates, and identify the theta--Mellin
determinant with the resulting boundary characteristic operator.

The next irreducible calculation is the joint trace-surjectivity theorem. It
must produce a uniformly bounded right inverse on the stratified horizontal
carrier. Only then does the already established unitary response sewing become
a skew-adjoint, rather than merely skew-symmetric, RH operator.
