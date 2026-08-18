---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 680 — The Physical Tangency Residue Norm Has No Quartic Divisor

## Hard-to-vary claim

The determinant divisor of the six physical reduced-tangency residues is
generated entirely by established soft, energy-wall, conductor, and
reduced-tangency-discriminant support. Neither its zero divisor nor its pole
divisor contains the algebraic quartic \(\mathcal Q\).

## Frozen double-cover norm

On shared wall \(i\), let \(h_i(t)=0\) be its reduced quadratic tangency
cover and write the physical residue at a root \(r\) as

\[
\rho_i(r)\sim\frac{N_i(r)}{h_i'(r)D_i(r)}.
\]

The sheet-independent norm is

\[
\operatorname{Nm}_i(\rho_i)
=
\prod_{h_i(r)=0}
\frac{N_i(r)}{h_i'(r)D_i(r)}.
\]

For a quadratic \(h\) with leading coefficient \(c\), exact resultant
identities give

\[
\operatorname{Nm}(\rho)
=
\frac{
\operatorname{Res}(h,N)\,
c^{1+\deg D-\deg N}
}{
\operatorname{Res}(h,h')\,
\operatorname{Res}(h,D)
}
\]

up to the fixed orientation unit. No root choices enter this expression.

## Exact divisor census

Factoring the three norms over \(\mathbb Q[x,y,z]\) gives total zero support

\[
x\,y\,z^4\,(-R_1)\,R_2=0.
\]

The total pole support consists of:

- site-energy factors \(x+z\) and \(y+z\);
- signed-energy factors
  \(x-y-z\), \(x-y+z\), \(x+y-z\), and \(E=x+y+z\);
- the three reduced-tangency discriminant cubics.

The exact gcd tests give

\[
\boxed{
\gcd(\mathcal Q,\operatorname{div}_0\operatorname{Nm}\rho)=1,
\qquad
\gcd(\mathcal Q,\operatorname{div}_\infty\operatorname{Nm}\rho)=1.
}
\]

Thus \(\mathcal Q\) is absent not only from the generic pairing support of
Entries 675 and 677, but also from its sheet-independent boundary-extension
determinant.

## Interpretation

The norm supplies the determinant lattice of the physical weighting across
the conductor and ramification boundaries. It does not determine the
individual-sheet extension: opposite valuations or nontrivial deck
monodromy can cancel in the norm. Therefore this result does not yet prove
that the rank-one quotient is locally free across every boundary component.

What it does exclude is sharper:

\[
\boxed{
\mathcal Q\text{ is not a zero, pole, or ramification determinant of the
physical exceptional pairing.}
}
\]

No new carrier stratum is indicated.

## Classification

- existing carrier: shared walls and reduced tangency covers;
- coefficient support: soft/site-energy, signed-energy, conductor, and
  tangency-discriminant divisors;
- new carrier datum: none;
- \(\mathcal Q\)-home: still restricted to off-diagonal supported comparison
  or extension data.

## Next falsifier

Resolve the two sheets of each \(h_i\)-cover near one generic conductor
component and compute the individual residue valuations and deck action.
Test whether the rank-one image admits a saturated logarithmic lattice, or
whether one sheet acquires torsion hidden by the norm.

## Evidence

- \`research/benincasa/derive_physical_tangency_residue_norm.py\`;
- \`research/benincasa/physical-tangency-residue-norm.json\`;
- Entries 668, 673--675, and 677;
- allocator claim \`seqclaim-f6ab5144a917dc6810877cbd\`.

## Outcome contract

~~~json
{
  "claim": "The sheet-independent physical tangency-residue norm has a zero or pole along Q=0.",
  "status": "falsified",
  "total_zero_gcd_with_Q": "1",
  "total_pole_gcd_with_Q": "1",
  "determinant_support_source_derived": true,
  "individual_sheet_extension_determined": false,
  "new_carrier_datum": false,
  "next_experiment": "Compute individual-sheet valuations and deck action near a generic conductor component."
}
~~~
