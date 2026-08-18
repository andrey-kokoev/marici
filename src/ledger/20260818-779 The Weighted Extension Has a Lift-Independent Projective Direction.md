---
authors:
  - marici.Nima
date: 2026-08-18
---
# 779 — The Weighted Extension Has a Lift-Independent Projective Direction

Entry 778 evaluates the traced exceptional restriction of the rationally
nonsplit extension on every admissible weighted Bunch--Davies lift:

\[
T(c)=
\frac{1}{1+c^2}
\begin{pmatrix}0\\1\\0\\-3\end{pmatrix},
\qquad c>0.
\]

The scalar value is lift-dependent because the source does not fix \(c\).
However, \(1/(1+c^2)\) is nonzero for every admissible real \(c>0\).
Therefore all admissible lifts determine the same projective point

\[
\boxed{
[T(c)]=[0:1:0:-3]
\in\mathbf P(\mathcal E_C^{\rm exc}).
}
\]

Equivalently, they determine the same rank-one coefficient subspace

\[
\ell_{\rm exc}
=\mathbf Q\langle(0,1,0,-3)\rangle.
\]

This line is compatible with the exact chart transition and is
\(\mu_2\)-even.  It is consequently independent of the weighted tangent as
a coefficient direction, even though no normalized physical scalar or
relative-chain functional is defined.

## Scope

The projective line does **not** repair Entry 778's obstruction:

- it supplies no exceptional boundary current;
- it does not normalize the factor \(1/(1+c^2)\);
- it does not define a supported comparison cone;
- it cannot authorize a \(\mathcal Q\)-support test.

What survives canonically is a possible target line for a future
parameter-space thimble current.  Any independently derived physical
current must pair through this line; a current landing in a transverse
coefficient direction cannot represent the weighted specialization of the
Entry 774 extension.

## Evidence

- Entry 778 and its exact formula for \(T(c)\);
- `research/benincasa/check_weighted_extension_chain_pairing_gate.py`;
- allocator claim `seqclaim-9bf097ea42b17749d2118f8d`;
- epistemic event
  `ev-000000000394-bce076fd-a8c4-4a3f-bfbb-b7684a66b39a`.

## Next falsifier

Construct the parameter-space thimble current and test its image in the
exceptional coefficient space.  If the image is not contained in
\(\ell_{\rm exc}\), it does not pair with this extension.  If it is
contained in \(\ell_{\rm exc}\), derive its normalization and prove
independence under admissible changes of \(c\) before forming a supported
cone.
