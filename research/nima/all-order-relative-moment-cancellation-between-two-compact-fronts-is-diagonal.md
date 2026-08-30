# All-order relative moment cancellation between two compact fronts is diagonal

## Theorem

Let \(\varphi_-,\varphi_+\in C_c^\infty(\mathbb R)\). Suppose their moments agree at every order:
\[
\int x^j\varphi_-(x)\,dx
=
\int x^j\varphi_+(x)\,dx
\qquad(j\ge0).
\]
Then
\[
\varphi_-=\varphi_+.
\]

Apply the compact-front moment theorem to
\[
\psi=\varphi_- - \varphi_+.
\]
Every moment of \(\psi\) vanishes, so \(\psi=0\).

Equivalently, the full moment map
\[
M_\infty:
C_c^\infty(\mathbb R)
\longrightarrow
\mathbb C^{\mathbb N},
\qquad
\varphi\longmapsto(m_0,m_1,\ldots)
\]
is injective.

## Relative consequence

If two compact chart fronts cancel their complete principal-value asymptotic expansions through equality of every moment, their anti-diagonal class vanishes:
\[
[\varphi_- - \varphi_+]=0.
\]

Thus passing from one compact front to a pair of compact fronts does not evade the all-moment obstruction. Exact all-order moment matching forces the pair onto the diagonal chart direction, which is precisely the orientation-free sector.

This closes the tempting construction
\[
\text{compact front}_-
-
\text{compact front}_+
\]
with identical Hilbert tails but a nonzero compactly supported odd residue. Such a pair cannot exist.

## Distinction from asymptotic cancellation

The theorem concerns equality of the full moment sequence. It does not say that two noncompact distributions with the same asymptotic germ must coincide. Nor does it exclude cancellation involving:

- a noncompact archimedean carrier;
- boundary values of holomorphic functions in different half-planes;
- hyperfunctions with zero ordinary moment germ but nontrivial jump class;
- a mapping-cone coordinate not represented by a scalar compact front.

Those are now the only viable source types for a nonzero residual after complete algebraic-tail cancellation.

## Canonical splitting implication

The infinite singular-moment coordinate is not merely a nuisance on compact fronts: it is faithful. Its kernel is zero. Therefore defining the residual as
\[
\ker M_\infty
\]
inside the compact-front space produces no odd residual at all.

A source-authorized rank-three extension must enlarge the carrier before taking this kernel. The residual coordinate must be cohomological, hyperfunctional, or otherwise relative; it cannot be a hidden subspace of the original compact front.

## Hostile

Any proposed compact two-chart constructor claiming

1. equality of all moment jets,
2. a nonzero anti-diagonal compact residual,

is internally inconsistent. Finite numerical moment checks cannot detect this if they stop at bounded order, but the all-order theorem rejects it.

## Revised frontier

The search is reduced to a topology-changing source map:
\[
\text{two compact chart fronts}
\longrightarrow
\text{noncompact or cohomological relative carrier}.
\]

The next audit must locate such a map in the existing Fourier–Tate, archimedean, or causal-history source data. Without it, the rank-three extension remains an algebraic template with no nonzero residual realization.
