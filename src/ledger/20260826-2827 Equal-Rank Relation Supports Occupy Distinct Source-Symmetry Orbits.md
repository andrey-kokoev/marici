# 2827 — Equal-Rank Relation Supports Occupy Distinct Source-Symmetry Orbits

## Frozen symmetry test

Entry 2824 produced two equal-rank relation supports with primitive coefficient vectors

\[
L_V=(1,1,3)
\]

and

\[
L_C=(1,1,0)
\]

in the homogeneous site-energy basis \((x,y,z)\).

The admissible test group was frozen as signed permutations of the three labelled site energies, modulo multiplication by a nonzero scalar unit. This contains the homogeneous site relabellings and polarity changes while preserving the meaning of the three source coordinates.

## Orbit result

The two orbits are disjoint. Their invariant discriminator is the number of zero site-energy coefficients:

- every transform of \(L_V\) has full three-coordinate support;
- every transform of \(L_C\) has exactly one zero coefficient.

Geometrically, \(L_V=0\) contains no coordinate axis. The divisor \(L_C=0\) contains one coordinate axis; in the displayed chart this is

\[
x=y=0,
\qquad z\text{ arbitrary}.
\]

Thus the equal-rank relations occupy inequivalent supported objects under the declared source symmetry.

## Physical qualification

Both divisors miss the strict positive-energy chamber. Orbit inequivalence therefore does not by itself produce distinct physical observables. It instead predicts different incidence with existing coordinate-soft support, which is the correct input for a subsequent restriction/Gysin comparison.

## Narrow conclusion

The support distinction in Entry 2824 is not removable by homogeneous labelled-site relabelling or polarity. Bare Koszul rank misses a source-invariant incidence property: containment of a coordinate-soft axis.

The next finite test is local. Restrict both relation objects to coordinate-soft strata and compute their costalk/Gysin maps. The complementary relation has a contained soft axis; the vertex relation meets coordinate-soft strata only transversely. If the resulting supported maps are nevertheless canonically equivalent, this discriminator does not survive the comparison calculus.

## Durable artifacts

- `research/benincasa/check_equal_rank_support_symmetry_orbits.py`
- `research/benincasa/equal-rank-support-symmetry-orbits.json`
