# Modular sewing as a robust equivariant realization selector

## Problem

The completed scalar boundary condition determines only a relative filling class. Distinct chain representatives can have the same boundary response, and arbitrary right inverses can carry unbounded hidden components. What theta-specific mechanism could remove this internal ambiguity without using zero locations or choosing representatives after scalarization?

## Bold conjecture

**The completed theta source has a parameterized, refinement-compatible family of uniformly bounded reciprocal-equivariant right inverses to its labelled boundary maps. On the reciprocal fixed locus this family descends with the modularly sewn endpoint type, while any off-seam Evans zero forces a named failure of equivariance, refinement compatibility, uniform boundedness, or endpoint type. This incompatibility is the source-level mechanism behind RH.**

More explicitly, this statement requires a declared centered spectral parameter `s` and parameterized objects. For Euler cutoffs `N`, there should be labelled chain spaces `X_N(s)`, boundary spaces `Y_N(s)`, boundary maps `B_N(s)`, reciprocal transports `S_N(s):X_N(s)->X_N(-conjugate(s))` and `T_N(s):Y_N(s)->Y_N(-conjugate(s))`, refinement maps `i_N(s)` and `j_N(s)`, and selectors `K_N(s):Y_N(s)->X_N(s)` satisfying

\[
B_N(s)K_N(s)=I,
\]

\[
S_N(s)K_N(s)=K_N(-\overline s)T_N(s),
\]

\[
i_N(s)K_N(s)=K_{N+1}(s)j_N(s).
\]

On each declared compact parameter set, completed descent additionally requires a source-specified norm and a uniform bound in `N`. The conjectured seam distinction is not finite right-invertibility: it is that the refinement-compatible family extends to the completed source with the sewn endpoint type on the fixed locus `s=-conjugate(s)`, while an off-seam Evans zero forces failure of compatibility, boundedness, or endpoint type. The parameter spaces and norms may not be supplied after observing that failure.

## Named rivals

1. Only a relative filling class exists; no natural strict contraction exists.
2. Equivariant selectors exist at every finite cutoff but their norms diverge, so no completed selector descends.
3. A completed selector exists but is universal and also accepts the hostile two-atom source, giving no RH information.
4. The required selector depends on a basis, anchor, zero location, or fitted metric and is therefore not source-derived.
5. The Evans exclusion law requires different theta-specific data rather than a right-inverse factorization.

## Risky consequences

1. Finite equivariant splitting is not theta-specific: when a right inverse exists and two is invertible, reciprocal averaging constructs one automatically. The discriminating finite quantities are instead the refinement commutator, norm growth, and endpoint-type residual.
2. The fixed-anchor detour may be repaired by averaging at one cutoff; the repaired selector must still be tested for refinement compatibility and uniform boundedness.
3. Boundary-null sequences must obey a uniform observability estimate; a sequence with unit hidden norm and vanishing boundary norm refutes completed descent.
4. The hostile two-atom source must fail at least one named source law before scalar aggregation.
5. The selector must determine the same relative class under basis mutation and Euler-cutoff refinement without representative-specific correction.
6. If the completed selector exists off the seam with the same bounds and source laws, the conjectured RH mechanism is refuted.

## Strongest falsification attempt and exact residual

The finite control fixture has `B=[1,0]` and right inverses `K_alpha=(1,alpha)^T`. It proves `BK_alpha=1` for every hidden gain, while reciprocal equivariance has residual `(0,-2 alpha)^T` and unit-output norm squared `1+alpha^2`. Voevodsky's direct-edge versus fixed-anchor fixture independently shows equal boundaries with a nonnatural representative choice requiring a 2-cell.

These tests eliminate boundary solvability as the explanation. They do not yet test the bold conjecture because the first required typed objects are absent: source cutoff maps, completed chain action, graph topology, and a natural chain-level contraction coherent under modular sewing, basis mutation, and refinement.

## Disposition

The conjecture is open but presently authority-blocked. Its first acceptance test is to materialize one finite labelled theta cutoff with `B_N`, reciprocal actions, and refinement maps, then solve for all equivariant right inverses and compute the minimum operator norm. Do not create further abstract successors until that source packet exists.
