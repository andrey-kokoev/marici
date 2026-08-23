# Tate eight-cone symmetry does not select the global row map

Date: 2026-08-23

## Exact negative control

The full-log source has 24 Beck--Chevalley rows indexed by

\[
(\sigma,P),
\qquad
\sigma\in\{\pm1\}^3,
\quad P\in\binom{\{1,3,5\}}2.
\]

The literal replacement has 24 rows indexed by six road/sheet halves, two
missing Boolean states, and two Tor grades.  With the established rotation
and reflection actions, both sets are free \(D_3\)-sets with four orbits.
Their permutation characters are identically

\[
(24,0,0,0,0,0),
\]

so both are four copies of the regular representation.

This agreement establishes compatibility, not canonicity.  Equivariant
bijections between two free \(D_3\)-sets with four orbits are counted by

\[
4!\,|D_3|^4
=24\cdot6^4
=31{,}104.
\]

Therefore equal cardinality, Smith rank, and \(D_3\) covariance do not
determine the global row assignment.  Any checker that chooses one of these
bijections without further geometric data fits the desired comparison.

The four source orbits nevertheless carry canonical fingerprints:

1. all three sheet signs are uniform;
2. the contracted pair has equal signs and the complementary sign is
   opposite;
3. the contracted pair is mixed in cyclic-forward order; and
4. the contracted pair is mixed in cyclic-backward order.

These are invariant under the signed \(D_3\) action.  Thus the next problem
is finitely reduced: derive a bijection from these four fingerprints to the
four target decorations

\[
(\text{missing Boolean state type},\operatorname{Tor}\text{ grade}).
\]

Matching them by enumeration would still be a choice.  The actual
normalization--conductor stalk maps must determine the matching.

## Consequence

The universal conductor kernel must do more than reproduce the correct
representation.  Its actual occurrence/multi-Rees stalk maps must select:

- the correspondence between the four source and four target orbits; and
- one based phase in each regular orbit.

Only after those choices are derived may the eight-cone boundary be compared
with Entry 251's six short-facet defect.

## Evidence

- `research/nima/checkers/check_tate_eight_cone_d3_assignment_ambiguity.py`
- Entries 251, 259--262, and 627.
