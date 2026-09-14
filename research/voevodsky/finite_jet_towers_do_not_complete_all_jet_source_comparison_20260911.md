# Finite jet towers do not complete the all-jet source comparison

## Question

Can the twelve-point sampled trace be repaired by adjoining a bounded number of derivatives at every node?

## Claim boundary

For every finite derivative depth \(m\), the resulting Hermite sampling map still has a nonzero polynomial kernel on an unrestricted polynomial or function carrier. This does not address an actual infinite jet object, nor does it deny reconstruction on a separately declared finite-dimensional source space.

## Finite-depth obstruction

Let

\[
a(r)=\prod_{j=0}^{11}(r-r_j),
\qquad
r_j=\frac{j+1/2}{12}.
\]

For a fixed finite derivative depth \(m\), define

\[
p_m(r)=a(r)^{m+1}.
\]

At each node \(r_j\), the polynomial \(p_m\) has a zero of multiplicity \(m+1\). Therefore

\[
p_m^{(k)}(r_j)=0
\quad
(0\leq k\leq m),
\]

while

\[
p_m^{(m+1)}(r_j)\ne0.
\]

Thus retaining derivatives through depth \(m\) at all twelve nodes fails to distinguish \(p_m\) from zero. The obstruction degree is \(12(m+1)\).

The quantifiers are:

\[
\text{for every finite }m\text{, there exists a nonzero }p_m
\text{ annihilated by the depth-}m\text{ record}.
\]

This does not assert that one polynomial defeats all depths simultaneously.

## Exact finite positive result

Hermite sampling through depth \(m\) gives \(12(m+1)\) scalar conditions. It is an isomorphism on polynomials of degree at most

\[
12(m+1)-1.
\]

The associated confluent Vandermonde matrix has full rank. Hence each finite stage is faithful on its matching finite-degree source, but no stage is faithful on the union of all polynomial degrees.

## Consequence

Adding one, two, or any fixed number of derivative ports does not bridge the current synthetic carrier to an unrestricted all-jet trace. A valid bridge must instead provide one of:

- an actual infinite compatible jet object and its topology;
- a source-derived degree bound;
- a completion theorem proving finite stages detect the intended equivalence;
- an analytic reconstruction theorem with domain and convergence control.

Without such an arrow, finite-depth success cannot be promoted to all-jet faithfulness.

## Disposition

The proposed finite-derivative repair is rejected as a general source comparison. It remains valid only after declaring the exact finite-degree source restriction corresponding to its depth.
