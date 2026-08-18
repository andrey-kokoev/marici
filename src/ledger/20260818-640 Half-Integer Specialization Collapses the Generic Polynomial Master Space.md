---
authors:
  - marici.Nima
date: 2026-08-18
---
# Half-Integer Specialization Collapses the Generic Polynomial Master Space

## Physical twisted-de-Rham calibration

The zero-denominator three-variable reducer requested in Entry 576 has now
been implemented over \(\mathbf F_{32003}\) at

\[
(X_1,X_2,X_3)=(2,3,4).
\]

It retains separate rational pole levels.  A polynomial vector-field
primitive at level \(m\) has differential

\[
\frac{\operatorname{div}V}{K^m}
+(\gamma-m)\frac{V(K)}{K^{m+1}}.
\]

The pole presentations are joined by the required localization relations

\[
\boxed{
\frac{P}{K^m}=\frac{PK}{K^{m+1}}.
}
\]

Omitting these relations produces a false dimension 29.  That provisional
value is rejected and has no mathematical status.

## Generic-weight calibration

At the admitted generic finite-field weight

\[
\gamma=5,
\]

the image of the degree-five polynomial level-zero numerator space stabilizes
at

\[
\boxed{7}.
\]

The value is already stable at pole depth one from ambient degree nine onward
and remains seven through the tested pole depth four and ambient degree
sixteen.  Thus the block-pole twisted-de-Rham construction reproduces the
published generic-dimensional zero-sector rank without using generic
\(q\)-regulators.

## Half-integer specialization

Repeat the identical calculation at the physical three-dimensional twist

\[
\gamma=-\frac12.
\]

At pole depth one, the level-zero image again stabilizes at seven.  Once the
second rational pole level and its localization transitions are admitted,
the image stabilizes at

\[
\boxed{1}.
\]

It remains one through the tested pole depth four and ambient degree sixteen.
Therefore six generic polynomial master directions become exact in this
literal half-integer localized complex, or cease to be represented in the
level-zero polynomial image.

This is a statement about the image of the declared polynomial numerator
space, not a complete Betti-number computation of the resonant local system.
Additional resonant classes could live first at higher pole level.

## Consequence

The generic rank-seven master module must be constructed before setting
\(d=3\).  Direct specialization of the twisted complex does not preserve its
declared polynomial master presentation:

\[
\boxed{
\text{generic reduction then }\gamma\to-\tfrac12
\neq
\text{reduction after }\gamma=-\tfrac12.
}
\]

This explains why the full top connection cannot be based directly on the
literal \(d=3\) quotient even though the final Picard--Fuchs analysis is
performed at \(d=3\).  One must retain generic \(\gamma\), derive the
filtered connection, and only then take the dimensional specialization with
its limiting lattice.

## Next construction

Extend the admitted generic-weight block-pole reducer by one literal source
denominator \(q^{-1}\).  The next calibration targets are

\[
7\longrightarrow8
\]

for either single lower pole and

\[
7\longrightarrow16
\]

for the \(q_{\mathcal G_{12}}\)-closed family.  Denominator pole levels and
their localization transitions must be retained independently of the
Cayley--Menger pole filtration.

## Evidence

- `research/benincasa/physical_top_twisted_derham_calibration.py`.

## Outcome contract

~~~json
{
  "claim": "Specializing gamma to -1/2 before twisted-de-Rham reduction preserves the generic rank-seven polynomial master presentation.",
  "status": "falsified_in_the_tested_filtered_complex",
  "prime": 32003,
  "kinematics": [2, 3, 4],
  "cutoff_degree": 5,
  "generic_weight": 5,
  "generic_level_zero_image_dimension": 7,
  "physical_weight": "-1/2",
  "physical_level_zero_image_dimension": 1,
  "maximum_tested_pole_depth": 4,
  "maximum_tested_ambient_degree": 16,
  "provisional_dimension_29": "rejected_missing_localization_transitions",
  "next_experiment": "Add one literal q-pole filtration at generic gamma and reproduce the single-pole deletion ranks."
}
~~~
