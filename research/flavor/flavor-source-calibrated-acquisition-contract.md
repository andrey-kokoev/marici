# Minimal Source-Calibrated Flavor Acquisition Contract Is Not Yet Schedulable

## Purpose

WP891 leaves five unresolved directions. The smallest physical experiment
capable of attacking more than one must jointly measure absolute portal
normalization and distinguish a source-packet zero from a detector
transmission zero. This packet freezes its acceptance contract before any
apparatus or data are chosen.

## Admitted state domain

The source domain is the selected-completion, full-rank subset of the Spin(5)
mass constructor, transported to the faithful low-energy `physical16`
quotient. Yukawa-discriminant strata remain explicit boundary cases. The
experiment may not replace `physical16` by the measured ten-coordinate
projection.

## Required source operations

The contract requires two independently labelled perturbations
(epsilon_1,epsilon_2) of the ordered portal source. Each must be generated
by a named term in the admitted action and propagated through the same RG and
threshold matching map. Algebraically choosing two tangent vectors is not an
executable source operation.

## Required records

For every setting cell, the acquisition packet must retain:

1. absolute source exposure or luminosity from an independent monitor;
2. signal-channel counts;
3. a complementary output sensitive to transmission zeros;
4. an independently derived background-normal count;
5. efficiency and acceptance calibration;
6. mass and finite-width resolution;
7. detector setting, time, and provenance;
8. the source-frame and threshold-matching identifiers;
9. covariance and support assumptions;
10. raw null outcomes as completed trials.

## Acceptance statistic

Let the calibrated response vector include at least absolute yield, the
complementary zero-classifier output, mass, and width. For the two source
perturbations define

\[
J_{\rm det}=\frac{\partial r}{\partial(\epsilon_1,\epsilon_2)}.
\]

With an independently calibrated positive detector metric (W), the primary
gate is

\[
\operatorname{rank}J_{\rm det}=2,
\qquad
\det(J_{\rm det}^TWJ_{\rm det})>0.
\]

The uncertainty-aware gate additionally requires the lower confidence bound
on the smallest singular value to remain positive. Packet-zero and
transmission-zero hypotheses must be tested on preregistered complementary
records rather than inferred from the selected signal port alone.

## Current readiness audit

The present flavor programme supplies:

- an ordered source frame and Hodge-odd portal direction;
- smooth co-moving transport;
- algebraic mass constructors and exact packet-zero classifiers.

It does not supply:

- a selected completion and numerical source action;
- two executable source perturbation controls;
- a production and decay process;
- an apparatus binding or detector model;
- independent exposure, efficiency, or background calibration;
- raw event cells, mass/width resolution, or covariance;
- a complementary physical output.

Therefore the acquisition candidate has zero admitted event cells and is
`not_schedulable`. Formal rank rows are not promoted.

## Selector boundary

Even a successful experiment would identify coordinates of a realized source
packet. It would not prove that the source dynamics selected that packet from
the admissible family. Instrument faithfulness and source selection remain
independent claims.

## Smallest falsifiers

1. The two declared source perturbations induce proportional detector rows.
2. Exposure calibration is derived from the portal signal itself.
3. The complementary output is reconstructed from the selected port.
4. The smallest singular value reaches zero within uncertainty.
5. Source and detector records lack a common-frame provenance key.
6. A rank-two formal Jacobian exists but no physical control executes either
   perturbation.

## Verdict

The experiment is now exactly specified but not physically bound. The next
advance requires a named production/decay process and an admitted apparatus
surface capable of instantiating these fields. Until then, the correct
portfolio remains empty.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp892_source_calibrated_acquisition_contract.py
~~~
