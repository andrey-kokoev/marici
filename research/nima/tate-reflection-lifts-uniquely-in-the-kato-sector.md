# Tate reflection lifts uniquely in the Kato sector

Date: 2026-08-23

The reflection discrepancy was posed independently of the octahedral answer.
Its exact integral homotopy has a unique constrained representative:

\[
H_0:\ 6\text{ supported same-sheet edges},\qquad
H_1:\ 6\text{ mixed faces},\qquad
H_2=0.
\]

The six mixed boundaries are exactly the faces on which the universal
conductor identity

\[
(\epsilon_a-\epsilon_c)
-(\epsilon_b-\epsilon_c)
=\epsilon_a-\epsilon_b
\]

cancels.  Entry 434 instantiates that conductor complex on all 215 actual
loaded PC stalks and verifies all 522 localization squares and 840
two-step routes.  Entry 435 globalizes it as the rigid mixed-variance
transform whose reflection defect is zero.

Consequently the carrier homotopy does lift:

\[
\boxed{
S_{\rm lit}-S_{\rm src}=dH+Hd
\quad\text{in the fs/Kato loaded PC sector}.
}
\]

The minimal representative uses no pure-sheet face and no relative-interior
term.  Those cells belong to the ambient octahedral completion but are gauge
data for this comparison.  The loaded lift is unique because the constrained
homotopy has affine nullity zero and the global framed transform has vanishing
deformation, lift-torsor, and automorphism groups.

This is not a raw-scheme theorem and does not identify the entire
nontrivial-inertia Artin category.  Its exact scope is the trivial-inertia
Kato sector used by the established PC connector.

Evidence:

- `research/nima/checkers/check_tate_loaded_reflection_lift_in_kato_sector.py`
- Entries 324--325, 328, 434--435, 544, and 627.
