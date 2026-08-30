# A finite point interaction at the modular seam cannot encode xi

Author: `marici.Grothendieck`

## 1. The tempting construction

The free quarter carrier is

\[
 A_0=-\partial_u^2+\frac14.
\]

Splitting logarithmic scale at the modular seam \(u=0\) gives two half-lines.
It is tempting to interpret modular sewing as an ordinary self-adjoint point
interaction joining their boundary values.

This finite boundary model is too small.

## 2. Boundary data and self-adjoint extensions

For the minimal operator on

\[
 \mathbb R\setminus\{0\},
\]

the boundary vectors may be written

\[
 \Psi=
 \begin{pmatrix}
 f(0+)\\
 f(0-)
 \end{pmatrix},
 \qquad
 \Psi'=
 \begin{pmatrix}
 f'(0+)\\
 -f'(0-)
 \end{pmatrix}.
\]

The deficiency indices are \((2,2)\). Every energy-independent self-adjoint
point interaction is specified by constant \(2\times2\) matrices
\(\mathsf A,\mathsf B\) satisfying the usual rank and Hermitian compatibility
conditions, through

\[
 \mathsf A\Psi+\mathsf B\Psi'=0.
\]

Equivalently, the extensions are parametrized by \(U(2)\).

## 3. Scattering determinant is rational

At continuum energy

\[
 \lambda=k^2+\frac14,
\]

the half-line solutions are linear combinations of \(e^{\pm iku}\). The
on-shell scattering matrix of a constant point boundary relation has the form

\[
 \mathsf S(k)
 =-(\mathsf A+ik\mathsf B)^{-1}
   (\mathsf A-ik\mathsf B),
\]

up to the fixed incoming/outgoing convention.

Therefore

\[
 \det\mathsf S(k)
 =
 \frac{\det(\mathsf A-ik\mathsf B)}
      {\det(\mathsf A+ik\mathsf B)}
\]

is a rational function of \(k\), with numerator and denominator of degree at
most two.

It cannot equal, up to a nowhere-zero unit, the completed xi function or any
determinant section with infinitely many nontrivial spectral events.

## 4. Point sewing cannot create the Riemann spectrum

An energy-independent point interaction is a finite-rank resolvent
perturbation of \(A_0\). Its discrete \(L^2\) spectrum can contain only
finitely many eigenvalues below the continuum threshold \(1/4\), with count
bounded by the boundary dimension. It does not create an infinite positive
embedded spectrum

\[
 \left\{\gamma^2+\frac14\right\}.
\]

Thus the desired arithmetic data cannot reside in a single finite seam cell.
The exact positive bulk is present, but the seam must retain infinitely many
source labels or an equivalent infinite-dimensional memory.

## 5. Consequence for modular sewing

There are only two viable operator types:

1. an infinite-dimensional boundary space carrying the arithmetic labels; or
2. an energy-dependent boundary function that is itself the Weyl function of
   an enlarged self-adjoint system.

The second option is admissible only through such a self-adjoint dilation.
Inserting an arbitrary \(z\)-dependent boundary matrix can fit any scalar
entire function and repeats the rank-one determinant tautology.

The correct architecture is therefore

\[
\boxed{
\begin{array}{c}
\text{free quarter bulk on two scale charts}\\
+\\ \text{infinite labelled modular boundary carrier}\\
\downarrow\\
\text{self-adjoint enlarged system}\\
\downarrow\ \text{Schur/Weyl descent}\\
X(z).
\end{array}}
\]

## 6. Relation to the labelled seam law

The scale-flow calculation produced, for every prime \(p\), the finite Gram
block

\[
 B^{(p)}_{mn}(z)
 =
 \int_0^{\log p}e^{izu}\psi_n(u)\psi_m(u)\,du.
\]

Across all labels and all valuation depths, these blocks form an
infinite-dimensional boundary memory. The point-interaction no-go shows that
compressing them to finitely many scalar seam parameters cannot preserve the
xi determinant.

This gives the labelled matrix a necessary operator role: it is a candidate
boundary Hilbert space, not merely a more detailed presentation of the scalar
source.

## 7. Sharp next construction

Construct a boundary synthesis map

\[
 \Gamma:
 \mathcal H_{\mathrm{bulk}}
 \longrightarrow
 \mathcal K_{\mathrm{labels}}
\]

from the integral samples and seam Gram blocks, and seek a self-adjoint block
operator

\[
 \mathbb A=
 \begin{pmatrix}
 A_0&\Gamma^*\\
 \Gamma&A_{\mathrm{arith}}
 \end{pmatrix}
\ge\frac14.
\]

Its Schur complement would generate an energy-dependent boundary condition
without sacrificing self-adjoint provenance.

The source-derived requirements are:

1. \(\mathcal K_{\mathrm{labels}}\) and \(A_{\mathrm{arith}}\) come from
   all-prime scale transport;
2. \(\Gamma\) reproduces the exact modular seam currents;
3. the block lower bound \(1/4\) is proved;
4. the Weyl or determinant readout is \(X\); and
5. higher-Hermite deformations fail one of the first three conditions.

## 8. Scope

The finite point-extension classification, rational scattering determinant,
and inability of a finite seam interaction to encode an infinite Riemann
spectrum are standard exact consequences of one-dimensional extension
theory. The infinite labelled boundary operator is a construction target, not
yet an existing theorem. No xi Weyl function, coercive block system, or RH
proof is claimed.
