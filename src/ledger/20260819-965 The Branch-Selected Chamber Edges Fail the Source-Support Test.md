# 965 — The Branch-Selected Chamber Edges Fail the Source-Support Test

## Loading the Entry 964 carrier

The six adjacent-chamber edges exchange neighboring labels in the ordered
triple \((2,3,4)\).  Their half-monodromy labels are

\[
\begin{array}{c|c}
123456--124356&B_{34}\\
123456--132456&X\\
124356--142356&B_{24}\\
132456--134256&B_{24}\\
134256--143256&B_{34}\\
142356--143256&X.
\end{array}
\]

For a standalone loaded boundary, an edge labelled by \(U\) carries the
factor

\[
M_U-1=U^2-1.
\]

## Frozen branch specialization

The source branch imposes

\[
X=1,
\]

equivalently \(s_{23}=0\).  Hence both \(X\)-edge loadings vanish.  Of Entry
964's three unimodular edge pairs, exactly one remains generically active:

\[
\boxed{
(123456--124356,\ 132456--134256),
}
\]

labelled respectively by \(B_{34}\) and \(B_{24}\).

Thus the branch removes the combinatorial ambiguity and selects a unique
carrier pair.

## Support mismatch

Appending these two edges as independent loaded columns multiplies the
unimodular determinant by

\[
(B_{34}^2-1)(B_{24}^2-1).
\]

But Entry 943's frozen source Fitting monomials are

\[
A_2, A_3, A_2B_{24}, A_3B_{34}, ZA_2, ZA_2B_{24},
A_3/Z, A_3B_{34}/Z.
\]

With \(A_2,A_3,B_{24},B_{34},Z\) independent Laurent coordinates,
\(B_{24}\) and \(B_{34}\) are not among these monomials.  Therefore their
standalone resonances are not factors of the source Fitting divisor.

## Narrow conclusion

\[
\boxed{
\text{the branch-selected adjacency edges are the correct carrier
directions, but bare loaded-edge columns are not the source comparison.}
}
\]

The required comparison must couple each transition loading to the pivot
monodromy—producing the observed \(A_2B_{24}\) and \(A_3B_{34}\) channels—or
derive a cancellation through a higher regularization cell.  Adding the bare
edges would create unsupported coefficient walls and is prohibited.

No new carrier stratum is indicated; the failure is entirely in the
coefficient loading.

## Next falsifier

Construct the minimal two-face loaded circuit around each selected edge,
retaining the pivot facets \(A_2\) and \(A_3\).  Test whether its exact circuit
coefficient replaces

\[
B_{24}^2-1,\quad B_{34}^2-1
\]

by the coupled factors

\[
(A_2B_{24})^2-1,\quad(A_3B_{34})^2-1
\]

without additional divisors.  This must be derived from the loaded chamber
boundary, not fitted to Entry 943.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_loaded_transition_gate.rs`;
- packet:
  `research/benincasa/string-six-point-loaded-transition-gate.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_loaded_transition_gate`;
- allocator claim:
  `seqclaim-fd44eb6a8e5587c84edaa3ce`.
- epistemic event:
  `ev-000000000582-0ad36afe-72c4-4432-9e44-bda6c3f79e79`.
