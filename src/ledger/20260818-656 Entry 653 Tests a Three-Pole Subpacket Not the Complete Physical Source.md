---
authors:
  - marici.Nima
date: 2026-08-18
---
# 656 — Entry 653 Tests a Three-Pole Subpacket, Not the Complete Physical Source

## Scope correction

Entry 653's retained-pivot calculation is correct, but its interpretation as
the literal **complete physical source** is too broad.

## Object actually tested

The calibrated rank-twenty-one complex has denominator labels

\[
(q_{g_1},q_{g_2},q_{G_{12}}).
\]

Its tested constant-numerator column is

\[
\frac{dc\wedge da\wedge db}
{q_{g_1}q_{g_2}q_{G_{12}}}.
\]

Entry 653 proves, correctly, that this column occupies the unique proper top
line of that three-pole subpacket.

## Complete source object

Entries 589 and 596 establish that the physical \(q_{G_{12}}\) contribution
comes from the two five-pole families

\[
\{q_{g_1},q_{g_2},q_{g_3},q_{G_{12}},q_{g_{23}}\},
\]

\[
\{q_{g_1},q_{g_2},q_{g_3},q_{G_{12}},q_{g_{31}}\},
\]

each of rank thirty-five, combined with the source-prescribed occurrence
factor

\[
\frac1{q_{g_{23}}}+\frac1{q_{g_{31}}}.
\]

The rank-twenty-one subpacket omits \(q_{g_3}\) and the occurrence wall. It
is a deletion face of each physical family, not the complete source
summand.

Therefore

\[
\boxed{
\text{Entry 653 proves three-pole top occupancy, not complete physical
five-pole occupancy.}
}
\]

## Consequences for Entries 654--655

Entry 654's typing separation remains valid, but the proposed source side
must be replaced by a retained-presentation rank-thirty-five five-pole
complex before taking \(q_{G_{12}}\) residue.

Entry 655's residue-chain-map theorem also remains valid: exact IBP
corrections have zero wall-cohomology image. Its suggested next experiment
must not freeze Entry 653's subpacket generator as though it were the full
physical source.

## Corrected frontier

Construct the literal labelled five-pole twisted-de-Rham presentations for
the \(g_{23}\) and \(g_{31}\) families and verify rank thirty-five. Retain
their pivot certificates, then:

1. reduce the two source columns;
2. form their prescribed unsplit sum;
3. isolate its quotient relative to all proper deletion faces;
4. only then construct the \(q_{G_{12}}\) Poincare residue and compare it
   with Entry 648's wall cocycle.

The secondary homotopy problem of Entry 655 begins after this source object
is typed correctly.

## Evidence

- `research/benincasa/physical_source_scope_correction.py`;
- Entries 589, 596, 643, and 653--655.

## Outcome contract

~~~json
{
  "claim": "Entry 653's three-pole constant-numerator column is the complete physical q_G12 source summand.",
  "status": "falsified_by_scope",
  "tested_subpacket_denominator_count": 3,
  "physical_family_denominator_count": 5,
  "tested_subpacket_rank": 21,
  "physical_family_rank": 35,
  "entry_653_linear_algebra_valid": true,
  "entry_653_complete_source_interpretation_valid": false,
  "next_experiment": "Build retained-pivot rank-35 five-pole complexes and reduce the source-unsplit pair before Poincare residue."
}
~~~
