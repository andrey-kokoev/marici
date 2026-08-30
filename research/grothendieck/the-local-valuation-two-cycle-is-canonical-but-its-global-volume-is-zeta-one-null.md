# The local valuation two-cycle is canonical but its global volume is zeta-one null

## Canonical local scalarization

At a finite place \(p\), let

\[
f_{0,p}=1_{\mathbb Z_p},
\qquad
f_{1,p}=1_{p\mathbb Z_p}.
\]

These are not fitted probes.  They are the vacuum valuation cell and its first
proper radial subcell.  Both belong to the Schwartz--Bruhat test space.

Use the ordered boundary observers

\[
\epsilon_p(f)=f(0),
\qquad
\mu_p(f)=\int_{\mathbb Q_p}f(x)\,dx
\]

with self-dual Haar normalization.  Then

\[
\epsilon_p(f_{0,p})=epsilon_p(f_{1,p})=1,
\]

and

\[
\mu_p(f_{0,p})=1,
\qquad
\mu_p(f_{1,p})=p^{-1}.
\]

The local test two-cycle

\[
\chi_p=f_{1,p}\wedge f_{0,p}
\]

therefore evaluates against the oriented boundary bivector as

\[
(\epsilon_p\wedge\mu_p)(\chi_p)
=1-p^{-1}>0.
\]

This closes local scalarization without a Hilbert pivot.  The valuation
filtration itself supplies the required two-plane and fixes its orientation.

## Restricted-product obstruction

If the local determinant lines are aggregated multiplicatively through a
finite prime cutoff \(X\), their oriented volume is

\[
V_X=\prod_{p\le X}(1-p^{-1}).
\]

Euler's divergence of the prime harmonic series gives

\[
V_X\longrightarrow0.
\]

Equivalently, the inverse Euler product at \(s=1\) vanishes.  Thus every
finite place supplies a nondegenerate canonical two-cycle, while their naive
global determinant volume collapses at completion.

This is not failure of local transversality.  It is a determinant-line
completion anomaly.  The finite products remain positive, but their
logarithms accumulate the prime-square divergence

\[
-\log V_X
=
\sum_{p\le X}\frac1p+O(1).
\]

Here the local area is quadratic in the primitive amplitude
\(p^{-1/2}\).  Therefore the divergent term \(p^{-1}\) is the \(k=2\)
prime-square channel, not the \(k=1\) primitive channel.  The square current
measures loss of the global oriented volume.  The primitive channel retains
the odd coorientation that defined the bivector in the first place.

## Interpretation

The boundary bivector construction and the valuation two-cycle together solve
the local typing problem completely:

1. two covectors form an exterior two-form;
2. two adjacent valuation cells form a test two-cycle;
3. their evaluation is the positive local factor \(1-p^{-1}\).

The obstruction is global normalization.  A nonzero completed scalar current
requires a relative determinant line retaining the divergent prime-square
countercurrent.  Dividing by the vanishing product after completion would be
circular unless the renormalization is derived from the same finite-cutoff
source construction.

This gives the next exact target: construct a relative product in which

\[
\prod_{p\le X}(1-p^{-1})
\]

and the prime-square boundary current are retained as a paired determinant
object before taking \(X\to\infty\).  The desired global scalarization must be
a finite nonzero relative volume, not an ordinary restricted product of local
areas.

## Falsifier

Any claimed ordinary global test two-cycle whose local valuation minors are
\(1-p^{-1}\) must reproduce \(V_X\).  If it claims a nonzero ordinary limit
without an explicit prime-square relative factor, it contradicts the Euler
product calculation.  Conversely, a proposed relative completion must replay
every finite \(V_X\) before its countercurrent is applied.
