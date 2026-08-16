---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Weight-Zero Wall Class Is a Cyclic Kummer Sign System

## Record

Status: the rank-one wall class derived in entry 240 has semisimple
total-energy monodromy \(-1\), trivial unipotent part, and a cyclically
covariant sewing among the three unsplit marked-Cut sectors. The transported
relative chain has the same sign, so the physical period pairing is
single-valued.

The two individual lower-denominator occurrences have not yet been split at
weight \(0\). No multiplicity or cancellation is inferred before that
calculation.

No carrier cell, local-system summand, sign choice, or normalization is
added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the new weight }0\text{ wall class may acquire unipotent monodromy
or fail cyclic covariance.}
}
\]

The finite falsifier was the frozen deck action on the wall cover together
with the source cyclic permutation of ordered marked sectors.

## Frozen class

For the \(q_{\mathcal G_{12}}\)-sector write

\[
\kappa_{12}
=
c_{12}\left[\frac{dn_{12}}{w_{12}}\right],
\]

where

\[
c_{12}
=
\frac{3(X_1-X_2)(X_1+X_2)}
{16(X_1X_2)^{7/2}},
\]

\[
w_{12}^2
=
X_1X_2n_{12}^2-2(X_1+X_2).
\]

Define \(\kappa_{23}\) and \(\kappa_{31}\) by the source cyclic rotation
\((1,2,3)\mapsto(2,3,1)\), preserving the displayed order in each pair.

## Total-energy deck action

The weighted chart has

\[
E_T=\tau^2,
\qquad
A+B=\tau^3n.
\]

A positive loop around \(E_T=0\) sends

\[
\tau\longmapsto-\tau,
\qquad
n\longmapsto-n.
\]

The normalized wall root is

\[
w=\frac{\sqrt K}{\tau^3}
\]

up to the frozen nonzero scalar. Both \(\sqrt K\) and \(\tau^3\) change
sign on this loop, so

\[
w\longmapsto w.
\]

Consequently

\[
\boxed{
\frac{dn}{w}\longmapsto-\frac{dn}{w}.
}
\]

The monodromy decomposition is therefore

\[
\boxed{
T_s=-1,
\qquad
T_u=1,
\qquad
N=\log T_u=0.
}
\]

This is a rank-one Kummer sign system, not a unipotent nearby-cycle line.
It is distinct from the rank-two nodal Legendre quotient of the absolute
nine-master module.

## Endpoint and chain action

The exact primitive in entry 240 is

\[
\frac{nP(n^2)}{w^5}.
\]

It is odd under the deck action, so its opposite endpoint polar-jet vector
also has character \(-1\).

The oriented physical interval from \(-N_0\) to \(+N_0\) is sent by
\(n\mapsto-n\) to the same geometric interval with reversed orientation.
Hence its transported relative-homology class also has character \(-1\).
The period pairing has product character

\[
(-1)_{\rm cohomology}(-1)_{\rm chain}=+1.
\]

Thus the nonzero regularized period of entry 240 is single-valued even
though its coefficient and chain factors are separately sign-twisted.

## Cyclic sewing

The source rotation gives

\[
\boxed{
\rho(\kappa_{12})=\kappa_{23},
\qquad
\rho(\kappa_{23})=\kappa_{31},
\qquad
\rho(\kappa_{31})=\kappa_{12}.
}
\]

No reflection or pair-order reversal occurs. The coefficient squares

\[
c_{ij}^2
=
\frac{9(X_i-X_j)^2(X_i+X_j)^2}
{256(X_iX_j)^7}
\]

were checked under all three cyclic substitutions at 1,728 exact positive
integer triples. The unsquared sign is fixed by the source pair order and
the same \(da\wedge db\) orientation used in entries 225--240.

Therefore the three unsplit sector classes sew as one cyclic family with a
common total-energy sign character.

## Occurrence boundary

Entry 240 used the literal source sum

\[
\frac1{q_{\mathfrak g_{23}}}
+
\frac1{q_{\mathfrak g_{31}}}
\]

before taking the weight-\(0\) wall class. Thus \(\kappa_{12}\) is already
the unsplit \(++\) result. It does not determine whether the two individual
occurrence lifts contribute equally, cancel lower classes before summing,
or carry different endpoint jets.

Accordingly,

\[
\boxed{
\text{unsplit cyclic covariance}
\not\Rightarrow
\text{occurrence-resolved sewing}.
}
\]

No factor \(2\) is asserted at this stage.

## Verdict

The unipotent-or-cyclic obstruction is falsified for the unsplit class:

\[
\boxed{
\text{weight }0\text{ wall system}
=
\text{cyclic rank-one Kummer sign system}.
}
\]

The result remains relative Tate/Kummer coefficient data over the existing
resolved carrier. It supplies no direct Legendre component, absolute
nine-master coordinate, \(L_1\) line, or \(\mathcal Q\) provenance.

## Classification

- existing carrier: unchanged total-energy deck, cyclic marked sectors,
  wall covers, and endpoint flags;
- coefficient local system: rank-one Kummer sign in each sector;
- semisimple monodromy: \(-1\);
- unipotent logarithm: \(N=0\);
- endpoint polar-jet character: \(-1\);
- transported chain character: \(-1\);
- period character: trivial;
- cyclic sewing: verified for unsplit sector sums;
- occurrence-resolved sewing: uncomputed;
- genuinely new carrier datum: none.

## Exact evidence

- `research/benincasa/check_weight_zero_wall_monodromy_cyclic.rs`;
- `research/benincasa/weight-zero-wall-monodromy-cyclic.json`;
- 1,728 exact cyclic coefficient-square tests;
- exact deck-sign and chain-sign assertions;
- warnings-denied optimized Rust compilation and exact JSON comparison.

## Next finite falsifier

Split the two lower-denominator occurrences before the weighted expansion.
For each of

\[
D_{23}
=
\frac1{q_{\mathfrak g_1}q_{\mathfrak g_2}q_{\mathfrak g_3}
q_{\mathfrak g_{23}}},
\qquad
D_{31}
=
\frac1{q_{\mathfrak g_1}q_{\mathfrak g_2}q_{\mathfrak g_3}
q_{\mathfrak g_{31}}},
\]

compute enough grades to reach their individual weight-\(0\) wall classes.
Project each onto the \([dn/w]\) Kummer generator and compare endpoint polar
jets.

Then test whether:

1. the two Kummer coefficients are equal and occurrence forgetting gives
   multiplicity two;
2. they differ but sum to entry 240's coefficient;
3. one or both are exact before summing;
4. cyclic transport preserves both occurrence orbits.

Any answer must reproduce the frozen unsplit sum. Failure does not justify a
new carrier unless an actual missing incidence stratum is derived.

## Outcome contract

~~~json
{
  "claim": "The new weight-0 wall class may acquire unipotent monodromy or fail cyclic covariance.",
  "status": "falsified_for_unsplit_sector_sums",
  "semisimple_character": -1,
  "unipotent_part": 1,
  "N": 0,
  "endpoint_jet_character": -1,
  "relative_chain_character": -1,
  "period_character": 1,
  "cyclic_covariance": ["kappa12->kappa23", "kappa23->kappa31", "kappa31->kappa12"],
  "occurrence_split_status": "uncomputed",
  "new_carrier_incidence": false,
  "next_experiment": "Compute the two individual lower-denominator weight-0 Kummer classes and sew both cyclic occurrence orbits."
}
~~~
