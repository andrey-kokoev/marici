# Degenerate pairing turns rigidity into a radical obstruction class

Epistemic-graph event: 1345.

## Setup

Let the coefficient--Betti pairing on the target complex have right radical

`R_n={x in C_n(H): <a,x>=0 for every coefficient a}`.

Assume Stokes compatibility makes `R` a subcomplex.  Fix one degreewise
adjoint candidate `S`.  Every other graded map preserving all coefficient
pairings is exactly

`S+C`, with `C_n:C_n(G)->R_n`.

## Radical repair theorem

Write `Omega=D_H S-SD_G`.  A pairing-preserving chain-map repair exists if
and only if both conditions hold:

1. the image of `Omega` in `C(H)/R` vanishes;
2. after viewing `Omega` as a radical-valued degree-minus-one map, its class
   vanishes in the Hom-complex cohomology

   `H^(-1)(Hom(C(G),R))`.

Indeed, the corrected defect is

`Omega+delta C`, where `delta C=D_H C-CD_G`.

Because `R` is a subcomplex, every `delta C` is radical-valued, proving the
first necessity.  Once `Omega` is radical-valued, the defect Bianchi identity
`delta Omega=0` makes it a Hom-complex cocycle.  A correction exists exactly
when `Omega=-delta C`, which is the second condition.

## Perfect-pairing limit

If the pairing is perfect, `R=0`; both conditions collapse to `Omega=0`.
Thus Ledger 1313's rigidity is the zero-radical specialization of this
obstruction theory.

## Falsifier

Either a nonzero projected entry of `Omega` in `C(H)/R`, or a nonzero radical
cohomology class `[Omega]`, completely falsifies every pairing-preserving
repair.  Conversely, a displayed radical-valued `C` with
`delta C=-Omega` is a constructive repair certificate, but it establishes a
chain map only relative to the admitted degenerate pairing.

## Physical scope

The five-site formal delta pairing is perfect on sheet labels, but the actual
relative pairing has not been constructed.  If its physical realization is
degenerate, the boundary audit must compute the radical and this two-stage
obstruction rather than assuming uniqueness.  This possibility does not
supply the missing physical complexes.
