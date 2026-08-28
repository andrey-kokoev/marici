# Additive Portal Zero-Exit Source Audit

## Question

Can an admitted radiative source make the portal unavoidable by generating it
additively at zero, avoiding WP872's multiplicative zero-cusp obstruction?

## Coordinate correction

WP870's Ward gain and the portal coefficient need not be the same running
coordinate. A conserved detector-current coupling is multiplicatively
renormalized, but a scalar portal coefficient can have an additive beta term
when other nonzero source interactions connect the two sectors. Therefore
\(\beta_\delta(0)\ne0\) is physically admissible for a portal even though it
was inadmissible for the Ward gain audited in WP872.

## Admitted additive mechanisms

WP478 gives an explicit messenger threshold

\[
\Delta V_{h^2\phi^2}
=-\frac{3y_Q^2y_\Phi^2}{8\pi^2}h^2\phi^2.
\]

It generates the correct operator and sign from a renormalizable source. Its
magnitude remains proportional to free messenger Yukawas; replacing
\(y_Q\) by \(2y_Q\) multiplies the coefficient by four.

WP729 supplies the stronger RG statement. The primary-source portal beta
contains an additive term, and the representation-labelled pair has zero-
portal sources

\[
(b_A,b_B)=(-4q_A,-3q_B).
\]

Thus zero is not invariant when the Yukawa products are nonzero. The ordered
contrast

\[
b_A-b_B=-4q_A+3q_B
\]

can nevertheless vanish at \(q_B=4q_A/3\).

WP733 removes that cancellation throughout the positive nullcline domain of
the two separately published models. This is a genuine conditional sign
theorem, not a fitted boundary condition.

## Simultaneous-source obstruction

The separate models share Standard Model fields and therefore cannot be
combined without cross anomalous dimensions. WP735 derives the actual
simultaneous one-loop coefficients. On the common nullcline,

\[
\kappa_A
=-\frac{6(4T+12g_1+53g_2)}{103}.
\]

For \(T,g_1,g_2\geq0\), this is nonpositive and is strictly negative whenever
any source coordinate is positive. Hence there is no fully interacting
nonnegative source point with all four required Yukawa squared couplings
positive. The additive portal term is legal, but the simultaneous source
surface needed to make it unavoidable is empty.

This obstruction occurs before portal magnitude, global basin, threshold
survival, or detector calibration can be tested. It is stronger than the
WP729 cancellation fiber because it uses the completed shared-field
backreaction rather than freely variable products.

## Gate classification

- Nonzero generation from zero: physically possible and explicitly realized
  in incomplete messenger/source packets.
- Relative sign: fixed conditionally by separate-model gauge parallelization.
- Simultaneous source existence: fails in the strongest admitted one-loop
  singlet–triplet model.
- Magnitude and basin: unopened because the interacting source surface is
  empty.
- Threshold: messenger matching fixes an operator sign but retains Yukawa and
  finite-matching fibers.
- Readout: representation labels are physical, but no calibrated rank-two
  'physical16' response is derived.

## Smallest exact falsifiers

- At the representation-only level, \(q_B=4q_A/3\) cancels the additive
  contrast.
- At the completed simultaneous level, any positive \(T\), \(g_1\), or \(g_2\)
  makes \(\kappa_A<0\).
- In the messenger threshold, \(y_Q\mapsto2y_Q\) changes the generated
  magnitude by a factor of four.

## Disposition

Negative for the currently admitted additive source, but the mechanism class
remains open. Additive radiative generation is the correct physical way to
escape exact zero without inventing a dual coupling. The present
singlet–triplet realization fails because shared-field backreaction removes
its positive interacting source surface.

A progressive successor must modify that numerator for a reason independently
required by the source, then derive the complete fixed point, global basin,
finite thresholds, and Ward-locked calibrated readout. Adding matter merely
to manufacture a zero is prohibited.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp875_additive_portal_zero_exit_source_audit.py
~~~
