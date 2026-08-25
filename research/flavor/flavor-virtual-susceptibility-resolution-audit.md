# WP164 — virtual-susceptibility resolution audit

## Bounded question

Can a subthreshold virtual response remove WP163's on-shell accessibility
obstruction at finite detector resolution?

## Frozen response and detector

For every continuous protector mode, freeze the low-energy tangent
susceptibility

\[
\chi_a=\frac{g_a^2}{M_a^2},
\qquad g_a=1.
\]

Replace WP162's complement by

\[
(\chi_a,n_a\chi_a,n_a^2\chi_a).
\]

Algebraically, any nonzero \(\chi_a\) preserves the relevant Vandermonde
columns. Type the detector with exact sensitivity

\[
\delta=\frac14.
\]

Responses below \(\delta\) are unresolved and recorded as zero. This is a
frozen threshold detector model, not a claim about an existing apparatus.

## Exact rank comparison

At unit mass,

\[
\chi=1>\delta,
\]

and both formal and detector-typed ranks are seven.

After the common dilation

\[
M:1\longmapsto3,
\qquad
\chi:1\longmapsto\frac19,
\]

the formal response remains nonzero and the exact algebraic rank remains
seven. But

\[
\frac19<\frac14,
\]

so the detector records every tangent susceptibility as zero. The detected
rank collapses to four and the three-dimensional WP161 alias kernel returns.

A partial packet with only the order-three and order-five continuous modes
above sensitivity has detected rank six and kernel dimension one.

## Consequence

Virtual response removes the strict statement that subthreshold modes provide
no mathematical signal. It does not provide uniform physical faithfulness at
fixed resolution:

\[
\text{nonzero formal susceptibility}
\not\Rightarrow
\text{detectable record}.
\]

The source-scale dilation remains a decisive obstruction unless the source
selects a lower mass, a larger coupling, or the instrument supplies a proven
uniform sensitivity bound.

## Typing

- **Admitted state domain:** WP161's seven sources with continuous masses and
  couplings.
- **Faithful flavor quotient:** `physical16`; mass dilation leaves it and the
  return records unchanged.
- **Source-authorized probe family:** virtual tangent susceptibility and its
  two order-conditioned moments.
- **Contextual partition:** detector-relative; full, partial, and aliased
  classes occur as responses cross \(\delta\).
- **Separation:** formal rank seven at every finite benchmark mass; detected
  rank seven, six, or four in the declared packets.
- **Selection:** none.
- **Rigidification:** none.
- **Descent:** susceptibility is a physical source-response scalar under the
  frozen matching law; flavor descent remains full weak-basis invariant.
- **Reference port:** the virtual-response apparatus is a new relational
  experiment.
- **Physical instrument:** response and threshold are typed, but no calibrated
  apparatus or noise model is implemented.

## Smallest exact falsifier

At masses one and three, formal rank is seven in both packets. The dilation
suppresses \(\chi\) from one to \(1/9\), below \(\delta=1/4\), and detector rank
falls to four. This exactly falsifies the inference from algebraic nonzero
response to operational faithfulness.

## Remaining gates

Derive \(g,M\), the susceptibility normalization, backgrounds, integration
time, noise distribution, and detector threshold from a physical apparatus.
Test whether any source-authorized measurement has a uniform lower response
bound over the admitted scale domain. Without such a bound, arbitrarily heavy
continuous rivals remain operationally equivalent to discrete protectors.

## Verification

```text
python research/flavor/checkers/wp164_virtual_susceptibility_resolution.py
```

The dependency-free exact checker writes the JSON result and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 8/10, confidence 10/10, expected information gain
9/10. The expected split between algebraic rank and detector rank was clear.
The confound was the frozen \(g^2/M^2\) law and sharp sensitivity threshold.

Frozen optionality snapshot: unit, partial, and dilated response packets; one
formal rank branch; one detector threshold; ranks seven/six/four; 12 checks;
and no implemented instrument.

Post-objective: excitement 8/10, confidence 10/10, realized information gain
9/10. Virtual response restored formal rank beyond the on-shell domain but not
operational rank. The exact scale dilation preserved algebraic faithfulness
while reopening the full detector kernel. The instrument is more tightly typed,
yet its physical noise and calibration remain absent.

