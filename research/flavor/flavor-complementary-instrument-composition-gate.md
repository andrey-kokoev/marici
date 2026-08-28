# Complementary instrument composition gate

> Superseded scope: WP989 proves that WP986's three complementary coordinate
> rows do not descend through kinetic field normalization. The rank-zero
> instrument conclusion remains valid, but rank four is not the physical
> target; the faithful quotient has dimension two.

Work package: WP987  
Owner: marici.Figueiredo

## Question

Does the full-rank formal family of WP986 already compose from admitted flavor
instruments?

## Domain and quotient

The source domain is the positive four-parameter mediator packet

\[
x=(\log\Gamma,\log A,\log B,\log C).
\]

The faithful coordinate for this audit is the complete source tangent modulo
declared source symmetries. The measured-ten projection is not used. Every
candidate readout must descend through the full weak-basis groupoid and share
one source preparation, threshold map, calibration provenance key, nuisance
model, and detector metric before rows may be stacked.

## Formal and admitted ranks

WP986's formal rows are

\[
r_0=(2,4,-1,-5),\quad r_\Gamma=(1,0,0,0),\quad
r_B=(0,0,1,0),\quad r_C=(0,0,0,1).
\]

They have rank four. Existing work supplies superficially similar, but
source-mismatched fragments:

- WP560 derives a weak-basis-descending trace-adjoint self-quartic entrance and
  names an executed triple-Higgs readout. This is not the WP977 mixed
  \(s\det A\) vertex whose coefficient supplies \(\Gamma\); no declared
  source arrow identifies those couplings.
- WP534 supplies finite-width, Ward-complete gauge poles on a different frozen
  source witness. They are not the WP977 scalar and adjoint mediator poles
  whose masses supply \(B,C\); no declared source arrow identifies them.
- WP892 requires a shared preparation and provenance key and explicitly
  prohibits promoting algebraically chosen tangent rows to operations.

Consequently no WP986 complementary row currently has even a correctly typed
candidate record on the same source witness, and no row has a complete admitted
source-to-calibrated-record arrow on this four-coordinate domain. The
end-to-end admitted response matrix has zero rows and rank zero. In particular,
the formal direct sum of WP560 and WP534 is not a physical composition.

## Exact composition criterion

For each row define seven gates: source operation, weak-basis descent,
threshold transport, finite-width completion, detector response, calibrated
covariance, and shared provenance. A row is executable only if every gate is
true. Rows may be stacked only if their shared-provenance identifiers agree.

The current gate table gives zero executable rows. The smallest repair is not
another algebraic observable: it is one joint likelihood carrying the
quartic-sensitive record and two independently pole-sensitive records through
the same source and calibration frame. Only then may the weighted Gram
determinant test physical rank four.

## Classification and falsifier

Current outcome: the family is a formal constructor separator, neither a
selector nor an admitted instrument. WP560 and WP534 remain valid on their own
domains, but neither is a partial realization of the corresponding WP986 row.
Their juxtaposition does not inherit source identity or authority.

The smallest exact falsifier of a proposed repair is one pair of source
directions whose completed, nuisance-profiled detector responses coincide.
Equivalently, the smallest singular value of the common-frame response reaches
zero within the declared uncertainty set.

## Reproduction

Run:

    python research/flavor/checkers/wp987_complementary_instrument_composition_gate.py

The generated result is
research/flavor/results/wp987_complementary_instrument_composition_gate.json.
