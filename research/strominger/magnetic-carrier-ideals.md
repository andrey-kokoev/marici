# Observation-route ideals and their scope

The carrier method has a coordinate-independent formulation.  For an
observation `R` with independent transport routes having coefficients
`c_1,...,c_s`, define its route ideal

\[
\mathcal I_R=(c_1,\ldots,c_s).
\]

A preferred chart chooses one generator.  That generator may vanish while
the ideal remains nonzero.  The observation itself is lost only on

\[
V(\mathcal I_R)=\{c_1=\cdots=c_s=0\}.
\]

This gives the invariant distinction:

\[
\begin{array}{c|c}
\text{one chosen generator vanishes}&\text{chart boundary}\\
\text{the whole route ideal vanishes}&\text{observation loss}
\end{array}
\]

## Magnetic route ideals

For `q=1`, the relevant ideal is principal:

\[
\mathcal I_{q=1}=\bigl((g-2)4^{\overline g}\bigr).
\]

In the integer domain `g>=2`, its zero locus is `g=2` and produces the
primitive circuit `(1,-1)`.

For the odd low-grade transverse observation,

\[
\mathcal I_{R_2}=(L_{g,d},R_{g,d}),
\]

with

\[
L_{g,d}=-\left(2dg+2d-g^2-11g-4\right)
\frac{(d+g-3)!}{(d-2)!},
\]

\[
R_{g,d}=\frac{g(d-4)(d-3)(g-2)(g-1)(g+3)}{2}
\frac{(d+g-3)!}{d!}.
\]

On admissible integers `g>=2`, odd `d>=3`, their common zero locus is

\[
V(\mathcal I_{R_2})=\{(2,5)\}.
\]

It produces `(1,-3,2)`.

At the even chart divisor, the route ideal contains both the preferred
coordinate `d-g-8` and the transverse coordinate `tau_g`:

\[
\mathcal I_{\mathrm{even}}=(d-g-8,\tau_g).
\]

The first generator vanishes on the divisor, but the second is nonzero at
every admissible integral point.  Hence the ideal does not vanish and no
observation is lost.

## Relation to the determinantal ideal

The route ideal is not automatically identical to the maximal-minor or
Fitting ideal of the full matrix.  It detects rank loss caused by simultaneous
failure of identified transport routes.  A determinant can, in principle,
also vanish through cancellation while every named carrier is nonzero.

In the magnetic integer domain that alternative is excluded by the completed
rank theorem and the odd-core Diophantine lemma: route-ideal loss and actual
rank loss select exactly the same two components.  Over a continuous or
complexified parameter space, the odd obstruction polynomial `P(g,d)=0`
defines a larger algebraic hypersurface than the common-zero locus
`L=R=0`.  These objects must not be conflated.

Therefore the transferable workflow is

\[
\boxed{
\text{route ideals for explanation}
\quad+\quad
\text{Fitting ideals for completeness}.
}
\]

Route ideals say which independently constructed observation channels failed.
Fitting ideals detect every rank defect, including cancellation mechanisms not
captured by the proposed route decomposition.  Agreement between them is a
theorem to prove or a falsifier to test, not a definition.
