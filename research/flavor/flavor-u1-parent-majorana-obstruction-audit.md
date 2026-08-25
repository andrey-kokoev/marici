# WP157 — U(1)-parent Majorana obstruction

## Bounded question

Does embedding WP154's \(\mathbb Z_4\) character in a gauged continuous
\(U(1)\) independently forbid WP156's charge-two Majorana spectator?

## Frozen minimal Higgsing grammar

Take a gauged \(U(1)\) and a complex scalar \(\Phi\) of charge four. A nonzero
vacuum expectation value leaves the residual subgroup

\[
U(1)\longrightarrow\mathbb Z_4.
\]

Introduce a left-handed Weyl spectator \(N\) of charge two. Before symmetry
breaking, the bare bilinear \(NN\) has charge four and is not \(U(1)\)
invariant. However, the renormalizable operator

\[
y\Phi^\dagger NN
\]

has total charge

\[
-4+2+2=0.
\]

Its field dimension is four. After \(\langle\Phi\rangle=v\), it generates the
Majorana mass

\[
M_N=yv.
\]

The surviving discrete charge of \(N\) is two modulo four, so this is exactly
WP156's symmetry-preserving residue-two Majorana block.

## Exact hostile packet

For the benchmark \((y,v)=(3,5)\), the generated mass is 15. The flavor packet

\[
f=(2,2,2)
\]

has total residue two, and the generated spectator contributes another two:

\[
2+2=0\pmod4.
\]

Thus the minimal continuous gauge parent does not close the spectator domain.
It provides a renormalizable UV origin for the obstruction.

## Architectural consequence

An unbroken continuous fermion number would forbid \(NN\), but then the source
experiment is no longer the isolated gauged \(\mathbb Z_4\) assumed in WP154:
it includes an unbroken gauge symmetry, its gauge field, and new anomaly and
instrument requirements. Once a charge-four condensate creates the desired
residual \(\mathbb Z_4\), the dressed Majorana operator is legal unless a
further source rule forbids it.

Therefore

\[
U(1)\text{ parent}\not\Rightarrow\text{Dirac-only spectator grammar}.
\]

## Typing

- **Admitted state domain:** the minimal charge-four Higgsing sector plus a
  charge-two Weyl spectator.
- **Faithful flavor quotient:** `physical16` downstream; \(\Phi,N\) are UV
  completion data.
- **Source-authorized operations:** gauge-invariant renormalizable operators
  under the frozen charge assignment.
- **Contextual partition:** unbroken-\(U(1)\) phase versus Higgsed residual-
  \(\mathbb Z_4\) phase.
- **Selection:** none; the Higgsed theory admits the residue-two completion.
- **Rigidification:** residual charge classes only.
- **Descent:** the charge equation is gauge-presentation invariant, and the
  induced flavor packet descends under full weak-basis equivalence.
- **Reference port:** keeping the continuous gauge field defines an enlarged
  relational experiment.
- **Physical instrument:** no detector for \(N\), \(\Phi\), or the gauge field
  is supplied.

## Claim boundary

This packet proves only the exact charge and operator-dimension obstruction in
the minimal Higgsing grammar. It does not assert that the full spectrum is free
of continuous, discrete, mixed, or global anomalies. Those calculations are
precisely part of the missing gauge-complete source model.

## Smallest exact falsifier

\[
q(\Phi^\dagger)+q(N)+q(N)=-4+2+2=0.
\]

This single legal dimension-four operator falsifies the claim that a charge-
four \(U(1)\) parent automatically forbids the charge-two Majorana block.

## Reopening condition

Derive an additional gauge or representation constraint that forbids
\(\Phi^\dagger NN\) while retaining the faithful residual \(\mathbb Z_4\)
character. The constraint must be anomaly-consistent and stable under all
renormalizable operators and threshold matching. Setting the Yukawa coupling
to zero without a protecting source law is not a selector.

## Verification

```text
python research/flavor/checkers/wp157_u1_parent_majorana_obstruction.py
```

The dependency-free checker writes the generated JSON and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 9/10, confidence 10/10, expected information gain
9/10. The renormalizable dressed mass made the obstruction sharp. The confound
was restriction to the minimal charge-four Higgsing grammar.

Frozen optionality snapshot: one unbroken continuous phase, one residual-Z4
phase, one charge-two spectator, one legal dressed Majorana operator, one
hostile flavor packet, 12 checks, and no instrument.

Post-objective: excitement 9/10, confidence 10/10, realized information gain
9/10. The naive continuous-parent protection branch was eliminated; the
Majorana obstruction gained a renormalizable UV realization. Keeping the
continuous symmetry unbroken was retyped as a different source experiment.
No complete anomaly cancellation, protecting representation, or physical
instrument was constructed.

