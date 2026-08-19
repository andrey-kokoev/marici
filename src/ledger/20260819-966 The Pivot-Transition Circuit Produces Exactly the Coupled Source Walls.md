# 966 — The Pivot-Transition Circuit Produces Exactly the Coupled Source Walls

## Minimal coherence cell

Entry 965 rejects standalone loading of the branch-selected \(B_{24}\) and
\(B_{34}\) transition edges.  Retain instead the pre-existing pivot facet and
transition edge as an ordered two-step loaded path.

For rank-one monodromies \(M_A\) and \(M_B\), the group coboundary identity is

\[
\boxed{
M_AM_B-1=(M_A-1)+M_A(M_B-1).
}
\]

The first term is the pivot-facet boundary.  The second is the transition
boundary transported across the pivot sheet.  Their sum is the boundary of
the composite path; no additional cell is introduced.

## Two selected circuits

Using square-root monodromy coordinates gives

\[
\begin{aligned}
(A_3^2-1)+A_3^2(B_{34}^2-1)
&=(A_3B_{34})^2-1,\\
(A_2^2-1)+A_2^2(B_{24}^2-1)
&=(A_2B_{24})^2-1.
\end{aligned}
\]

Therefore the determinant contribution of the two branch-selected circuits
is

\[
\boxed{
\bigl((A_3B_{34})^2-1\bigr)
\bigl((A_2B_{24})^2-1\bigr).
}
\]

These are exactly two of Entry 943's frozen source Fitting factors.  Exact
Symbolica reduction finds no additional irreducible factor.

## Narrow conclusion

The support mismatch in Entry 965 is repaired by the native loaded-path
coherence, not by changing the carrier:

\[
\boxed{
\text{pivot transport converts the bare transition resonance into the
observed coupled source resonance.}
}
\]

This supplies a source-support-compatible mechanism for the two chamber
directions missing in Entry 963.  It does not yet prove the complete
six-by-six de Rham--Betti comparison matrix or its normalization.

## Next falsifier

Assemble the four independent host columns with the two ordered
pivot-transition circuit columns in the frozen six-word basis.  Preserve the
sheet-transport coefficients rather than replacing them by incidence units.
Test:

1. generic rank six;
2. determinant support and valuations against Entry 943;
3. independence from equivalent path representatives through the chamber
   hexagon;
4. compatibility with the existing dense-to-block transition.

Any residual factor not in Entry 943 is a comparison obstruction.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_pivot_transition_circuit.rs`;
- packet:
  `research/benincasa/string-six-point-pivot-transition-circuit.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_pivot_transition_circuit`;
- allocator claim:
  `seqclaim-2db05a576b0f650bab86eeeb`.
- epistemic event:
  `ev-000000000583-31f00561-6780-4939-8817-84c7174a7968`.
