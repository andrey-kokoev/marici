# Nonunit Pfaffian refinement has empty and multiple fibers

## The relation

For refinement inside a selected gap, the ring-generic line relation is

\[
\rho\tau_{\rm new}
=
\alpha\beta\tau_{\rm old}.
\]

If \(\rho\) is not a unit, this relation need not define a map from arbitrary old line coordinates to new ones.

## Composite-ring hostile

Work over \(\mathbb Z/6\) with \(\rho=2\).

The equation

\[
2\tau_{\rm new}=2
\]

has two solutions:

\[
\tau_{\rm new}=1,4.
\]

But

\[
2\tau_{\rm new}=1
\]

has no solution.

Thus the refinement relation can have both multiple and empty fibers.

## Geometric image

Actual chain torsions are not arbitrary independent line coordinates. They arise from one common remaining factor \(r\):

\[
\tau_{\rm old}=r\rho,
\qquad
\tau_{\rm new}=r\alpha\beta.
\]

These geometric pairs always satisfy the cross relation. Over \(\mathbb Z/6\) with \(\rho=2\) and \(\alpha\beta=1\),

\[
2(r)=1(2r)
\]

for every \(r\), even though the relation does not extend to a total map on the ambient old line.

## Correct categorical object

Before localization, the refinement object is not merely a span between two free scalar lines. It should retain the common-factor presentation

\[
r\longmapsto(r\rho,r\alpha\beta)
\]

or its scheme/module-theoretic image.

After localizing \(\rho\), projection to the old coordinate becomes invertible and the presented relation becomes the transition map

\[
\tau_{\rm new}
=
\alpha\beta\rho^{-1}\tau_{\rm old}.
\]

## Consequence

```text
cross-multiplied equality
!= total refinement map
!= equivalence
```

The constructor alphabet must type the ring-generic operation as a presented correspondence with a common-factor witness. The localized operation alone is a line isomorphism.

## Verification

```text
python research/coherence/check_nonunit_pfaffian_correspondence_fibers.py
```

Artifacts:

- `check_nonunit_pfaffian_correspondence_fibers.py`
- `nonunit-pfaffian-correspondence-fibers.v1.json`
