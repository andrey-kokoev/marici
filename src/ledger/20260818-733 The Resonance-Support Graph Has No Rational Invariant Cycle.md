---
authors:
  - marici.Nima
date: 2026-08-18
---
# 733 — The Resonance-Support Graph Has No Rational Invariant Cycle

## Question after Entries 731–732

Entry 728 computed the cycle representation of the complete resolved dual
graph.  Entry 731 now proves that the rational weighted exceptional component
over \(D_2\cap D_3\) has invertible residue and no positive-order extension
resonance.  What remains after retaining only edges that actually carry local
extension-resonance coefficients?

## Resonance-support subgraph

The complete geometric multigraph has edge multiplicities \((2,2,1)\) between
the three rational divisor vertices.  Its invariant cycle required the
rational edge:

\[
\gamma_0=(e_{12}^++e_{12}^-)
         -(e_{13}^++e_{13}^-)+2e_{23}.
\]

Entry 731 removes \(e_{23}\) from the local exceptional-resonance support.
The remaining graph \(\Gamma_{\rm res}\) has three vertices and four edges,
two in each conjugate pair.  It remains connected, so

\[
b_1(\Gamma_{\rm res})=4-3+1=2.
\]

Its edge representation is

\[
C_1(\Gamma_{\rm res})
\simeq
\mathbf1^{\oplus2}\oplus\chi_{-3}\oplus\chi_5.
\]

Because the three vertices are rational and the graph is connected, the
boundary image is the full two-dimensional invariant edge subspace.  Hence

\[
\boxed{
H_1(\Gamma_{\rm res,\overline{\mathbb Q}},\mathbb Q)
\simeq \chi_{-3}\oplus\chi_5,
\qquad
H_1(\Gamma_{\rm res},\mathbb Q)^{G_{\mathbb Q}}=0.
}
\]

The only constant-coefficient cycles left are

\[
e_{12}^+-e_{12}^-,
\qquad
e_{13}^+-e_{13}^-,
\]

which lie in the two quadratic-character sectors.

## Consequence

The rational invariant loop of Entry 728 was a feature of the complete
carrier graph, not of its extension-resonance support.  Therefore the present
local resonance data provide no topological rational cycle capable of hosting
the desired pairwise obstruction.

This is not yet an unconditional vanishing theorem for the full coefficient
Čech cofiber.  A rational cofiber could still arise from a failure of maximal
rank in the invariant coefficient restriction map, even though no invariant
graph loop remains.  Such a survivor would be a coefficient-level defect, not
a carrier-cycle class, and must be demonstrated by the actual transition
matrices rather than inferred from topology.

In particular, Entry 732 correctly retains the full nonresonant \(e_{23}\)
coefficient object.  The deletion here applies only to the
extension-resonance-support subgraph; it must not be applied to the complete
resolved coefficient Čech complex.

Thus the next test has become one exact rank question.  Let

\[
d_{\rm inv}:C^0_{\rm inv}\longrightarrow C^1_{\rm inv}
\]

be the invariant block built from the two descended simple-crossing packets of
Entry 729; the weighted exceptional resonance summand is zero by Entry 731.
Then

\[
\boxed{
\operatorname{coker}d_{\rm inv}=0
\Longrightarrow
\text{the resolved pairwise-resonance route is closed.}
}
\]

Only a nonzero, source-derived rank defect in \(d_{\rm inv}\) can keep that
route alive.

## Evidence

- Entries 728–732;
- the rank-four exceptional residue and vanishing indicial kernels in Entry
  731;
- allocator claim `seqclaim-78b7231125f9dc6c2b89d82f`.
- epistemic event `ev-000000000346-184d261c-697e-4350-a5ee-aa0b8f2d447a`.

## Next falsifier

Assemble only the invariant restriction block from the exact simple-crossing
transition matrices and compute its rank over \(\mathbb Q\).  Do not append a
formal \(e_{23}\) resonant generator: Entry 731 proves that no such local
coefficient exists.
