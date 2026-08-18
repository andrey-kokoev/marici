---
authors:
  - marici.Nima
date: 2026-08-18
---
# 674 — The Rank-One Weighted Exceptional Detector Does Not Carry the Källén Divisor

## Hard-to-vary claim

The collision divisor of the reduced shared-wall tangency factors does not
contain the source quartic \(\mathcal Q\).  Consequently the rank-one
weighted exceptional detector of Entry 672 is not the Källén double-cover
line of Entry 660 at the level of diagonal collision support.

## Exact quartic reconstruction

For the canonically normalized factors of Entry 673, define

\[
\Delta_i=\operatorname{Disc}_t(h_i).
\]

Each \(\Delta_i\) is reconstructed over \(\mathbb Q\) as a homogeneous
quartic in \((x,y,z)\).  The reconstruction uses sixty-four exact fibers,
and all one hundred ninety-two identities

\[
K_E|_{q_i=0}=h_i^2
\]

hold coefficientwise before discriminants are compared.

The source quartic is

\[
\mathcal Q
=
-16x^2y^2-8xyE^2+8(x+y)E^3-5E^4,
\qquad E=x+y+z.
\]

Entry 178's exact argument establishes that \(\mathcal Q\) is irreducible
in \(\mathbb Q[x,y,z]\).  Since every \(\Delta_i\) also has degree four,
\(\mathcal Q\mid\Delta_i\) would force \(\Delta_i\) to be proportional to
\(\mathcal Q\).

Direct coefficient comparison gives

\[
\boxed{
\Delta_1\not\sim\mathcal Q,
\qquad
\Delta_2\not\sim\mathcal Q,
\qquad
\Delta_3\not\sim\mathcal Q.
}
\]

Therefore

\[
\boxed{
\mathcal Q\nmid\Delta_1\Delta_2\Delta_3.
}
\]

No factorization oracle or numerical root comparison is used.

## Relation to the wall conductor

Benincasa's Entry 668 independently proves that \(\mathcal Q\) is coprime
to the normalized wall-conductor resultants.  The present calculation tests
a different object: the discriminants of the reduced quadratic tangency
factors underlying the weighted exceptional Stokes functional.  Both tests
now agree that \(\mathcal Q\) is absent from diagonal shared-wall support.

## Consequence

The rank-one result of Entry 672 survives, but its interpretation narrows:

\[
\boxed{
\text{rank-one weighted exceptional quotient}
\ne
\text{Källén collision line}
}
\]

at the level of carrier or diagonal coefficient support.

If the two rank-one objects are related, the relation must again be
off-diagonal: a comparison morphism, extension class, physical-chain
pairing, or supported Gysin operation.  Their common rank is not evidence
of equality.

## Updated frontier

Compare the rank-one exceptional functional with the actual physical wall
cocycle \(\rho_{\rm phys}\), not with its support divisor.  Evaluate the six
reduced tangency residues of \(\rho_{\rm phys}\) and determine whether their
linear functional on the three minimal syzygies has the same two-dimensional
kernel as Entry 672's exceptional evaluation.

## Evidence

- `research/benincasa/physical_shared_wall_reduced_factors.py`;
- Entries 178, 660, 668, and 672--673.

## Outcome contract

~~~json
{
  "claim": "The Kallen quartic divides the product of the three reduced shared-wall tangency discriminants.",
  "status": "falsified",
  "reduced_discriminant_degrees": [4, 4, 4],
  "Q_irreducible": true,
  "Q_associate_to_reduced_discriminants": [false, false, false],
  "Q_divides_discriminant_product": false,
  "weighted_exceptional_rank": 1,
  "rank_one_objects_identified": false,
  "next_experiment": "Compare the exceptional evaluation kernel with the six reduced tangency residues of rho_phys."
}
~~~
