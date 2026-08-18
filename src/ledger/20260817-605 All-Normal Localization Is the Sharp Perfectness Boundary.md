# All-Normal Localization Is the Sharp Perfectness Boundary

## Result

For the corrected D03 ringed correspondence of Entries 365--367, global
inversion of one normal parameter removes the telescope-dual obstruction
attached to that parameter.  It does not remove the corresponding
obstructions for the other normal labels.  On the full Entry-352 incidence
space there are nine labels, one for every diagonal of the hexagon, and each
one independently carries a rank-one telescope-dual class.

Consequently the sharp localization boundary for the **full** carrier is

\[
B=R[X][u_d^{-1}:d\text{ a diagonal of }K_6].
\]

Recomputing the extraordinary inverse image over this coefficient ring
makes the D03 dualizing complex perfect.  Any localization omitting even one
of the nine normal parameters leaves a nonperfect stalk witness.

## Why one inversion works locally

Fix a normal parameter \(u\).  Before localization, the obstructing
coefficient is

\[
D_u=R\operatorname{Hom}_A(A[u^{-1}],A),
\]

whose degree-one completion quotient is not finitely generated.  If the
coefficient theory itself is first changed to \(B=A[u^{-1}]\), the same
restriction is recomputed as the identity \(B\to B\), and its dual is simply

\[
R\operatorname{Hom}_B(B,B)=B.
\]

This is a statement about recomputing \(q^!\) after coefficient change.  It
must not be replaced by tensoring the old nonperfect object
\(D_u\) with \(B\): derived Hom from the noncompact module
\(A[u^{-1}]\) need not commute with that base change.

## Exact nine-normal census

The checker repeats Entry 367's filtered target-chain computation for every
diagonal label.  In diagonal order it finds:

| normal label | chain ranks | boundary ranks mod 101 | homology |
| --- | --- | --- | --- |
| \((0,2)\) | \((2,43,96,54)\) | \((0,2,41,54)\) | \((0,0,1,0)\) |
| \((0,3)\) | \((2,43,102,60)\) | \((0,2,41,60)\) | \((0,0,1,0)\) |
| \((0,4)\) | \((2,43,96,54)\) | \((0,2,41,54)\) | \((0,0,1,0)\) |
| \((1,3)\) | \((2,43,96,54)\) | \((0,2,41,54)\) | \((0,0,1,0)\) |
| \((1,4)\) | \((2,43,102,60)\) | \((0,2,41,60)\) | \((0,0,1,0)\) |
| \((1,5)\) | \((2,43,96,54)\) | \((0,2,41,54)\) | \((0,0,1,0)\) |
| \((2,4)\) | \((2,43,96,54)\) | \((0,2,41,54)\) | \((0,0,1,0)\) |
| \((2,5)\) | \((2,43,102,60)\) | \((0,2,41,60)\) | \((0,0,1,0)\) |
| \((3,5)\) | \((2,43,96,54)\) | \((0,2,41,54)\) | \((0,0,1,0)\) |

Every sector has Euler characteristic one and exactly one modular homology
class.  The proof of Entry 367 applies after all spectator normals are made
units, so these are independent omission witnesses: if a localization set
does not contain \(u_d\), the \(u_d\)-completion quotient survives even when
all other normal parameters have already been inverted.

The physical four-normal residue ideal

\[
(u_0,u_1,u_3,u_5)
\]

uses the short-diagonal labels \((0,2),(1,3),(3,5),(1,5)\).  Inverting these
four therefore leaves five full-carrier obstructions: the other two short
diagonals \((0,4),(2,4)\) and all three long diagonals
\((0,3),(1,4),(2,5)\).  Four-normal localization can only be sufficient
after an additional support restriction or quotient removes those five
directions.

## Sufficiency after all nine inversions

After all nine parameters are units, every stalk ring

\[
A_{(S,H)}\otimes B
\]

is canonically \(B\), and every ring restriction in the 215-point target and
1,169-point corrected carrier is the identity.  Entry 366's formula then has
only coefficients \(R\operatorname{Hom}_B(B,B)=B\).  It is a bounded finite
incidence complex because the carrier has finitely many chains and bounded
dimension.  Each finite costandard incidence module has the usual bounded
resolution by finite sums of representables, so the total complex has a
bounded finite-projective compression.  Entry 363's occurrence factor
preserves perfectness, hence the same conclusion holds for \(\omega_q\).

Thus

\[
\boxed{
\omega_q^{(L)}\text{ is perfect on the full carrier}
\iff L\text{ contains all nine normal labels}.
}
\]

Here \(\omega_q^{(L)}\) denotes extraordinary pullback recomputed in the
localized coefficient theory.

## Consequence for Entry 176

The all-normal localization is an excellent diagnostic but a poor final
home for the exceptional cap: it erases every normal-support distinction
that Entry 176's framed relative normal class is designed to retain.  The
next high-information construction is therefore not a literal comparison
after all-normal inversion.  It is a support restriction or Verdier quotient
that kills the five nonphysical carrier directions and the ordinary
telescope sectors while retaining the framed exceptional normal pair.  Only
in that reduced category can the Entry-176 cap be compared to the
exceptional summand of the recomputed dualizing object without destroying
its geometry.

## Evidence boundary

`research/voevodsky/check_d03_ringed_carrier_typing.rs` verifies the unique
degree-zero witness and complete filtered chain complex for each of the nine
labels, including chain ranks, boundary ranks modulo 101, homology, and Euler
characteristic.  The sufficiency statement uses the explicit incidence
formula of Entry 366 and the standard finite representable resolution of a
costandard module on a finite poset.  No identification with Entry 176 is
claimed here.
