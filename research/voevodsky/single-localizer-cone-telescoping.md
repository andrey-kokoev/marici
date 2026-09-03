# Single localizer cone by telescoping

## Question

Are both Hausdorff cone families independently RH-strength, or can decay reconstruct the Hankel cone from one localizer cone?

## Claim boundary

The two-cone gate is reduced to one localizer family plus decay. Here \(H\) must denote a decaying normalized target. The raw endpoint-bearing heat function can contain \(e^{t/4}\) and does not satisfy the required decay. Positivity of the normalized explicit arithmetic localizer remains open.

## Hankel and localizer matrices

For positive \(t,h\), define

\[
M_h(t)_{ij}=H(t+(i+j)h).
\]

Its \(1-y\) localizer is

\[
L_h(t)=M_h(t)-M_h(t+h).
\]

Normalize it as the matrix divided difference

\[
Q_h(t)=\frac{L_h(t)}{h}.
\]

Positivity of \(L_h(t)\) is equivalent to positivity of \(Q_h(t)\).

## Telescoping reconstruction

For every positive integer \(R\),

\[
M_h(t)
=
\sum_{r=0}^{R-1}L_h(t+rh)
+
M_h(t+Rh).
\]

Suppose:

1. \(L_h(s)\) is positive semidefinite for every positive rational \(s,h\) and every finite matrix size;
2. \(H(s)\to0\) as \(s\to\infty\).

For fixed matrix size, every entry of \(M_h(t+Rh)\) tends to zero. Finite-dimensional positive cones are closed, so

\[
M_h(t)
=
\sum_{r\geq0}L_h(t+rh)
\geq0.
\]

Therefore the ordinary Hankel cone is not an independent positivity gate. It follows from the localizer cone and decay.

## Divided-difference interpretation

The normalized localizer satisfies

\[
Q_h(t)
=
\frac{M_h(t)-M_h(t+h)}{h}.
\]

As \(h\) tends to zero, it approaches the matrix built from \(-H'\). At finite \(h\), it is the interval average of that derivative. This is the precise bridge between:

- the undifferentiated finite-difference chart;
- the reported outer-derivative Stieltjes density;
- the compact Hausdorff localizer.

Thus the single divided-difference kernel is not merely another presentation. Its positive matrix cone generates the missing Hankel cone by telescoping.

## GNS consequence

Once \(L_h(t)\geq0\) and decay reconstruct \(M_h(t)\geq0\), the prior GNS construction yields

\[
0\leq Y_h\leq1.
\]

Compact determinacy supplies rational cross-step semigroup coherence, and source continuity gives the strongly continuous extension. Hence all later positive objects follow from the one localizer family.

## Exact fixtures

For positive atoms with contraction coordinates \(1/4\) and \(2/3\), the checker verifies

\[
L=VW(1-Y)V^*\geq0,
\]

six finite telescoping identities, and entrywise decay of the remainder. A signed atomic weight produces a negative localizer determinant.

## Revised proof boundary

The remaining RH-strength target is now one matrix inequality:

\[
\left(
H(t+(i+j)h)-H(t+(i+j+1)h)
\right)_{i,j=0}^{r-1}
\geq0
\]

for every finite rank \(r\) and rational positive \(t,h\), together with the already expected decay of \(H\).

This target uses only undifferentiated values of the completed explicit function.

## No implicit finiteness

No bounded rank verifies the family. A finite negative determinant refutes positivity, but positive matrices through any fixed rank do not establish the universal cone. A source-derived Gram or positive J-fraction factor must generate every rank compatibly.

## Disposition

The two-cone Hausdorff gate collapses to a single localizer cone plus decay. The first missing object is a source-derived positive factorization of the matrix divided-difference kernel \(Q_h(t)\). All Hankel, semigroup, Bernstein, entire-kernel, and Gram positivity structures then follow functorially.

## Verification

- `research/voevodsky/single-localizer-cone-telescoping-v1.json`
- `research/voevodsky/checkers/check_single_localizer_cone_telescoping.py`
- `research/voevodsky/results/single_localizer_cone_telescoping.json`
