---
id: 511
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Labelled Principal-Gradient Total Complex Squares to Zero

Entry 509 requires a labelled source model.  The missing datum is not only
the gradient homotopy (H), but also the coefficient of the principal
quartic in each exact operator.

Write every labelled exact generator uniquely in its source-derived form

\[
d(f)=C(f)K+\nabla K\cdot H(f).
\]

For the two columns,

\[
H_p=(0,3m/2,0),
\qquad
H_q=(-3m/2,0,0),
\]

where (m=fL_1^{e_a}L_2^{e_b}), while (C_p,C_q) are the coefficients of
(K) already present in the complete operators.

Using the Euler vector

\[
E=(a/4,0,u/2),
\qquad
\nabla K\cdot E=K,
\]

define the full lift

\[
\boxed{
\widehat H(f)=H(f)+C(f)E.
}
\]

Then

\[
\boxed{
\nabla K\cdot\widehat H(f)=d(f).
}
\]

## Total complex

Let (A) be the labelled exact source, (P) the principal cell, (B) the
scalar target, (G) the three-gradient module, and
(R=B/(K)).  Define

\[
D_{-1}(f,p)
=
\bigl(d(f)+Kp,;\widehat H(f)+Ep\bigr),
\]

\[
D_0(b,g)=b\bmod K-\nabla K\cdot g\bmod K.
\]

The preceding identity gives

\[
\boxed{D_0D_{-1}=0.}
\]

This is the smallest labelled principal-gradient totalization containing all
data required by Entries 508 and 509.  Deleting (P), (C(f)), or the
(K_u) row destroys one of the established comparison identities.

## Consequence

The finite homology calculation now has a typed chain complex.  No
postprocessing of the old image-span matrix is needed, and no new carrier
cell has been added: (P) is the principal conormal cell forced by (K=0).

This entry proves only the chain condition.  It does not yet establish the
stable ranks of this enlarged complex or the induced corrected
(a^2)-action.

## Next falsifier

Instantiate (A,P,B,G,R) at cutoffs (D=12,16,20,24), retain deck
characters and (u^2=0), and compute:

1. stable plus (u)-homology of the total complex;
2. the action induced by Entry 508;
3. whether that action vanishes across (D\to D+2).

Any failure of stable defect rank one already falsifies the proposed total
model before the incidence hypothesis is tested.

## Evidence

- `research/benincasa/marici-gm/src/bin/soft_axis_labelled_total_complex.rs`;
- Entries 487, 493, 508, and 509.
