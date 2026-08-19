# 1040 — The Weighted Source Bar Cells Are Horizontal but Their Constant Grades Are Not

## Correction of type

Entry 1038 correctly computes the cellular homology of the source-selected
associated-grade nerve. Its integer face boundaries are not, by themselves,
the unspecialized source bar boundaries.

For multiplicative characters (a,b), put

[
q_a=a-1,qquad q_b=b-1,qquad q_{ab}=ab-1.
]

The source bar relation is weighted:

[
oxed{q_{ab}=q_a+a,q_b.}
]

Thus the coefficient of the second edge is the moving character (a), not a
constant (1). Entry 1038 is recovered at the simultaneous Cartier grade
(a=b=1).

## Exact horizontality calculation

Differentiating the source identity gives

[
dq_{ab}-dq_a-a,dq_b-q_b,da=0.
]

The last term is the first-normal coherence omitted by the constant incidence
matrix. Direct differentiation in both independent character directions
annihilates the complete expression identically.

For the two source transitions this applies with

[
(a,b,ab)=
(M_{Q_1},B_{24}^{,2},M_{Q_2})
]

and

[
(a,b,ab)=
(M_{Q_3},B_{34}^{,2},M_{Q_4}).
]

Therefore both full weighted bar cells are strict morphisms for the
tautological character connection:

[
oxed{Theta_{24}=Theta_{34}=0.}
]

No fitted homotopy is required. The term (q_b,da) is already forced by
differentiating the frozen multiplicative source identity.

## Narrow conclusion

The static closure of Entry 1038 survives the unspecialized character family,
but only after restoring the source weight and its first-normal coherence.
The constant associated-grade face is not an independently horizontal
object.

This is a useful cross-sector pattern:

[
	ext{associated-grade incidence}
quad+quad
	ext{derivative of the multiplicative transition}
quad=quad
	ext{horizontal weighted bar cell}.
]

It supplies no comparison between the two connected components and no
integral descent through the unresolved two-primary projector.

## Next falsifier

The remaining static (H_0congmathbb Q^2) must be typed in the native
source lattice. Compute the integral character saturation without rational
projectors and determine whether the two components remain separate, glue
with finite index, or acquire two-primary torsion. This is now the first
possible obstruction; the rational higher Cousin grades are closed.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_weighted_bar_horizontality.rs`
- `research/benincasa/string-six-point-weighted-bar-horizontality.json`

Epistemic event: `ev-000000000659-7b92f565-cbd5-41a2-a91e-3c51f559d6d1`.
