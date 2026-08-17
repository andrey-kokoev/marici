---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Three Soft-Corner Slices Do Not Determine the Mixed SNC Extension

## Record

Status: exact finite common-frame falsifier and local extension-space theorem for
the frozen (q_{\mathcal G_{12}}) nine-master module. No carrier cell,
denominator, source master, or normalization is added.

This continues entries 312, 316.

## Deutsch--Popperian claim tested

Freeze

\[
u=\ell_4=E_T,\qquad v=\ell_3,\qquad B=uv.
\]

Entry 316 computed the (u)-normal, (v)-normal, and radial connections on

\[
(u,v)=(\lambda,1),\qquad(1,\lambda),\qquad(\lambda,2\lambda).
\]

The tested claim was that these independently reduced residues already occupy
one common logarithmic frame and therefore directly determine the bivariate
extension.

## Exact falsifier

On the final ((e_7,e_8,e_9)) block, the literal sum of the two axis residues
has characteristic polynomial

\[
\chi_{R_u+R_v}(t)=t(t^2+1/16),
\]

whereas the radial residue has

\[
\chi_{R_{\rm rad}}(t)=t^2(t-1).
\]

They are not constant-conjugate, and their literal commutator is nonzero. The
first six-master block does assemble additively and commute.

This is not a bivariate obstruction. The axis residues were evaluated at
different generic points, (v=1) and (u=1), and each Griffiths--Dwork
reduction may use a different exact-form gauge. A corner comparison requires
one Deligne frame.

## Pure elliptic quotient

Away from (X_1X_2=0), (A) is a unit at the corner and

\[
n=\frac BA=\frac{uv}{A}
\]

is a nodal Legendre coordinate. Hence

\[
d\log n=d\log u+d\log v-d\log A,
\]

with the final term regular. In the canonical (n)-frame the two quotient
residues are the same universal nodal operator (N), up to the commuting
scalar half-residue of the (B^{-1/2}) Kummer twist:

\[
[R_u^{\rm ell},R_v^{\rm ell}]=0,qquad
\operatorname{rank}N=1,qquad N^2=0.
\]

Thus the pure elliptic quotient has no hidden corner obstruction.

## Why all three curves can miss an extension

Let (A_{\rm alg}) be a trivial local algebraic target and put

\[
M=\operatorname{Hom}(V_{\rm ell},A_{\rm alg}),\qquad D=T_M-1.
\]

A cocycle for the local group (mathbb Z^2) is a pair ((a,b)) satisfying

\[
D(b-a)=0,
\]

and coboundaries are ((Dc,Dc)). Triviality on each axis requires
(a,b\in\operatorname{im}D). Modulo diagonal coboundaries, the residual
class is

\[
\boxed{\ker(\text{restriction to both axes})\simeq\operatorname{im}D.}
\]

Its radial restriction is also trivial because
(operatorname{im}(T_M^2-1)=operatorname{im}D) for (N^2=0). Therefore
all three tests in entry 316 can miss a genuine mixed codimension-two class.

## Character refinement

Equivariance confines the hidden class to the elliptic ((--)) character.
The final-block Gysin kernel is

\[
A_{--}=\langle e_6,v_{\rm alg}\rangle.
\]

Consequently:

\[
\boxed{\dim E_{\rm hidden}^{\rm final}=2,}
\]

with scalar coordinates

\[
(\varepsilon_{e_6},\varepsilon_{v_{\rm alg}}).
\]

The source last-three cyclic module contains only the algebraic
(v_{\rm alg}) line, so

\[
\boxed{\dim E_{\rm hidden}^{L_3}=1.}
\]

The remaining five algebraic kernel dimensions have different
(C_2^{(a)}\times C_2^{(b)}) characters and cannot contribute
equivariantly.

## Classification

Even if either scalar is nonzero, it is an extension class supported at the
already frozen SNC incidence (u=v=0):

\[
\text{existing energy carrier}
+
\text{Tate/Kummer/Legendre coefficient extension}.
\]

It does not by itself justify a new carrier generator.

## Exact evidence

- `research/benincasa/soft-corner-common-frame-falsifier.json`;
- `research/benincasa/soft-corner-hidden-extension-space.json`;
- the exact three-slice artifacts of entry 316.

## Next hostile falsifier

Derive the final four-master connection over
(mathbb Q(X_1,u,v)), transport its quotient to the (n=uv/A) Deligne
frame, and compute the antisymmetric off-diagonal residue difference modulo
diagonal coboundaries. The calculation has only two outputs:

\[
(\varepsilon_{e_6},\varepsilon_{v_{\rm alg}}).
\]

Their simultaneous vanishing closes the generic soft-corner extension.
A nonzero value locates a coefficient-supported mixed SNC extension while
leaving the common carrier intact.
