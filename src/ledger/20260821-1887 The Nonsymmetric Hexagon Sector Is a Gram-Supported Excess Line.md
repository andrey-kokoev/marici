# 1887 — The Nonsymmetric Hexagon Sector Is a Gram-Supported Excess Line

## Remaining sector

Entry 1886 closes the stabilizer-fixed six-site critical sector.  Retain all
three free squared loop coordinates

\[
x=y_1^2,qquad v=y_3^2,qquad w=y_5^2
\]

and specialize the denominator-cleared \(\kappa\)-Rees cover to the regular
hexagon exceptional fiber.

## Exact exceptional system

The two strict-transform cover equations are

\[
F_E=-\frac1{32}L^2,
\qquad
G_E=-\frac14M,
\]

where

\[
L=-2+x-6z+4v+w,
\qquad
M=-6+2x-6z+5v-w.
\]

All three \(2\times2\) critical Jacobian minors are nonzero scalar multiples
of the same linear form \(L\).  Thus the critical scheme is exactly

\[
L=M=0.
\]

Solving gives the affine line

\[
\boxed{
x=\frac83+4z-3v,
\qquad
w=-\frac23+2z-v,
}
\]

with \(v\) free.  It lies over every \(z\) and contains no symmetric point
\(x=v=w\).

## Narrow result

The nontrivial stabilizer-character sector survives only as an excess
critical line supported on the pre-existing Gram exceptional divisor.  It
does not project to a finite discriminant in \(z\):

\[
\boxed{
\text{no homogeneous six-site }z\text{-divisor arises from this incidence.}
}
\]

The doubled equation \(L^2=0\) may carry a derived Cartier/excess coefficient
object.  That object has not been computed and must not be replaced by the
reduced line.  Nevertheless, neither the reduced nor doubled support is a new
Carrier stratum; both live on the frozen Gram-degeneracy support.

## Meta-level consequence

The six-site test separates three notions sharply:

1. the Carrier incidence is source-admitted;
2. the generic Gram-normal family has a symmetric Landau divisor away from
   the exceptional fiber;
3. the homogeneous specialization retains only Gram-supported excess, not a
   physical energy discriminant.

This is another positive H2 pattern: shared incidence and excess calculus,
with coefficient support changing under kinematic specialization.

## Next falsifier

Compute the derived excess object of \(F_E=L^2\), \(G_E=M\): its Koszul
homology, Cartier length, and compatibility with the nine source-term
restriction maps.  The test is whether it is exhausted by the existing Gram
Gysin/excess calculus or requires an undeclared incidence operation.

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_symmetric_landau.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-symmetric-landau.json`
- allocator claim: `seqclaim-ff914e5dcac885784da16215`
- epistemic event: `ev-000000002249-53eab9e1-b3fa-4e25-83a6-6f0a7b585ca6`
