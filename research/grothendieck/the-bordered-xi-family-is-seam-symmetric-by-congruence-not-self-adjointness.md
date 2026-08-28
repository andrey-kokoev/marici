# The bordered xi family is seam-symmetric by congruence, not self-adjointness

Author: `marici.Grothendieck`

## Question

Does the source-bordered determinant family hide an ordinary self-adjoint
operator on the critical line?

## Incidence symmetrization

Start from

\[
\mathcal M_s=
\begin{pmatrix}
s&0&1\\
0&s-1&1\\
1&-1&H(s)
\end{pmatrix},
\qquad
H(1-s)=H(s).
\]

Multiplying the second endpoint equation by its incidence sign gives

\[
K_s=
\operatorname{diag}(1,-1,1)\mathcal M_s
=
\begin{pmatrix}
s&0&1\\
0&1-s&-1\\
1&-1&H(s)
\end{pmatrix}.
\]

This matrix is complex symmetric:

\[
K_s^T=K_s.
\]

Put \(z=s-1/2\), and pass to the symmetric and antisymmetric endpoint
coordinates

\[
e_+=\frac{e_0+e_1}{\sqrt2},
\qquad
e_-=\frac{e_0-e_1}{\sqrt2}.
\]

The congruent matrix becomes

\[
A_z=
\begin{pmatrix}
1/2&z&0\\
z&1/2&\sqrt2\\
0&\sqrt2&H(1/2+z)
\end{pmatrix}.
\]

The bulk couples only to the antisymmetric endpoint coordinate. This is a
newly visible structural selection rule.

## Real symmetric seam form

Apply the constant phase congruence

\[
C=\operatorname{diag}(1,i,i).
\]

On the critical line \(z=it\), the matrix

\[
Q_t=C^TA_{it}C
=
\begin{pmatrix}
1/2&-t&0\\
-t&-1/2&-\sqrt2\\
0&-\sqrt2&-H(1/2+it)
\end{pmatrix}
\]

is real symmetric. Since \(H(1/2+it)\) is real,

\[
\det Q_t=-2\xi(1/2+it).
\]

Thus the source family does possess a canonical real quadratic-form
presentation on the seam. The half offset appears as the fixed diagonal pair
\((1/2,-1/2)\), and the spectral ordinate appears as their off-diagonal
comparison.

## Constant Hermitian-metric no-go

This seam congruence is not an ordinary self-adjoint realization. Suppose a
constant Hermitian matrix \(G\) satisfied

\[
\mathcal M_{1/2+it}^*G
=
G\mathcal M_{1/2+it}
\]

for every real \(t\). Write

\[
G=
\begin{pmatrix}
G_\partial&b\\
b^*&c
\end{pmatrix}.
\]

The endpoint--endpoint block of the identity has a term

\[
-itG_\partial=itG_\partial,
\]

while all incidence terms are independent of \(t\). Hence

\[
G_\partial=0.
\]

The endpoint--bulk block then reads componentwise

with a fixed scalar \(k_j\):

\[
(\overline d_j(t)-H(1/2+it))b_j
=
k_j.
\]

where \(\overline d_j(t)\) contains \(-it\), while
\(H(1/2+it)\) is real. Holding for every \(t\) forces \(b=0\).
The remaining incidence term forces \(c=0\). Therefore

\[
G=0.
\]

There is no nonzero constant Hermitian metric, definite or indefinite, that
makes the original bordered family self-adjoint along the whole seam.

## Interpretation

The relevant symmetry has three distinct types:

1. reciprocal reflection is a left-right equivalence;
2. boundary incidence produces a complex-symmetric bilinear form;
3. a constant phase congruence makes that form real symmetric on the seam.

None is a similarity to a fixed self-adjoint spectral operator. Treating them
as interchangeable would erase precisely the incoming/outgoing distinction
that generated the endpoint packet.

## Hostile tests

- Any claimed constant Hilbert or Krein metric must satisfy the block identity
  above; its only solution is zero.
- A parameter-dependent metric is not accepted without an independent source
  constructor, because it can be fitted pointwise.
- Real symmetry on the seam does not exclude zeros there or away from it; it
  only identifies the seam as the native real-form locus.

## Claim boundary

This proves an exact seam real form and a constant-metric no-go for the
three-dimensional bordered family. It does not exclude a larger conservative
linearization, a parameter-dependent source metric, or a rigged
infinite-dimensional operator.

## Disposition

The direct finite Hilbert--Pólya interpretation is closed. The live direction
is a source-derived conservative linearization that enlarges the bulk
coordinate rather than fitting a metric to the compressed scalar entry
\(H(s)\).
