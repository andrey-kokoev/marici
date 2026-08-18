---
authors:
  - marici.Nima
date: 2026-08-18
---
# 653 — The Literal Physical Source Occupies the Unique Proper Top Line

## Hard-to-vary claim

In the retained-pivot presentation of the literal three-denominator twisted
de Rham complex, the source representative

\[
\Omega_{111}
=
\frac{dc\wedge da\wedge db}
{q_{g_1}q_{g_2}q_{G_{12}}}
\]

maps nontrivially to the unique proper top quotient. The proper top line is
therefore physically occupied rather than merely available in the ambient
rank-twenty-one coefficient system.

## Retained pivot certificate

Entry 643 established the full deletion-closed rank

\[
\operatorname{rank}M_{111}=21
\]

but its reducer discarded the quotient projection. The extended checker
retains every normalized pivot row and reduces all binary-pole low-space
columns to the same free-column presentation.

The images inherited from the seven proper deletion faces span

\[
\boxed{20}
\]

dimensions. Hence the quotient by all proper faces is one-dimensional, in
agreement with Mobius inversion.

The literal constant-numerator source column has label

\[
(m,n_1,n_2,n_3;\deg c,\deg a,\deg b)
=(0,1,1,1;0,0,0).
\]

Adjoining its reduced class raises the face-span rank from twenty to
twenty-one:

\[
\boxed{
\operatorname{rank}(F_{\rm proper}+\langle\Omega_{111}\rangle)=21.
}
\]

Thus

\[
\boxed{[\Omega_{111}]\ne0\text{ in }M_{111}/F_{\rm proper}.}
\]

## Replication

The complete matrix calculation was run independently at generic Kummer
weights

\[
\gamma=5,
\qquad
\gamma=7,
\]

over \(\mathbb F_{32003}\), with the admitted cutoffs of Entry 643. Both
runs returned

\[
(\operatorname{rank}M,\operatorname{rank}F_{\rm proper},
\operatorname{rank}(F_{\rm proper}+\Omega_{111}))=(21,20,21).
\]

## Relation to the IBP ambiguity

Entry 651 proves that complete logarithmic syzygy primitives have legal
physical Cayley--Menger boundary behavior. Entry 652 finds three minimal
degree-seven primitive choices after all five frozen walls are retained.

The present result fixes the target, not the primitive:

\[
\text{canonical occupied top line}
\quad\ne\quad
\text{canonical primitive selecting a lift}.
\]

It excludes rank zero for any correctly typed source-reduction map that
represents \(\Omega_{111}\), but it does not decide whether the three
minimal five-wall syzygies have image rank one, two, or three before the
relative-exact quotient.

## Updated frontier

Retain the three degree-seven generators from Entry 652 and compute their
boundary-residue matrix in the same quotient presentation. The decisive
data are:

1. the rank of their image;
2. whether that image contains the occupied source top line;
3. the rank remaining after quotienting relative-exact primitive
   differences.

Only rank one with source incidence can canonically reduce the primitive
ambiguity to a normalized line.

## Evidence

- `research/benincasa/physical_three_q_source_top_projection.py`;
- `research/benincasa/physical_three_q_twisted_derham_calibration.py`;
- Entries 643 and 650--652.

## Outcome contract

~~~json
{
  "claim": "The literal source representative dies in the quotient of the rank-twenty-one three-pole complex by all proper deletion faces.",
  "status": "falsified",
  "prime": 32003,
  "generic_gamma_tests": [5, 7],
  "full_rank": 21,
  "proper_face_span_rank": 20,
  "proper_top_quotient_rank": 1,
  "rank_after_adjoining_literal_source": 21,
  "literal_source_occupies_top_line": true,
  "minimal_primitive_choice_rank": 3,
  "canonical_primitive_selected": false,
  "next_experiment": "Compute the boundary-residue matrix of the three minimal complete-wall syzygies and quotient relative-exact differences."
}
~~~
