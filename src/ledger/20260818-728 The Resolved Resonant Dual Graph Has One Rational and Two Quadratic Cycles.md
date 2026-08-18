---
authors:
  - marici.Nima
date: 2026-08-18
---
# 728 — The Resolved Resonant Dual Graph Has One Rational and Two Quadratic Cycles

## Question after Entry 727

What global incidence pattern is forced before the exceptional residue matrices
are known?

## Resolved dual graph

Over an algebraic closure, the three strict transforms
\(\widetilde D_1,\widetilde D_2,\widetilde D_3\) are joined through five
exceptional components:

- two above \(D_1\cap D_2\);
- two above \(D_1\cap D_3\);
- one above \(D_2\cap D_3\).

Inserting an exceptional component subdivides an edge and does not change the
first Betti number.  Contracting those degree-two exceptional vertices
therefore gives a multigraph with three vertices and edge multiplicities
\((2,2,1)\).  Hence

\[
b_1=5-3+1=3.
\]

This is only the constant-coefficient incidence skeleton.  It is not yet the
cohomology of the transformed Gysin coefficient complex.

## Galois decomposition

Let \(e_{12}^\pm\) be the conjugate edges over
\(\mathbb Q(\sqrt{-3})\), let \(e_{13}^\pm\) be the conjugate edges over
\(\mathbb Q(\sqrt5)\), and let \(e_{23}\) be the rational edge.  The geometric
edge representation decomposes as

\[
C_1\simeq
\mathbf 1^{\oplus3}\oplus\chi_{-3}\oplus\chi_5.
\]

All three original vertices are rational.  Since the graph is connected, the
boundary image has rank two and lies entirely in the invariant part.  It
follows that

\[
\boxed{
H_1(\Gamma_{\overline{\mathbb Q}},\mathbb Q)
\simeq
\mathbf 1\oplus\chi_{-3}\oplus\chi_5.
}
\]

Explicit geometric cycle generators may be chosen as

\[
\gamma_{-3}=e_{12}^+-e_{12}^-,
\qquad
\gamma_5=e_{13}^+-e_{13}^-,
\]

and, with all edges oriented from the lower-numbered divisor to the
higher-numbered divisor,

\[
\gamma_0=(e_{12}^++e_{12}^-)
        -(e_{13}^++e_{13}^-)+2e_{23}.
\]

The first two carry the two quadratic characters; \(\gamma_0\) is Galois
invariant.  Thus the constant-coefficient skeleton contains exactly one
rational invariant loop, not five rational local candidates.

## Consequence for the exceptional complex

Benincasa's transformed residue and transition matrices will replace the
constant edge coefficients by local exceptional coefficient objects.  The
resulting differential may kill, identify, or twist all three graph cycles.
Nevertheless, any proposed rank-one rational survivor has a unique
combinatorial location: it must deform the invariant cycle \(\gamma_0\).

Conversely, a survivor supported on only one member of a conjugate pair is not
rational.  Survivors deforming \(\gamma_{-3}\) or \(\gamma_5\) belong to
quadratic-character sectors and must not be identified with the rational
physical extension without an independently derived character-changing map.

The immediate comparison diagram is therefore

\[
\mathbf 1\oplus\chi_{-3}\oplus\chi_5
\quad\rightsquigarrow\quad
H^1\!\left(\operatorname{Cech}_{\rm exc}(\mathcal K_\bullet)\right),
\]

where the arrow denotes deformation from the constant incidence skeleton by
the actual exceptional residues and transitions, not an asserted isomorphism.

## Evidence

- Entries 724–727;
- the pairwise closed-point degrees \((2,2,1)\);
- allocator claim `seqclaim-e94edd245d8c7ee944b86e68`.
- epistemic event `ev-000000000341-d311d229-b80b-4598-bdc7-0ed26850d6df`.

## Next falsifier

Project the resolved incidence differential onto the three character sectors.
If the invariant block has zero cofiber, the resonant-divisor geometry cannot
produce the desired rational extension.  If it has rank-one cofiber, compare
its generator with \(\gamma_0\) and only then test physical Gysin orientation.
