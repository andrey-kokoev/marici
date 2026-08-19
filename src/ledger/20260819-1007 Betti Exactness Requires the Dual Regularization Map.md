# 1007 — Betti Exactness Requires the Dual Regularization Map

## Two repaired overreaches

Entry 1004 incorrectly equated dense chamber indices with sparse source-occurrence indices.  Entry 1005 correctly repaired that label transport using Entry 974's permutation, but then made a second, subtler inference:

\[
\text{regularity of source chain denominators}
\Longrightarrow
\text{regularity of a target cochain primitive}.
\]

That inference is not typed.

## Variance

Entry 949's Pochhammer regularization is a chain operation:

\[
\operatorname{Reg}:
C^{\rm rel}_\bullet
\longrightarrow
C^{\rm tw,closed}_\bullet[(M-1)^{-1}].
\]

Entry 1002's primitive is instead a target chamber cochain:

\[
p_{--}=P_{--}\lambda
\in
C^0_{\rm chamber}(\mathcal K_{\rm KN}).
\]

To transport exactness into the Betti lattice one needs the dual map

\[
\operatorname{Reg}^\vee:
(C^{\rm tw,closed}_\bullet)^\vee
\longrightarrow
(C^{\rm rel}_\bullet)^\vee
\]

or an independently normalized chain/cochain intersection pairing.  Neither is contained in the frozen six-point packets.

## Why the support permutation is insufficient

Entry 974 explicitly limits its permutation to

\[
\text{support and labelled ordering only}.
\]

It does not transport rational coefficients, dual bases, or Pochhammer poles.  Therefore

\[
\{4,5\}_{\rm dense}\mapsto\{0,3\}_{\rm occurrence}
\]

is a valid label statement but not a formula for \(\operatorname{Reg}^\vee(p_{--})\).

The loaded incidence matrix \(C\) also cannot be inverted and applied naively: \(\lambda C=r\) is a cochain pullback, while regularization acts covariantly on chains.  Transpose, orientation, and intersection normalization must be derived rather than guessed.

## Result

\[
\boxed{
\text{the arc is cellularly exact, but its exactness in the resonant Betti lattice remains untyped.}
}
\]

Entry 1004 remains fully retracted.  Entry 1005 survives only as the dense-to-occurrence label correction; its generic Betti-exactness conclusion is retracted.

No new carrier divisor or coefficient class is indicated by this failure.  The missing datum is a comparison morphism with the correct variance.

## Finite acceptance test

Construct the source-normalized dual regularization matrix in the frozen bases by requiring simultaneously:

1. compatibility with the exact loaded incidence relation \(\lambda C=r\);
2. the local half-monodromy normalization \(U/(U^2-1)\);
3. the ordered Poincare/intersection orientation;
4. adjointness with the source chamber intersection form;
5. the determinant valuations of Entry 949.

Then apply it to \(p_{--}\) and compute the Laurent grades on the two \((--)\) walls.  Only that result can decide whether cellular exactness survives Betti specialization.

If the source does not fix the intersection form or dual normalization, record the Betti comparison as unavailable; do not select a transpose convention by convenience.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_minus_twisted_cycle_lattice_gate.rs`
- `research/benincasa/string-six-point-minus-twisted-cycle-lattice-gate.json`

The v3 checker retains the valid permutation correction while explicitly separating chain regularization, cochain variance, and the absent dual map.

Epistemic graph event: `ev-000000000626-92b98316-09b6-48d5-8131-6409b1b4f8b6`.
