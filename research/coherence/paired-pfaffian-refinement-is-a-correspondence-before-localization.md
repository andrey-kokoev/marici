# Paired Pfaffian refinement is a correspondence before localization

## Refining one gap

Replace an old gap weight

\[
\rho=\alpha\gamma\beta
\]

by three gaps \((\alpha,\gamma,\beta)\), thereby inserting two points and preserving configuration parity.

## Ring-generic laws

If the old gap occupied an unselected odd position, then

\[
\tau_{\rm new}=\gamma\tau_{\rm old}.
\]

This is already a forward polynomial transition.

If the old gap occupied a selected even position, no division-free forward formula for \(\tau_{\rm new}\) exists in general. The canonical relation is instead

\[
\rho\tau_{\rm new}
=
\alpha\beta\tau_{\rm old}.
\]

This identity is polynomial and remains valid over every commutative ring, including rings with zero divisors and nonunit gap weights.

## Localization

When \(\rho\) is a unit, the selected-gap relation becomes

\[
\tau_{\rm new}
=
\frac{\alpha\beta}{\rho}\tau_{\rm old}
=
\gamma^{-1}\tau_{\rm old}.
\]

Thus localization upgrades a ring-generic correspondence to an invertible line transition.

## Categorical form

Before localization, the refinement datum should be represented by the span/relation

```text
rho * tau_new = alpha * beta * tau_old
```

rather than by an isomorphism of Pfaffian lines. After adjoining the required unit witness, the span becomes the previously derived transition map.

This gives a clean coefficient-sensitive hierarchy:

```text
commutative ring:
  polynomial Pfaffian correspondence

selected-gap localization:
  invertible Pfaffian line transport
```

## Arithmetic meaning

If \(\rho\) is a nonunit, the relation may fail to determine \(\tau_{\rm new}\) uniquely or may impose divisibility conditions. That ambiguity is the same arithmetic obstruction that prevents the selected hyperbolic pair from being contractible.

Therefore integral cokernel torsion and noninvertible Pfaffian refinement are two manifestations of one missing-unit defect.

## Verification

```text
python research/coherence/check_ring_generic_paired_pfaffian_correspondence.py
```

The checker verifies 500 exact cases over the integers and residue rings modulo 6, 8, 10, and 12.

Artifacts:

- `check_ring_generic_paired_pfaffian_correspondence.py`
- `ring-generic-paired-pfaffian-correspondence.v1.json`
