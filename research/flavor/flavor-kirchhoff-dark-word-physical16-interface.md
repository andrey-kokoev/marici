# Kirchhoff Dark-Word `physical16` Interface

## Question

Does WP859's selected two-port ray define a proper family in the faithful
flavor quotient when attached to WP649's source-derived nonaligned frame?

## Oriented spin-one interface

Let (n,m,ell=n\times m) be WP649's ordered source frame and
(J_n,J_m,J_\ell) its spin-one generators. The oriented representation fixes
the complex structure

\[
[J_\ell,J_n]=iJ_m,
\qquad
[J_\ell,J_m]=-iJ_n.
\]

Identify WP859's two junction inputs with (J_n,J_m) and use the oriented
return phase (z=i). The selected dark coefficient vector gives

\[
F_-=rac{J_m-iJ_n}{\sqrt2},
\qquad
[J_\ell,F_-]=F_-.
\]

Thus the portal becomes one chiral ladder word. The quarter-turn is relative
to the oriented source frame; reversing the frame selects the conjugate
ladder. It is not an absolute phase of an unframed flavor experiment.

## Complete minimal Yukawa family

If the source law states that this is the complete nontrivial word allowed in
both sectors, the minimal family is

\[
Y_u=a_uI+F_-,
\qquad
Y_d=a_dI+F_-,
\qquad
a_u,a_d\in\mathbb C.
\]

The fixed portal coefficient contains no fitted magnitude or phase. The two
complex identity offsets remain source coordinates.

At the exact point

\[
a_u=1,
\qquad
a_d=1+i,
\]

both Hermitian squares have nondegenerate spectra: their characteristic
discriminants are (49) and (316). The CP-odd invariant is nonzero,

\[
\operatorname{Im}\operatorname{Tr}[H_u,H_d]^3=6.
\]

Differentiating ten algebraically independent weak-basis invariants with
respect to the four real components of (a_u,a_d) gives exact rank three.
The missing fourth direction is a redundant common phase. Hence the image is
a proper local three-dimensional family inside the intrinsic ten-dimensional
quark quotient.

This is genuine conditional selector behavior on `physical16`, not merely a
chart rigidification. It does not select a unique physical point.

## Additive-map hostile

If instead (F_-) is merely added to arbitrary pre-existing Yukawas,

\[
(Y_u,Y_d)\longmapsto(Y_u+F_-,Y_d+F_-),
\]

the map has the exact inverse obtained by subtracting (F_-). On an
unrestricted base domain it is a translation and selects no proper family.
Therefore source authority must exclude arbitrary base Yukawas and declare
the dark-word grammar complete. A fixed perturbation of a universal carrier
is not a selector.

## Remaining ensemble and instrument gates

The exact witness proves that the selected family is nonempty,
nondegenerate, CP violating, and proper. It does not prove compatibility with
the measured flavor point or all 1,210 fitted sheets. The next decisive test
must fit or eliminate this rank-three family against the measured invariants
without reopening word coefficients.

The source-to-detector map also remains conditional. WP859's complementary
port is an executable source-level probe, but no calibrated experiment yet
identifies its amplitude with variations of the six quark masses, CKM
moduli, and signed Jarlskog coordinate in one common frame.

## Classification

Conditional `physical16` selector with a rank-three invariant image, provided
one source derives the oriented frame, the (z=i) chiral interface, and the
completeness of the dark-word Yukawa grammar. As an additive correction it is
not a selector. Ensemble compatibility and calibrated instrumentation remain
open.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp861_kirchhoff_dark_word_physical16_interface.py
```
