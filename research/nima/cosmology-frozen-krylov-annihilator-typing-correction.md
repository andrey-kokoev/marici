# The degree-five line is a frozen Krylov statistic, not yet a Leray readout

The replicated rank-25 calculation at the physical half twist remains exact
as finite linear algebra.  Its stronger differential interpretation does not.

The closure routine evaluates the connection matrices at one external point,
reduces a vector to quotient coordinates, and then repeatedly applies those
same pointwise matrices while treating the reduced coordinates as constants.
Only the first source derivative is supplied explicitly.  After that first
step, both the reduced coordinates and the connection vary with the external
parameters.  A genuine iterated Gauss--Manin derivative contains these
derivatives; the frozen routine omits them.

Thus the established object is

\[
\operatorname{Krylov}_{(A_1(p),A_2(p),A_3(p))}(s(p)),
\]

not the fiber of a source-derived differential submodule.  Its replicated
codimension-one annihilator

\[
[a^5]^\vee-[a^4b]^\vee
\]

is correspondingly a frozen-point Krylov covector.  It is not presently
typed as horizontal, physical, supported, or Leray.

## How the defect was exposed

The geometric G12-to-G31 relabeling does descend through every retained
relation in both directions at \(\gamma=-1/2\), and the source covector
recomputes independently.  Nevertheless its contragredient transport is not
the independently computed target frozen-Krylov annihilator.  This is not a
failure of the quotient map.  It exposes the omitted derivative of the
parameter-dependent chart transition and, more fundamentally, the omitted
derivatives in the frozen Krylov iteration itself.

A first black-box attempt to reconstruct \(\partial T\) also showed why free
reducer columns cannot serve as a bundle trivialization: they jump across
nearby points.  Replacing them by a fixed labelled Pluecker chart repairs that
typing defect, but rational reconstruction already exceeds total degree five
in one axis.  The admissible next construction is a tangent-linearized
relation system (one exact elimination plus linear tangent solves), not a
larger sampling census.

## Surviving and withdrawn statements

Survives:

- the five-mark quotient has dimension 26 at the tested primes and pole
  depths;
- the frozen operator Krylov span has ranks 26 generically and 25 at the
  physical half twist;
- its physical frozen annihilator is the displayed degree-five line in the
  certified center Pluecker chart;
- the pointwise cyclic chart relabeling is a legal quotient isomorphism.

Withdrawn pending a tangent-linearized differential calculation:

- that the rank-25 span is a Gauss--Manin source orbit;
- that its annihilator defines a source-inaccessible operational direction;
- that the line can be compared directly with the canonical Leray covector;
- any physical/readout meaning for the line.

The Leray comparison objective therefore terminates at its transport gate:
the proposed input has not yet earned the required differential type.

## Subsequent repair

The raw-before-reduction jet calculation has now supplied the missing
differential type.  It does not recover the old line: the genuine physical
source-jet span stabilizes at rank 19 through orders four and five, whereas
the generic span reaches rank 26 at order four.  See
`cosmology-physical-half-twist-rank-seven-jet-defect.md`.

This also supersedes the family-level conclusions of ledger Entries 887 and
892.  Their claimed minimal rank-26 moving-wall extension and regeneration
from the rank-22 frozen kernel use the same frozen-presentation iteration.
Their recorded ranks survive only as pointwise Krylov statistics; they cannot
override the raw-before-reduction rank-19 horizontal closure.

Evidence:

- `research/nima/checkers/check_rank26_half_twist_kpole_stabilization.py`
- `research/nima/checkers/check_rank26_physical_orbit_annihilator.py`
- `research/nima/checkers/check_rank26_physical_annihilator_chart_transport.py`
- `research/nima/checkers/check_rank26_chart_transport_horizontality.py`
- corresponding prime/result packets, with the last checker retaining the
  bounded failed reconstruction as diagnostic evidence rather than a
  curvature claim.
- epistemic graph correction/supersession event
  `ev-000000002343-e27c47d1-b9f6-4179-8667-7201669c7bfb`.
