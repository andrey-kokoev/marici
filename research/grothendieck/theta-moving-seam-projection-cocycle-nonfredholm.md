# The moving seam is an exact projection cocycle but is non-Fredholm on \(L^2\)

## 1. Half-line projection

Let

\[
  P=M_{\mathbf 1_{[0,\infty)}}
\]

on \(L^2(\mathbb R)\), and use translations

\[
  (T_af)(u)=f(u+a).
\]

The transported cut is

\[
  P_a=T_aPT_a^{-1}
  =
  M_{\mathbf 1_{[-a,\infty)}}.
\]

For \(a>0\), the seam difference is therefore

\[
  C_a=P-P_a
  =
  -M_{\mathbf 1_{[-a,0)}}.
\]

It is exactly the oriented finite interval swept out by the moving cut.

## 2. Cocycle law

Transport by two displacements gives

\[
  P_{a+b}=T_aP_bT_a^{-1}.
\]

Consequently

\[
  C_{a+b}
  =
  C_a+T_aC_bT_a^{-1}
\]

with the corresponding convention for oriented intervals. This is the exact
moving-endpoint one-cocycle behind finite sewing terms such as

\[
  B_{a,p}(z)
  =
  \int_0^{\log p}h_a(u)e^{izu}\,du.
\]

The scalar seam current is obtained only after pairing the universal
projection cocycle with the completed source.

## 3. Non-Fredholm obstruction

Multiplication by the indicator of a positive-measure interval has
infinite-dimensional range and is not compact on \(L^2(\mathbb R)\).
Therefore

\[
  P-P_a
\]

is not compact for \(a\ne0\). The pair of projections \((P,P_a)\) is not a
Fredholm pair in the standard restricted-Grassmannian sense.

\[
\boxed{
\text{moving seam on continuum }L^2
\not\Longrightarrow
\text{a determinant-line transition}.}
\]

This blocks another automatic overlap-to-incidence construction. The finite
length of the swept interval does not mean finite operator rank.

## 4. Why scalar sewing looked finite

After pairing with one source state, \(C_a\) produces one scalar interval
integral. That scalar is finite and may appear to be a finite-rank boundary
channel. Before compression, however, the seam carries every \(L^2\) mode
supported on the interval.

Thus:

\[
\boxed{
\text{finite scalar seam current}
\ne
\text{finite-rank operator defect}.}
\]

This is the continuum analogue of the rule that a finite fiber need not be a
singleton fiber.

## 5. Required analytic compression

To obtain a Fredholm pair one needs a source-authorized subspace
\(\mathcal H_\Phi\subset L^2\) on which the compressed seam difference

\[
  \Pi_\Phi(P-P_a)\Pi_\Phi
\]

is compact, Hilbert--Schmidt, or trace class. Plausible analytic mechanisms
include Hardy, de Branges, or reproducing-kernel compression, but the space
and projection must be derived from the completed theta source before the
determinant is formed.

Arbitrary spectral compression is inadmissible because it can manufacture
compactness and a desired determinant after seeing \(X\).

## 6. Mixed quarter-turn

Fourier rotation conjugates the sharp position cut to a Hardy-type frequency
projection. Products and commutators of the two cuts become
Toeplitz/Hankel-style operators. This is the first setting in which the seam
cocycle may acquire compact off-diagonal blocks.

The precise next calculation is:

\[
  H_a
  =
  P\,\mathcal F C_a\mathcal F^{-1}(I-P),
\]

or its source-weighted analogue. Determine its operator class and whether the
completed theta vacuum selects a trace-class relative determinant. A result
that holds for every smooth positive vacuum supplies typing but no RH
orientation.

## 7. Falsifiers

The determinant programme fails at this gate if:

1. the source-derived compression leaves \(C_a\) noncompact;
2. compactness depends on an arbitrary regulator;
3. different admissible compressions give different divisors; or
4. the resulting determinant is inserted from the scalar overlap rather than
   derived from the compressed transport.

## 8. Scope

The projection formula, cocycle law, infinite-rank range, and noncompactness
on continuum \(L^2\) are exact. They show that the moving seam needs an
analytic compression before Fredholm geometry exists. No canonical
compression, trace-class holonomy, determinant identity, or RH theorem is
constructed.
