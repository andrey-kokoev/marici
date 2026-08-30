# WP150 — fixed-point Euler-correction audit

## Bounded question

When WP149's natural order-96 flavor action has fixed strata, does the properly
corrected Euler quotient still enforce WP148's modulus-four topology selector?

## Correctly typed quotient identity

For a finite group acting cellularly on a finite-CW-type source geometry,
Burnside averaging gives

\[
\chi(X/G)=\frac1{|G|}\sum_{g\in G}\chi(X^g).
\]

For \(|G|=96\), isolate the identity contribution and define

\[
F=\sum_{g\ne e}\chi(X^g).
\]

Then

\[
96\chi(X/G)=\chi(X)+F,
\qquad
k=\frac{\chi(X)}{24}
=4\chi(X/G)-\frac{F}{24}.
\]

The free-action theorem is precisely the special case \(F=0\).

## Exact correction partition

On the integral-\(k\) packets, write \(F=24r\). The topology residue is

\[
k\equiv-r\pmod4.
\]

Thus the fixed-point data split the source into four exact contextual classes:

| \(r\bmod4\) | \(k\bmod4\) |
|---:|---:|
| 0 | 0 |
| 1 | 3 |
| 2 | 2 |
| 3 | 1 |

For \(\chi(X/G)=1\), the smallest representatives \(F=0,24,48,72\)
produce respectively

\[
k=4,3,2,1.
\]

The same order-96 presentation grammar therefore realizes all four topology
residue classes once fixed-point corrections are admitted.

## Selector disposition

The modulus-four conclusion survives exactly when

\[
F\equiv0\pmod{96}.
\]

That is a new source law; it does not follow from group order. In particular:

- \(\chi(X/G)=1,F=24\) gives \(k=3\), the smallest falsifier of the
  modulus-four claim;
- \(\chi(X/G)=1,F=72\) gives inaccessible \(k=1\), so fixed strata can also
  destroy uniform threshold accessibility;
- \(F=96\) can preserve the congruence, showing that freeness is sufficient
  but not logically necessary. The exact requirement is control of the total
  fixed-point residue.

Consequently WP149's natural order-96 group is only a presentation grammar
unless its source dynamics derives \(F=0\pmod{96}\) over the full admitted
domain.

## Typing

- **Admitted source domain:** finite order-96 cellular actions with
  \(k=\chi(X)/24\) integral.
- **Faithful quotient coordinate:** `physical16` remains the downstream flavor
  quotient; \((\chi(X/G),F)\) is upstream source data.
- **Source-authorized probe family:** Euler characteristic, fixed-set Euler
  characteristics, and the inherited threshold predicate.
- **Contextual partition:** the four classes \(F/24\bmod4\), equivalently the
  four residues of \(k\).
- **Separation:** fixed-point probes separate the residue classes; threshold
  accessibility alone does not separate \(k=2,3,4\).
- **Selection:** none without a source-derived restriction
  \(F=0\pmod{96}\).
- **Rigidification:** order-96 group organization only.
- **Descent:** Burnside averaging is invariant under equivariant presentation
  changes; the resulting flavor readout descends under full weak-basis
  equivalence.
- **Reference port:** fixed-set probes are additional equivariant source data,
  not recovery of an absolute observable.
- **Physical instrument:** absent.

## Smallest exact falsifiers

For modulus-four selection:

\[
\chi(X/G)=1,\quad F=24
\quad\Longrightarrow\quad k=3.
\]

For uniform accessibility:

\[
\chi(X/G)=1,\quad F=72
\quad\Longrightarrow\quad k=1,
\]

whose threshold is above \(3/4\).

## Reopening condition

Derive an equivariant index or anomaly identity forcing the full fixed-point
sum \(F\) to vanish modulo 96 throughout the admitted source family. It is not
enough to check isolated fixed strata or a preferred vacuum. The associated
fixed-set data must have a declared physical or source-geometric instrument
before they can identify source classes.

## Verification

```text
python research/flavor/checkers/wp150_fixed_point_euler_correction.py
```

The dependency-free exact checker writes the JSON result and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 9/10, confidence 9/10 that fixed-point residues
would destroy selection, expected information gain 9/10. The confound was that
the algebraic packets characterize correction data without constructing every
corresponding UV manifold.

Frozen optionality snapshot: one free residue class, three nonzero correction
classes, one congruence-restoring nonfree packet, 12 checks, one corrected
quotient identity, and no physical instrument.

Post-objective: excitement 9/10, confidence 10/10 in the exact conditional
classification, realized information gain 10/10. The first nonfaithful arrow
is localized: forgetting \(F\) collapses four topology residues. The free-only
claim is superseded by the weaker exact condition \(F=0\pmod{96}\). Order-96
selection and uniform accessibility are both eliminated without that new
source law. No instrument was constructed.

