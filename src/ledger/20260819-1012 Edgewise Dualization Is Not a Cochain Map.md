# 1012 — Edgewise Dualization Is Not a Cochain Map

> **Typing correction (Entry 1013).** The final displayed adjointness identity
> in the first version of this entry was dimensionally incorrect.  The
> correctly typed cellular comparison is
> \(D_1\delta_u=\delta_{u^{-1}}D_0\).  Entry 1013 constructs its unique
> diagonal solution up to a global scalar.  The negative result below remains
> valid only for edgewise scaling with the vertex frame left unchanged.

## Fixed hexagon data

Entry 1002's minus primitive is supported at dense chamber vertices (4,5).
In the labelled cycle order

\[
(0,1,4,5,3,2),
\]

these are adjacent positions.  On a signed recombination sheet its primitive
is

\[
\lambda=(0,0,L,-L,0,0),
\qquad L=-16st,
\]

and the frozen edge transports are

\[
u=\left(
\frac{tZ}{A_3},
\frac{s}{ZA_2},
X,
\frac{A_3}{tZ},
\frac{ZA_2}{s},
\frac1X
\right),
\qquad \prod_eu_e=1.
\]

The primal edge cochain

\[
d_e=\lambda_{e+1}-u_e\lambda_e
\]

is supported on exactly the three edges (1,2,3), and its transported
boundary vanishes, reproducing Entry 1002.

## Dual-unit test

Entry 1010 derives the local dual Pochhammer unit.  Depending on whether the
serialized (u_e) is regarded as the monodromy or its square root, the
tempting edgewise transports are

\[
d_e\longmapsto-u_ed_e
\qquad\text{or}\qquad
d_e\longmapsto-u_e^2d_e.
\]

The dual cellular differential uses transport (u_e^{-1}).  The exact checker
computes its cyclic closure obstruction on all four signed sheets.  For both
unit conventions, every obstruction is a nonzero rational function of
(A_2,A_3,Z,X).

Therefore

\[
\boxed{
\operatorname{diag}(-u_e^r),\quad r=1,2,
\text{ does not carry primal coboundaries to dual coboundaries.}
}
\]

## Interpretation

This does not contradict Entry 1010.  The local coefficient

\[
c(M^{-1})=-M c(M)
\]

is correct on each regularized boundary component.  What fails is assembling
those local units independently while leaving the vertex lattice unchanged.
A genuine adjoint regularization must transform vertex and edge frames
together through the global chain/cochain pairing.

The remaining datum is thus irreducibly global:

\[
\boxed{
\text{dual Betti comparison}
\neq
\text{edgewise local dualization}.
}
\]

No Betti obstruction has yet been found; two unauthorized shortcuts have now
been excluded: bare transposition (Entry 1009) and independent edge scaling
(this entry).

## Next falsifier

Derive the twisted period pairing on the six labelled chambers.  Its vertex
and edge comparison frames must satisfy the typed intertwining identity

\[
D_1\delta_u
=
\delta_{u^{-1}}D_0
\]

with the source residue orientations.  Only this identity licenses transport
of the Entry 1002 primitive into the dual Betti complex.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_edgewise_dualization_gate.rs`;
- packet:
  `research/benincasa/string-six-point-edgewise-dualization-gate.json`;
- allocator claim:
  `seqclaim-f7f471c8f430eb9bf5c7fc97`.
- epistemic event:
  `ev-000000000631-d7a14509-2ecb-4639-83b4-807037883909`.
