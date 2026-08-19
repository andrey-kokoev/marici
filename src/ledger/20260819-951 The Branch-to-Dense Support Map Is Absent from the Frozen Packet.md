# 951 — The Branch-to-Dense Support Map Is Absent from the Frozen Packet

## Required comparison

Entry 950 asks whether the branch Fitting divisor is the pullback of the full
dense momentum-kernel divisor.  This requires a source-defined ring map from
the sparse (2\times2) block variables to the dense six-word kernel ring.

## Variable audit

The dense kernel is constructed over

\[
R_{\rm dense}
=
\mathbb Q[A_2^{\pm1},A_3^{\pm1},A_4^{\pm1},
X^{\pm1},B_{24}^{\pm1},B_{34}^{\pm1}].
\]

The sparse block uses

\[
(X,Y,Z,Q)
\]

and records only

\[
Q=XYZ.
\]

The only explicit overlap is (X).  No frozen relation expresses (Z), and
hence (Q), in the dense ring.

Therefore the desired occurrence map

\[
R_{\rm sparse}\longrightarrow R_{\rm dense}
\]

is currently undefined.

## Consequence

The branch factors involving

\[
ZA_2,quad ZA_2B_{24},quad A_3/Z,quad A_3B_{34}/Z
\]

cannot be assigned to dense channel monomials by visual factor matching.
Doing so would choose the missing kinematic map after seeing the determinant.

Thus

\[
\boxed{
\text{branch-to-dense support comparison: untyped, not failed.}
}
\]

Entries 949 and 950 remain independently valid in their respective rings.
The claim that one divisor is a restriction/Gysin pullback of the other is
neither proved nor falsified.

## Missing datum

The exact missing source object is the physical six-point
Mandelstam/conservation dictionary embedding the published sparse KLT block
into the dense momentum-kernel coordinates, including orientation and
monodromy conventions.

## Next falsifier

Return to the primary six-point KLT formulas and derive this dictionary before
exponentiation.  Push it to the monodromy torus and test every branch factor.
If no single-valued torus map exists because conservation introduces a
quotient or cover, record that cover explicitly rather than choosing roots.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_support_map_type_gate.rs`;
- packet:
  `research/benincasa/string-six-point-support-map-type-gate.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_support_map_type_gate`;
- allocator claim:
  `seqclaim-8b41f41b1f8ca6e826160878`.
- epistemic event:
  `ev-000000000568-cce26a61-4008-476d-850d-5b6869599a82`.
