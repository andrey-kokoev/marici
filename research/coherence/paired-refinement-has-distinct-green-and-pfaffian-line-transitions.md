# Paired refinement has distinct Green and Pfaffian line transitions

## Parity-preserving insertion

To compare even Pfaffian stages, refinement must add two points. Replace one old gap correlation \(\rho\) by three successive correlations

\[
\alpha,\gamma,\beta,
\qquad
\rho=\alpha\gamma\beta.
\]

The total number of points increases by two, so all gap parities beyond the refined interval remain unchanged.

## Pfaffian transition

The ordered skew Pfaffian selects even-indexed gaps.

If the replaced gap has even index, it was selected. After refinement, \(\alpha\) and \(\beta\) are selected while \(\gamma\) is not. Therefore

\[
\frac{\operatorname{Pf}M_{\rm new}}
     {\operatorname{Pf}M_{\rm old}}
=
\frac{\alpha\beta}{\rho}
=
\gamma^{-1}.
\]

If the replaced gap has odd index, it was unselected. After refinement only \(\gamma\) is selected, so

\[
\frac{\operatorname{Pf}M_{\rm new}}
     {\operatorname{Pf}M_{\rm old}}
=
\gamma.
\]

Thus insertion inside an existing Pfaffian pair contributes the inverse internal amplitude, while insertion between pairs contributes the internal amplitude.

## Green determinant transition

The positive Green determinant instead transforms by

\[
\frac{\det K_{\rm new}}{\det K_{\rm old}}
=
\frac{(1-\alpha^2)(1-\gamma^2)(1-\beta^2)}
     {1-\rho^2}.
\]

This transition is insensitive to whether the old gap occupied an even or odd parity position.

## Combined line object

A parity-preserving refinement therefore acts on the two line coordinates by

```text
Green determinant line:
  symmetric three-gap innovation factor

skew Pfaffian line:
  gamma^-1 inside a selected pair
  gamma    between selected pairs
```

These factors are independently multiplicative. Their ordered pair is the minimal line-transition datum for the combined Green/Pfaffian target.

## Collision behavior

If either outer new gap collapses, the Green determinant transition vanishes. The Pfaffian transition need not vanish because it depends only on the internal gap \(\gamma\) after cancellation against \(\rho\).

Conversely, as the two inserted points collide with each other, \(\gamma\to1\), the Pfaffian transition tends to one while the Green determinant transition vanishes.

Therefore Green rank degeneration and Pfaffian torsion transport have different collision laws.

## Verification

```text
python research/coherence/check_paired_refinement_line_transitions.py
```

The checker verifies 100 exact rational refinements, split equally between selected and unselected old gaps.

Artifacts:

- `check_paired_refinement_line_transitions.py`
- `paired-refinement-line-transitions.v1.json`
